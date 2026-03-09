#!/bin/bash
# scan-webshell.sh - Advanced local webshell scanner + privilege escalation audit (v4)
# Author: Akbar Wira Nugraha (updated v4)
# Description: Scan /public_html untuk SEMUA file (tanpa filter ekstensi)
#              berdasarkan content signature webshell
#              PLUS privilege escalation & account-change quick audit
#
# WARNING: Jalankan sebagai root untuk cek lengkap (SUID files, /var/log, package queries, dll)
# Usage: sudo ./scan-webshell.sh
#        (Simpan script ini di /public_html lalu jalankan dari sana)

# -----------------------------
# Basic config
# -----------------------------
# Jika script dijalankan dari /public_html, TARGET_DIR otomatis ke direktori script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_DIR="${SCAN_TARGET:-$SCRIPT_DIR}"

# Direktori whitelist (abaikan, misal vendor library CMS)
WHITELIST="$TARGET_DIR/vendor"

# Signature fungsi berbahaya (indikasi webshell + obfuscation)
# Lebih lengkap dari v3: tambah pola base64 encoded payload, $_REQUEST/$_POST/$_GET execution
PATTERNS='passthru|exec|eval|shell_exec|assert|str_rot13|system|phpinfo|base64_decode|chmod|mkdir|fopen|fclose|readfile|show_source|proc_open|pcntl_exec|execute|WScript\.Shell|WScript\.Network|FileSystemObject|Adodb\.stream|gzinflate|strrev|gzdecode|base64_decode\(.{100,}\)|preg_replace.*\/e|create_function|call_user_func|call_user_func_array|array_map.*eval|\$_(REQUEST|POST|GET|COOKIE|SERVER)\s*\[.*\]\s*\(|\$\{.{0,30}\}.*eval|popen\s*\(|curl_exec|wget|python\s+-c|perl\s+-e|nc\s+-e|bash\s+-i|/bin/sh|/bin/bash'

# Log file (disimpan di direktori yang sama dengan script)
LOGFILE="$SCRIPT_DIR/scan-result-$(date +%F_%H%M%S).log"

# Counter
SUSP_COUNT=0
SHELL_COUNT=0
TOTAL_SCANNED=0

# Warna output
RED='\033[0;31m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
NC='\033[0m'

# Ensure logfile exists
echo "[*] Scan started at $(date -u +"%Y-%m-%dT%H:%M:%SZ")" > "$LOGFILE"
echo "[*] Target directory: $TARGET_DIR" >> "$LOGFILE"
echo "[*] Script location : $SCRIPT_DIR" >> "$LOGFILE"

# Check running user
if [ "$EUID" -ne 0 ]; then
  echo -e "${YELLOW}[warning]${NC} Disarankan jalankan sebagai root untuk audit lengkap. Melanjutkan..."
  echo "[warning] Non-root run; beberapa cek mungkin tidak lengkap." | tee -a "$LOGFILE"
fi

echo ""
echo -e "${CYAN}[*] Scanning ALL files in: $TARGET_DIR${NC}"
echo -e "${CYAN}[*] Log akan disimpan di : $LOGFILE${NC}"
echo "---------------------------------------------------" | tee -a "$LOGFILE"

# ---------- Webshell scan - SEMUA FILE (tanpa filter ekstensi) ----------
while IFS= read -r -d '' file; do

  # Skip direktori whitelist
  if [[ "$file" == "$WHITELIST"* ]]; then
    continue
  fi

  # Skip script scan-webshell itu sendiri
  if [[ "$file" == "${BASH_SOURCE[0]}" ]] || [[ "$file" == "$SCRIPT_DIR/scan-webshell.sh" ]]; then
    continue
  fi

  # Skip log file hasil scan
  if [[ "$file" == "$SCRIPT_DIR/scan-result-"* ]]; then
    continue
  fi

  # Skip file binary murni (non-text) - hanya scan file teks
  if ! file "$file" 2>/dev/null | grep -qiE 'text|script|html|xml|php|ascii|utf'; then
    continue
  fi

  # Skip file besar (>500KB) - bisa disesuaikan
  fsize=$(stat -c%s "$file" 2>/dev/null)
  if [[ -n "$fsize" && "$fsize" -gt 512000 ]]; then
    continue
  fi

  ((TOTAL_SCANNED++))

  # Cek permission world-writable
  perms=$(stat -c "%a" "$file" 2>/dev/null)
  if [[ "$perms" == "777" || "$perms" == "666" ]]; then
    echo -e "[${YELLOW}alert: world-writable${NC}] $file (perm: $perms)" | tee -a "$LOGFILE"
  fi

  # Scan isi file dengan pola webshell
  if grep -E -qi "$PATTERNS" "$file"; then
    # Tampilkan baris/pola yang cocok untuk konteks
    matched_line=$(grep -E -i -m 1 "$PATTERNS" "$file" 2>/dev/null | head -c 120)
    echo -e "[${RED}WEBSHELL DETECTED${NC}] $file" | tee -a "$LOGFILE"
    echo -e "   ${RED}>> Match:${NC} $matched_line" | tee -a "$LOGFILE"
    ((SHELL_COUNT++))
  fi

