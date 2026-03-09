#!/bin/bash
# scan-webshell.sh - Advanced local webshell scanner + privilege escalation audit (v5)
# Author: Akbar Wira Nugraha
# Fix v5: ganti process substitution < <(...) dengan temp file agar kompatibel
#         di shared hosting / environment tanpa /dev/fd
#
# Usage: ./scan-webshell.sh
#        (Simpan di /public_html lalu jalankan dari sana)

# -----------------------------
# Basic config
# -----------------------------
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
TARGET_DIR="${SCAN_TARGET:-$SCRIPT_DIR}"

WHITELIST="$TARGET_DIR/vendor"

PATTERNS='passthru|exec|eval|shell_exec|assert|str_rot13|system|phpinfo|base64_decode|chmod|mkdir|fopen|fclose|readfile|show_source|proc_open|pcntl_exec|execute|WScript\.Shell|WScript\.Network|FileSystemObject|Adodb\.stream|gzinflate|strrev|gzdecode|preg_replace.*\/e|create_function|call_user_func|call_user_func_array'

LOGFILE="$SCRIPT_DIR/scan-result-$(date +%F_%H%M%S).log"
TMPFILE="$SCRIPT_DIR/.scanlist_tmp_$$.txt"

SHELL_COUNT=0
TOTAL_SCANNED=0

RED='\033[0;31m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
NC='\033[0m'

# Cleanup tmp on exit
trap 'rm -f "$TMPFILE"' EXIT

echo "[*] Scan started at $(date -u +"%Y-%m-%dT%H:%M:%SZ")" > "$LOGFILE"
echo "[*] Target directory: $TARGET_DIR" >> "$LOGFILE"

if [ "$EUID" -ne 0 ]; then
  echo -e "${YELLOW}[warning]${NC} Disarankan jalankan sebagai root. Melanjutkan..."
  echo "[warning] Non-root run; beberapa cek mungkin tidak lengkap." >> "$LOGFILE"
fi

echo ""
echo -e "${CYAN}[*] Scanning ALL files in: $TARGET_DIR${NC}"
echo -e "${CYAN}[*] Log: $LOGFILE${NC}"
echo "---------------------------------------------------" | tee -a "$LOGFILE"

# --- Build file list ke temp file (hindari process substitution) ---
find "$TARGET_DIR" -type f 2>/dev/null > "$TMPFILE"

TOTAL_FILES=$(wc -l < "$TMPFILE")
echo "[*] Total file ditemukan: $TOTAL_FILES" | tee -a "$LOGFILE"
echo "---------------------------------------------------" | tee -a "$LOGFILE"

# --- Scan setiap file ---
while IFS= read -r file; do

  # Skip whitelist
  case "$file" in
    "$WHITELIST"*) continue ;;
  esac

  # Skip script ini sendiri dan log
  case "$file" in
    *scan-webshell.sh) continue ;;
    *scan-result-*) continue ;;
  esac

  # Skip temp file
  [ "$file" = "$TMPFILE" ] && continue

  # Skip file besar > 500KB
  fsize=$(stat -c%s "$file" 2>/dev/null || echo 0)
  if [ "$fsize" -gt 512000 ]; then
    continue
  fi

  # Skip binary
  if command -v file >/dev/null 2>&1; then
    ftype=$(file -b "$file" 2>/dev/null)
    case "$ftype" in
      *ELF*|*PE32*|*Mach-O*|*gzip*|*bzip2*|*zip*|*PNG*|*JPEG*|*GIF*|*WebP*)
        continue ;;
    esac
  fi

  TOTAL_SCANNED=$((TOTAL_SCANNED + 1))

  # Cek permission world-writable
  perms=$(stat -c "%a" "$file" 2>/dev/null || echo "000")
  case "$perms" in
    777|666)
      echo -e "[${YELLOW}alert: world-writable${NC}] $file (perm: $perms)" | tee -a "$LOGFILE"
      ;;
  esac

  # Scan konten file
  if grep -E -qi "$PATTERNS" "$file" 2>/dev/null; then
    matched=$(grep -E -i -m 1 "$PATTERNS" "$file" 2>/dev/null | head -c 150 | tr -d '\r')
    echo -e "[${RED}WEBSHELL DETECTED${NC}] $file" | tee -a "$LOGFILE"
    echo -e "   ${RED}>> Match:${NC} $matched" | tee -a "$LOGFILE"
    SHELL_COUNT=$((SHELL_COUNT + 1))
  fi

done < "$TMPFILE"

echo "---------------------------------------------------" | tee -a "$LOGFILE"
echo "[*] Scan webshell selesai." | tee -a "$LOGFILE"
echo "[*] Total file diperiksa     : $TOTAL_SCANNED" | tee -a "$LOGFILE"
echo "[*] Total webshell terdeteksi: $SHELL_COUNT" | tee -a "$LOGFILE"

