# LiteraLand

## i. Nama Anggota
- Caesar Syahru Ramadhan
- M. Alif Al Hakim
- Farrel Muhammad Hanau
- Michelle Angelica Santoso
- Salma Nurul ‘Aziz

## ii. Cerita Aplikasi dan Manfaatnya
Nama Aplikasi : LiteraLand

Dalam era digital saat ini, membaca buku tetap menjadi salah satu kegiatan yang paling digemari banyak orang. Namun, dengan begitu banyaknya koleksi buku yang ada, seringkali pembaca kesulitan dalam mengingat halaman terakhir yang mereka baca, serta berdiskusi dan menyimpan buku favorit. Oleh karena itu, dibutuhkan sebuah aplikasi yang mampu menyediakan solusi untuk permasalahan tersebut.

LiteraLand adalah aplikasi koleksi buku berbasis web yang memungkinkan pengguna untuk membaca buku pada halaman web. Aplikasi ini menyediakan fitur yang dapat mendukung kegiatan membaca pengguna seperti sistem pencarian dan koleksi buku, pembatas buku, serta forum diskusi/review. Selain itu, aplikasi ini juga memungkinkan untuk membuat ranking buku sesuai personalisasi masing-masing.

## iii. Daftar Modul yang Akan Diimplementasikan
- Modul browse buku. Berisi daftar buku di database secara acak. User juga dapat membuat request ke admin untuk menambahkan buku baru ke database.
- Modul koleksi buku. Berisi informasi koleksi buku yang dipunyai user. 
- Modul ranking. Berisi daftar-daftar list buku favorite dari user.
- Modul review buku. Berisi forum review/diskusi tentang buku.
- Modul admin. Berguna untuk menambahkan buku baru ke database dan menerima pesan request dari user.


## iv. Sumber dataset katalog buku
- Google Book Dataset (https://www.kaggle.com/datasets/bilalyussef/google-books-dataset) - Berisi informasi mengenai judul, penulis, bahasa, kategori, rating umur, publisher, tanggal terbit, jumlah halaman, deskripsi, dan ISBN dari buku.
- Google Book API (https://developers.google.com/books/) - Berguna untuk menampilkan konten buku dari Google Books secara langsung di halaman web. 


## Role atau peran user
- Guest (User yang belum memiliki akun dan belum login hanya dapat melihat i nformasi terkini yang sudah disediakan oleh admin, serta dia hanya dapat melihat urutan rank dari buku yang ada)
- User (Pengguna yang sudah terautentifikasi bisa mengakses hampir semua fitur kecuali memberikan/mempublish informasi dan menghapus feedback / review dari user lain, dan menghapus forum)
- Admin (Pengguna yang mempunyai akses ke semua fitur seperti : dapat  memberikan/mempublish informasi dan menghapus feedback / review dari user lain, dan menghapus forum)
>>>>>>> 94a170257182648d599ab916cf9b7dbbb8bec8d9

