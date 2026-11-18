# Kafe Nusantara

Aplikasi Streamlit untuk login, melihat menu, membuat pesanan multi-item, dan membuka pesan pesanan yang sudah disiapkan di WhatsApp.

## Menjalankan secara lokal

```powershell
python -m pip install -r requirements.txt
streamlit run login.py
```

Secara default, aplikasi memakai MySQL lokal dengan host `localhost`, user `root`, password kosong, dan database `db_kafe`. Pengaturan koneksi bisa diberikan melalui environment variables `DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASSWORD`, dan `DB_NAME`.
Untuk mengaktifkan tombol WhatsApp secara lokal, atur environment variable `WHATSAPP_PHONE` ke nomor tujuan dengan kode negara tanpa tanda plus.

Sebelum memindahkan database, jalankan migrasi password lokal satu kali:

```powershell
python migrate_passwords.py
```

Migrasi memperbesar kolom password dan menyimpan hash PBKDF2 agar password asli tidak dipindahkan ke database cloud. Login tetap menerima akun lama.

## Deploy ke Streamlit Community Cloud

1. Unggah repository ini ke GitHub.
2. Pastikan database MySQL dapat diakses dari internet atau dari Streamlit Cloud; database `localhost` milik komputer lokal tidak dapat diakses oleh aplikasi yang di-deploy.
3. Di pengaturan aplikasi Streamlit Cloud, pilih repository/branch ini dan set **Main file path** ke `login.py`.
4. Tambahkan rahasia berikut di bagian **Secrets**, dengan kredensial database milik Anda:

```toml
WHATSAPP_PHONE = "NOMOR_TUJUAN_TANPA_PLUS"

[mysql]
host = "HOST_MYSQL"
port = 3306
database = "db_kafe"
user = "USER_MYSQL"
password = "PASSWORD_MYSQL"
```

Database yang di-host harus memiliki tabel `users` dan `menu` beserta data yang diperlukan. Aplikasi membuat tabel `pesanan` dan menambahkan kolom pengelompokan transaksi jika belum ada. Pengguna MySQL yang dikonfigurasi perlu izin membaca tabel tersebut dan membuat/mengubah tabel `pesanan`.

Jangan unggah file `secrets.toml`, `.env`, kredensial database, atau dump database ke GitHub. Simpan konfigurasi database di Secrets Streamlit Cloud.