# -----------------------------
# Privilege escalation audit
# -----------------------------
echo ""
echo "===================================================" | tee -a "$LOGFILE"
echo "[*] Privilege escalation & account-change audit" | tee -a "$LOGFILE"
echo "===================================================" | tee -a "$LOGFILE"

vercomp() {
  if [ "$1" = "$2" ]; then return 0; fi
  local IFS=.
  local i
  local -a a b
  a=($1); b=($2)
  local len=${#a[@]}
  if [ ${#b[@]} -gt "$len" ]; then len=${#b[@]}; fi
  for ((i=0; i<len; i++)); do
    local ai=${a[i]:-0}
    local bi=${b[i]:-0}
    if ((10#${ai} > 10#${bi})); then return 1; fi
    if ((10#${ai} < 10#${bi})); then return 2; fi
  done
  return 0
}

raw_uname=$(uname -r)
kernel_ver=$(echo "$raw_uname" | grep -oE '^[0-9]+(\.[0-9]+){0,2}')
IFS='.' read -r k1 k2 k3 <<< "$kernel_ver"
k1=${k1:-0}; k2=${k2:-0}; k3=${k3:-0}
kernel_ver="$k1.$k2.$k3"

echo "[info] Kernel : $raw_uname  (parsed: $kernel_ver)" | tee -a "$LOGFILE"

# Dirty COW
vercomp "$kernel_ver" "4.8.3"; r=$?
if [ $r -eq 2 ]; then
  echo -e "[${RED}vulnerable: Dirty COW CVE-2016-5195${NC}] kernel $kernel_ver < 4.8.3" | tee -a "$LOGFILE"
else
  echo "[info] Dirty COW CVE-2016-5195: tidak vulnerable (upstream >= 4.8.3)" | tee -a "$LOGFILE"
fi

# Dirty Pipe
vercomp "$kernel_ver" "5.8.0"; r=$?
if [ $r -eq 2 ]; then
  echo "[info] Dirty Pipe CVE-2022-0847: tidak affected (kernel < 5.8.0)" | tee -a "$LOGFILE"
else
  dp="maybe"
  if [ "$k1" -eq 5 ]; then
    if   [ "$k2" -lt 10 ]; then dp="yes"
    elif [ "$k2" -eq 10 ]; then vercomp "$kernel_ver" "5.10.102"; [ $? -eq 2 ] && dp="yes" || dp="no"
    elif [ "$k2" -gt 10 ] && [ "$k2" -lt 15 ]; then dp="maybe"
    elif [ "$k2" -eq 15 ]; then vercomp "$kernel_ver" "5.15.25";  [ $? -eq 2 ] && dp="yes" || dp="no"
    elif [ "$k2" -eq 16 ]; then vercomp "$kernel_ver" "5.16.11";  [ $? -eq 2 ] && dp="yes" || dp="no"
    else dp="maybe"; fi
  fi
  case "$dp" in
    yes)   echo -e "[${RED}vulnerable: Dirty Pipe CVE-2022-0847${NC}] kernel $kernel_ver — verifikasi vendor patch." | tee -a "$LOGFILE" ;;
    no)    echo -e "[${GREEN}not vulnerable (upstream)${NC}] Dirty Pipe: $kernel_ver sudah di-patch." | tee -a "$LOGFILE" ;;
    maybe) echo -e "[${YELLOW}potentially vulnerable / vendor-dependent${NC}] Dirty Pipe: $kernel_ver — cek vendor advisory." | tee -a "$LOGFILE" ;;
  esac
fi

echo "" | tee -a "$LOGFILE"
echo "[refs] CVE-2022-0847 | CVE-2016-5195 | CVE-2021-4034 — lihat NVD/vendor advisory." | tee -a "$LOGFILE"

# pkexec / PwnKit
pkexec_found=0
for PKEXEC_PATH in /usr/bin/pkexec /bin/pkexec; do
  if [ -x "$PKEXEC_PATH" ]; then
    pkexec_found=1
    lsout=$(ls -l "$PKEXEC_PATH" 2>/dev/null)
    echo "" | tee -a "$LOGFILE"
    echo "[info] pkexec ditemukan: $lsout" | tee -a "$LOGFILE"
    if [ -u "$PKEXEC_PATH" ]; then
      echo -e "[${YELLOW}alert${NC}] pkexec SUID aktif — cek PwnKit CVE-2021-4034, update polkit." | tee -a "$LOGFILE"
    fi
    polkit_pkgver=""
    if command -v dpkg-query >/dev/null 2>&1; then
      polkit_pkgver=$(dpkg-query -W -f='${Package} ${Version}\n' policykit-1 polkit 2>/dev/null | head -1)
    elif command -v rpm >/dev/null 2>&1; then
      polkit_pkgver=$(rpm -q --qf '%{NAME} %{VERSION}-%{RELEASE}\n' polkit 2>/dev/null | head -1)
    fi
    [ -n "$polkit_pkgver" ] && echo "[info] polkit: $polkit_pkgver" | tee -a "$LOGFILE"
    break
  fi
done
[ $pkexec_found -eq 0 ] && echo "[info] pkexec tidak ditemukan." | tee -a "$LOGFILE"

# /etc/passwd & shadow mtime
echo "" | tee -a "$LOGFILE"
echo "[*] Cek /etc/passwd & /etc/shadow (mtime < 7 hari)..." | tee -a "$LOGFILE"
for f in /etc/passwd /etc/shadow; do
  if [ -e "$f" ]; then
    chk=$(find "$f" -mtime -7 2>/dev/null)
    if [ -n "$chk" ]; then
      echo -e "[${YELLOW}changed${NC}] $f dimodifikasi dalam 7 hari terakhir" | tee -a "$LOGFILE"
    else
      echo "[info] $f tidak diubah dalam 7 hari" | tee -a "$LOGFILE"
    fi
  fi
done

# Auth log
echo "" | tee -a "$LOGFILE"
echo "[*] Cek auth log untuk event akun..." | tee -a "$LOGFILE"
LOG_PAT="useradd|adduser|new user|passwd|password changed|created user|deluser"
loghits=0
for lf in /var/log/auth.log /var/log/secure; do
  [ -f "$lf" ] || continue
  hits=$(grep -Ec "$LOG_PAT" "$lf" 2>/dev/null || echo 0)
  if [ "$hits" -gt 0 ]; then
    grep -Ei "$LOG_PAT" "$lf" 2>/dev/null | while IFS= read -r line; do
      echo -e "[${YELLOW}log-event${NC}] $lf: $line" | tee -a "$LOGFILE"
    done
    loghits=$((loghits + hits))
  fi
done
[ $loghits -eq 0 ] && echo "[info] Tidak ada event useradd/passwd di auth logs." | tee -a "$LOGFILE"

# sudoers
echo "" | tee -a "$LOGFILE"
echo "[*] Cek sudoers mtime < 7 hari..." | tee -a "$LOGFILE"
sudoers_hit=$(find /etc/sudoers /etc/sudoers.d -type f -mtime -7 2>/dev/null)
if [ -n "$sudoers_hit" ]; then
  echo "$sudoers_hit" | while IFS= read -r sf; do
    echo -e "[${YELLOW}changed${NC}] $sf" | tee -a "$LOGFILE"
  done
else
  echo "[info] Tidak ada perubahan sudoers dalam 7 hari." | tee -a "$LOGFILE"
fi

# SUID/SGID
echo "" | tee -a "$LOGFILE"
echo "[*] SUID/SGID files dimodifikasi < 7 hari..." | tee -a "$LOGFILE"
find / -xdev -perm /6000 -type f -mtime -7 -ls 2>/dev/null | tee -a "$LOGFILE" || true
echo "[info] Daftar SUID/SGID semua (200 pertama):" | tee -a "$LOGFILE"
find / -xdev -perm /6000 -type f -ls 2>/dev/null | head -200 | tee -a "$LOGFILE" || true

# Regular users
echo "" | tee -a "$LOGFILE"
echo "[*] User UID >= 1000:" | tee -a "$LOGFILE"
awk -F: '($3 >= 1000 && $1 != "nobody"){print $1":"$3":"$6}' /etc/passwd 2>/dev/null | tee -a "$LOGFILE" || true

# Final summary
echo "" | tee -a "$LOGFILE"
echo "---------------------------------------------------" | tee -a "$LOGFILE"
echo "[*] Audit selesai. Log: $LOGFILE" | tee -a "$LOGFILE"

echo ""
echo "╔══════════════════════════════════════════╗"
echo "║              HASIL SCAN                  ║"
echo "╠══════════════════════════════════════════╣"
printf "║  Total file diperiksa    : %-14s║\n" "$TOTAL_SCANNED"
printf "║  Webshell terdeteksi     : %-14s║\n" "$SHELL_COUNT"
echo "╠══════════════════════════════════════════╣"
printf "║  Log: %-35s║\n" "$(basename "$LOGFILE")"
echo "╚══════════════════════════════════════════╝"
echo ""
echo "Rekomendasi:"
echo " - Webshell ditemukan       -> isolasi host, forensic, preserve log."
echo " - SUID baru mencurigakan   -> verifikasi legitimasi binary."
echo " - /etc/passwd|shadow berubah -> cek akun baru di atas."
echo " - Kernel/polkit heuristik  -> konfirmasi ke vendor OS & NVD."
echo ""

exit 0
