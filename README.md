# IDX Scrapper

## Overview

IDX Scrapper merupakan sebuah scrapper yang dibuat menggunakan bahasa Python. Scrapper ini memanfaatkan endpoint-endpoint dari API yang dimiliki oleh PT Bursa Efek Indonesia (BEI) pada websitenya yaitu [idx.co.id](https://idx.co.id).

Apabila Anda tertarik untuk melihat dataset yang dihasilkan dari scrapper ini, kunjungi repository saya yang berisi dataset di [sini](https://github.com/wildangunawan/Dataset-Saham-IDX).

## Cara Penggunaan

Anda dapat langsung menggunakan script yang ada dengan meng-clone atau download repository ini. Setelah berhasil di-download, install library yang dibutuhkan oleh program untuk pekerja. Anda dapat dengan mudah menginstalnya dengan menggunakan pip.
```
pip install -r requirements.txt
```

Untuk penggunaan pertama kali, jalankan file [first-time.sh](first-time.sh). File ini akan mengambil data dari PT Bursa Efek Indonesia sampai dengan 365 hari kerja kebelakang mulai dari saat Anda menjalankannya. Anda dapat mengubah durasi waktu ini dengan mengedit `length` pada file tersebut menjadi banyak hari kerja yang Anda inginkan.

Untuk meng-update data setiap hari, jalankan [daily.sh](daily.sh). Script ini akan mengambil data dari BEI setiap harinya dan menambahkannya ke dalam data yang telah Anda simpan sebelumnya. Anda dapat menjalankan script ini secara otomatis pada server Anda dengan menggunakan cronjob. Saya sarankan Anda untuk menjalankannya pada pukul 17.00 WIB setiap hari kerja saja.

### Penggunaan Untuk Komersial

Mengacu pada [Syarat Penggunaan](https://idx.co.id/footer-menu/tautan-langsung/syarat-penggunaan/) PT Bursa Efek Indonesia Nomor 5:

> Pengguna dilarang menggunakan atau menyebarluaskan Informasi yang diperoleh dari Website kepada pihak lain untuk tujuan komersial tanpa izin tertulis terlebih dahulu dari Bursa Efek Indonesia dan/atau pemilik asal dari Informasi dan atau data tersebut.

Pengguna scrapper ini dilarang keras untuk menggunakan informasi untuk tujuan komersial apapun tanpa persetujuan tertulis dari PT Bursa Efek Indonesia dan/atau pemilik asal data yang Anda ambil. Pemilik projek ini tidak bertanggungjawab apapun apabila pengguna menyalahi aturan ini dan tidak dapat dituntut secara hukum.

## Lisensi

Projek ini dilisensikan dengan CC BY-NC 4.0. Lisensi ini membatasi Anda untuk tidak menggunakan data atau apapun yang berhubungan dengan projek ini untuk tujuan komersial.

Anda dapat membaca lisensi di [sini](LICENSE.md). Rangkuman pendek dari lisensi ini dapat Anda baca di [sini](https://creativecommons.org/licenses/by-nc/4.0/)