done < <(find "$TARGET_DIR" -type f -print0 2>/dev/null)

echo "---------------------------------------------------" | tee -a "$LOGFILE"
echo "[*] Scan webshell selesai." | tee -a "$LOGFILE"
echo "[*] Total file di-scan     : $TOTAL_SCANNED" | tee -a "$LOGFILE"
echo "[*] Total webshell terdeteksi: $SHELL_COUNT" | tee -a "$LOGFILE"

# -----------------------------
# Privilege escalation & account-change audit
# -----------------------------
echo ""
echo "===================================================" | tee -a "$LOGFILE"
echo "[*] Privilege escalation & account-change quick audit" | tee -a "$LOGFILE"
echo "===================================================" | tee -a "$LOGFILE"

# helper: compare dotted versions (returns 0 equal, 1 greater, 2 less)
vercomp() {
  if [[ "$1" == "$2" ]]; then
    return 0
  fi
  local IFS=.
  local i
  local -a a=($1) b=($2)
  local len=${#a[@]}
  if [ ${#b[@]} -gt $len ]; then len=${#b[@]}; fi
  for ((i=0; i<len; i++)); do
    local ai=${a[i]:-0}
    local bi=${b[i]:-0}
    if ((10#${ai} > 10#${bi})); then return 1; fi
    if ((10#${ai} < 10#${bi})); then return 2; fi
  done
  return 0
}

# get kernel version
raw_uname=$(uname -r)
kernel_ver=$(echo "$raw_uname" | sed -E 's/^([0-9]+)\.([0-9]+)(\.([0-9]+))?.*/\1.\2.\4/')
if [[ "$kernel_ver" =~ ^([0-9]+)\.([0-9]+)\.$ ]]; then
  kernel_ver="${BASH_REMATCH[1]}.${BASH_REMATCH[2]}.0"
fi
if ! [[ "$kernel_ver" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
  kernel_ver=$(echo "$raw_uname" | grep -oE '^[0-9]+(\.[0-9]+){0,2}')
  parts=(${kernel_ver//./ })
  while [ ${#parts[@]} -lt 3 ]; do parts+=("0"); done
  kernel_ver="${parts[0]}.${parts[1]}.${parts[2]}"
fi

echo "[info] Kernel raw uname  : $raw_uname" | tee -a "$LOGFILE"
echo "[info] Parsed kernel ver : $kernel_ver" | tee -a "$LOGFILE"

# --- Check Dirty COW (CVE-2016-5195) ---
vercomp "$kernel_ver" "4.8.3"
cmp_res=$?
if [ $cmp_res -eq 2 ]; then
  echo -e "[${RED}vulnerable: Dirty COW (CVE-2016-5195) likely${NC}] Kernel < 4.8.3: $kernel_ver" | tee -a "$LOGFILE"
else
  echo "[info] Dirty COW (CVE-2016-5195): kernel >= 4.8.3 -- upstream tidak vulnerable." | tee -a "$LOGFILE"
fi

# --- Check Dirty Pipe (CVE-2022-0847) ---
vercomp "$kernel_ver" "5.8.0"
cmp_dp=$?
if [ $cmp_dp -eq 2 ]; then
  echo "[info] Dirty Pipe (CVE-2022-0847): kernel < 5.8.0 -> tidak affected (upstream)." | tee -a "$LOGFILE"
else
  IFS='.' read -r kmajor kminor kpatch <<< "$kernel_ver"
  dp_vulnerable="unknown"
  if [ "$kmajor" -eq 5 ]; then
    if [ "$kminor" -lt 10 ]; then
      dp_vulnerable="yes"
    elif [ "$kminor" -eq 10 ]; then
      vercomp "$kernel_ver" "5.10.102"
      if [ $? -eq 2 ]; then dp_vulnerable="yes"; else dp_vulnerable="no"; fi
    elif [ "$kminor" -gt 10 ] && [ "$kminor" -lt 15 ]; then
      dp_vulnerable="maybe"
    elif [ "$kminor" -eq 15 ]; then
      vercomp "$kernel_ver" "5.15.25"
      if [ $? -eq 2 ]; then dp_vulnerable="yes"; else dp_vulnerable="no"; fi
    elif [ "$kminor" -eq 16 ]; then
      vercomp "$kernel_ver" "5.16.11"
      if [ $? -eq 2 ]; then dp_vulnerable="yes"; else dp_vulnerable="no"; fi
    else
      dp_vulnerable="maybe"
    fi
  else
    dp_vulnerable="maybe"
  fi

  if [ "$dp_vulnerable" = "yes" ]; then
    echo -e "[${RED}vulnerable: Dirty Pipe (CVE-2022-0847) => YES${NC}] Kernel $kernel_ver - verifikasi vendor patch." | tee -a "$LOGFILE"
  elif [ "$dp_vulnerable" = "no" ]; then
    echo -e "[${GREEN}not vulnerable (upstream patch)${NC}] Dirty Pipe: $kernel_ver terindikasi sudah di-patch." | tee -a "$LOGFILE"
  else
    echo -e "[${YELLOW}potentially vulnerable / vendor-dependent${NC}] Dirty Pipe: $kernel_ver — verifikasi ke vendor/distro." | tee -a "$LOGFILE"
  fi
fi

echo "" | tee -a "$LOGFILE"
echo "[refs] CVE references:" | tee -a "$LOGFILE"
echo " - CVE-2022-0847 (Dirty Pipe)  - NVD / advisories." | tee -a "$LOGFILE"
echo " - CVE-2016-5195 (Dirty COW)   - NVD / advisories." | tee -a "$LOGFILE"
echo " - CVE-2021-4034 (PwnKit)      - polkit pkexec advisories." | tee -a "$LOGFILE"

# --- pkexec / polkit (PwnKit) check ---
PKEXEC_PATH="/usr/bin/pkexec"
if [ -x "$PKEXEC_PATH" ]; then
  mode=$(stat -c "%a" "$PKEXEC_PATH" 2>/dev/null || echo "0000")
  lsout=$(ls -l "$PKEXEC_PATH" 2>/dev/null || true)
  echo "" | tee -a "$LOGFILE"
  echo "[info] pkexec found: $PKEXEC_PATH ($lsout)" | tee -a "$LOGFILE"
  if [ -n "$mode" ] && [ ${mode:0:1} -ge 4 ] || [ -u "$PKEXEC_PATH" ]; then
    echo -e "[${YELLOW}alert${NC}] pkexec hadir; cek PwnKit CVE-2021-4034, update polkit/pkexec jika vulnerable." | tee -a "$LOGFILE"
  else
    echo "[info] pkexec hadir tapi tidak ada SUID bit yang jelas." | tee -a "$LOGFILE"
  fi

  polkit_pkgver=""
  if command -v dpkg-query >/dev/null 2>&1; then
    polkit_pkgver=$(dpkg-query -W -f='${Package} ${Version}\n' policykit-1 2>/dev/null || dpkg-query -W -f='${Package} ${Version}\n' polkit 2>/dev/null || true)
  elif command -v rpm >/dev/null 2>&1; then
    polkit_pkgver=$(rpm -q --qf '%{NAME} %{VERSION}-%{RELEASE}\n' polkit 2>/dev/null || rpm -q --qf '%{NAME} %{VERSION}-%{RELEASE}\n' policykit 2>/dev/null || true)
  fi
  if [ -n "$polkit_pkgver" ]; then
    echo "[info] polkit package: $polkit_pkgver" | tee -a "$LOGFILE"
    echo -e "[${YELLOW}notice${NC}] Jika package lebih lama dari advisory Jan 2022, pertimbangkan update polkit/pkexec." | tee -a "$LOGFILE"
  else
    echo "[info] Tidak bisa menentukan versi polkit via dpkg/rpm." | tee -a "$LOGFILE"
  fi
else
  echo "[info] pkexec tidak ada di $PKEXEC_PATH." | tee -a "$LOGFILE"
fi

# --- Accounts / passwd / shadow changes (last 7 days) ---
echo "" | tee -a "$LOGFILE"
echo "[*] Cek /etc/passwd, /etc/shadow & log akun untuk perubahan dalam 7 hari..." | tee -a "$LOGFILE"

for f in /etc/passwd /etc/shadow; do
  if [ -e "$f" ]; then
    if find "$f" -mtime -7 -print -quit | grep -q .; then
      echo -e "[${YELLOW}changed${NC}] $f dimodifikasi dalam 7 hari terakhir" | tee -a "$LOGFILE"
    else
      echo "[info] $f tidak dimodifikasi dalam 7 hari terakhir" | tee -a "$LOGFILE"
    fi
  fi
done

# Search auth logs for account events
LOG_PATTERNS="useradd|adduser|new user|passwd|password changed|created user|deluser"
loghits=0
logfiles=()
if [ -f /var/log/auth.log ]; then logfiles+=("/var/log/auth.log"); fi
if [ -f /var/log/secure ]; then logfiles+=("/var/log/secure"); fi
logfiles+=($(find /var/log -type f \( -name "auth.log.*" -o -name "secure.*" \) 2>/dev/null))
for lf in "${logfiles[@]}"; do
  if [ -z "$lf" ]; then continue; fi
  if file "$lf" 2>/dev/null | grep -qi gzip; then
    zgrep -Ei "$LOG_PATTERNS" "$lf" 2>/dev/null | while read -r line; do
      echo -e "[${YELLOW}log-event${NC}] $lf: $line" | tee -a "$LOGFILE"
      loghits=$((loghits+1))
    done
  else
    grep -Ei "$LOG_PATTERNS" "$lf" 2>/dev/null | while read -r line; do
      echo -e "[${YELLOW}log-event${NC}] $lf: $line" | tee -a "$LOGFILE"
      loghits=$((loghits+1))
    done
  fi
done
if [ $loghits -eq 0 ]; then
  echo "[info] Tidak ada event useradd/passwd yang ditemukan di auth/secure logs." | tee -a "$LOGFILE"
fi

# --- sudoers modification check ---
echo "" | tee -a "$LOGFILE"
echo "[*] Cek sudoers & /etc/sudoers.d untuk modifikasi < 7 hari ..." | tee -a "$LOGFILE"
if find /etc/sudoers /etc/sudoers.d -type f -mtime -7 -print 2>/dev/null | grep -q .; then
  find /etc/sudoers /etc/sudoers.d -type f -mtime -7 -ls 2>/dev/null | tee -a "$LOGFILE"
else
  echo "[info] Tidak ada modifikasi sudoers dalam 7 hari terakhir." | tee -a "$LOGFILE"
fi

# --- SUID/SGID files modified in last 7 days ---
echo "" | tee -a "$LOGFILE"
echo "[*] Scan file SUID/SGID yang dimodifikasi dalam 7 hari terakhir ..." | tee -a "$LOGFILE"
if [ "$(id -u)" -ne 0 ]; then
  echo "[warning] Scan SUID/SGID mungkin tidak lengkap tanpa root." | tee -a "$LOGFILE"
fi
find / -xdev -perm /6000 -type f -mtime -7 -ls 2>/dev/null | tee -a "$LOGFILE" || true
echo "[info] Daftar SUID/SGID lengkap (200 entri pertama):" | tee -a "$LOGFILE"
find / -xdev -perm /6000 -type f -ls 2>/dev/null | head -n 200 | tee -a "$LOGFILE" || true

# List regular users
echo "" | tee -a "$LOGFILE"
echo "[*] Daftar user UID >= 1000 (regular users):" | tee -a "$LOGFILE"
awk -F: '($3 >= 1000 && $1 != "nobody"){print $1":"$3":"$6}' /etc/passwd 2>/dev/null | tee -a "$LOGFILE" || true

# -----------------------------
# End summary
# -----------------------------
echo "" | tee -a "$LOGFILE"
echo "---------------------------------------------------" | tee -a "$LOGFILE"
echo "[*] Audit privilege escalation selesai." | tee -a "$LOGFILE"
echo "[*] Log lengkap tersimpan di: $LOGFILE" | tee -a "$LOGFILE"

echo ""
echo "╔══════════════════════════════════════════╗"
echo "║              HASIL SCAN                  ║"
echo "╠══════════════════════════════════════════╣"
printf "║  Total file di-scan      : %-14s║\n" "$TOTAL_SCANNED"
printf "║  Webshell terdeteksi     : %-14s║\n" "$SHELL_COUNT"
printf "║  Log disimpan di         :               ║\n"
printf "║  %-40s║\n" "$LOGFILE"
echo "╚══════════════════════════════════════════╝"
echo ""
echo "Rekomendasi tindak lanjut:"
echo " - Jika ada webshell  -> isolasi host, ambil forensic artifact, preserve log."
echo " - Jika ada SUID baru -> verifikasi apakah legitimate atau backdoor."
echo " - Cek kernel/polkit  -> heuristik saja, konfirmasi ke vendor OS (Ubuntu/RHEL/Debian) dan NVD."
echo ""

exit 0
