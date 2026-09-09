# 🚀 Orbition Network Multi-Account Automation Bot

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" alt="Status">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
</p>

Skrip bot otomatisasi berbasis Python untuk mengelola multi-akun pada platform airdrop **Orbition Network**. Bot ini dirancang untuk dijalankan melalui terminal (termasuk Termux di Android) dengan sistem menu interaktif, rotasi *User-Agent* acak untuk keamanan anti-deteksi, serta fitur rekap total saldo OBN dari seluruh akun Anda.

---

## ✨ Fitur Utama

- 📂 **Multi-Account Support**: Memproses banyak akun sekaligus secara otomatis menggunakan file `token.txt`.
- 💰 **Cek Profil & Akumulasi OBN**: Menampilkan detail status akun, saldo OBN per akun, serta menghitung **Grand Total Saldo OBN** dari seluruh akun yang terdaftar.
- ⛏️ **Auto Start Mining**: Menjalankan proses penambangan (*AI Mining*) secara otomatis di setiap akun.
- 🎯 **Auto-Scraping & Verifikasi Quest**: Mengambil daftar quest, memfilter quest yang belum selesai, dan mengeksekusi verifikasi/klaim reward secara otomatis.
- 🛡️ **User-Agent Rotation**: Menggunakan *User-Agent* perangkat secara acak dari file lokal untuk menghindari pembatasan bot sederhana dari server.
- 🎛️ **Menu Interaktif**: Memudahkan Anda memilih fitur yang ingin dijalankan sesuai kebutuhan.

---

## 📁 Struktur Direktori Proyek

Pastikan file-file Anda tersusun rapi dalam satu folder yang sama seperti ini:

```text
📂 orbition/
├── 📄 bot.py             # Skrip utama bot
├── 📄 token.txt          # Daftar Bearer Token (satu token per baris)
├── 📄 user-agent.txt     # Daftar User-Agent perangkat/browser
└── 📄 README.md          # Dokumentasi proyek

⚙️ Persyaratan & Cara Instalasi
Pastikan komputer atau perangkat Android (Termux) Anda sudah terinstal Python dan pustaka requests.
 * Clone repository ini:
   git clone [https://github.com/heluvaa/orbition.git](https://github.com/heluvaa/orbition.git)
cd orbition

 * Instal modul/pustaka yang dibutuhkan:
   pip install requests

 * Siapkan File Konfigurasi:
   * token.txt: Buat file bernama token.txt, lalu masukkan Bearer Token akun Anda (satu baris per akun, tanpa tanda kutip).
   * user-agent.txt: Buat file bernama user-agent.txt, lalu isi dengan beberapa variasi string User-Agent seluler (satu baris per User-Agent).
🚀 Cara Penggunaan
 * Jalankan skrip Python melalui terminal atau Termux:
   python bot.py

 * Setelah dijalankan, skrip akan mendeteksi jumlah akun dari token.txt dan menampilkan menu interaktif seperti berikut:
   [+] Berhasil memuat 2 akun dari token.txt

===================================
      MENU UTAMA MULTI-AKUN
===================================
1. Cek Profile & Total OBN (Semua Akun)
2. Start Mining (Semua Akun)
3. Cek & Kerjakan Quest (Semua Akun)
4. Kerjakan Quest & Start Mining (Gabungan - Semua Akun)
5. Jalankan Semua Sekaligus (Semua Akun)
6. Keluar
===================================
Pilih menu (1-6): 

 * Ketik angka sesuai menu yang Anda inginkan (misalnya ketik 5 untuk menjalankan semua fitur secara otomatis ke seluruh akun), lalu tekan Enter.
⚠️ Catatan Keamanan
 * Kerahasiaan Token: Jangan pernah membagikan isi file token.txt atau Bearer Token Anda kepada siapa pun karena token tersebut memberikan akses penuh ke akun Anda.
 * Rate Limit: Jeda waktu (delay) otomatis telah disematkan di dalam skrip untuk menjaga kestabilan request ke server.
📜 Lisensi
Proyek ini dilisensikan di bawah MIT License. Bebas digunakan untuk keperluan pribadi dan pengembangan lanjutan.


