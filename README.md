# :books: LiteraLand

## :busts_in_silhouette: Nama Anggota :busts_in_silhouette:
- Caesar Syahru Ramadhan
- M. Alif Al Hakim
- Farrel Muhammad Hanau
- Michelle Angelica Santoso
- Salma Nurul ‘Aziz

## :book: Cerita Aplikasi dan Manfaatnya :book:
Nama Aplikasi : LiteraLand

Dalam era digital saat ini, membaca buku tetap menjadi salah satu kegiatan yang paling digemari banyak orang. Namun, dengan begitu banyaknya koleksi buku yang ada, seringkali pembaca kesulitan dalam mengingat halaman terakhir yang mereka baca, serta berdiskusi dan menyimpan buku favorit. Oleh karena itu, dibutuhkan sebuah aplikasi yang mampu menyediakan solusi untuk permasalahan tersebut.

LiteraLand adalah aplikasi koleksi buku berbasis web yang memungkinkan pengguna untuk membaca buku pada halaman web. Aplikasi ini menyediakan fitur yang dapat mendukung kegiatan membaca pengguna seperti sistem pencarian dan koleksi buku, pembatas buku, serta forum diskusi/review. Selain itu, aplikasi ini juga memungkinkan untuk membuat ranking buku sesuai personalisasi masing-masing.

## :file_folder: Daftar Modul yang Akan Diimplementasikan :file_folder:

### :mag_right: Modul Browse Buku :mag_right:
Pada modul ini akan ditampilkan semua buku yang terdapat di database projek. Selain itu, pada modul ini `user` dapat mengirimkan permintaan untuk menambahkan buku di database sehingga mereka dapat menambahkan buku tersebut ke koleksi.

### :bookmark: Modul Koleksi Buku :bookmark:
Pada modul ini `user` dapat menambahkan semua buku yang ingin mereka tambahkan ke daftar koleksi. `User` dapat menambahkan buku dengan meng-click buku pada halaman browse buku lalu menambahkannya ke daftar koleksi dengan menekan tombol `Add to Collections`. Pada modul ini `user` dapat menyimpan progres baca, status baca, dan rating dari buku yang ada pada daftar koleksi mereka. Selain itu, mereka dapat membaca buku yang ada dalam daftar koleksi mereka.

### :star: Model Ranking :star:
Pada modul ini setiap `user` dapat memposting daftar buku favorite menurut pendapat mereka. Selain itu, pada modul ini `user` juga dapat melihat list buku favorite dari user lain sehingga dapat menjadi referensi untuk membaca buku lain.

### :page_with_curl: Model Review Buku :page_with_curl:
Pada modul ini setiap `user` dapat memposting review mengenai suatu buku. `User` dapat memberikan komentar atau pendapat dan rating dari 1 sampai 5 untuk buku yang mereka review. `User` juga dapat melihat review dari `user lain` mengenai buku tersebut sehingga dapat menjadi referensi dalam memilih buku.

### :gem: Modul Admin :gem:
Pada modul ini `admin` akan menerima pesan request yang telah dikirimkan `user` pada modul `Browse Buku`. `Admin` dapat menambahkan buku yang telah di-request oleh `user` ke database projek sehingga semua `user` dapat menambahkan buku ke daftar koleksi, melakukan review terhadap buku tersebut, atau memasukkannya ke list rekomendasi buku.


## :information_source: Sumber dataset katalog buku :information_source:
- Google Book Dataset (https://www.kaggle.com/datasets/bilalyussef/google-books-dataset) - Berisi informasi mengenai judul, penulis, bahasa, kategori, rating umur, publisher, tanggal terbit, jumlah halaman, deskripsi, dan ISBN dari buku.
- Google Book API (https://developers.google.com/books/) - Berguna untuk menampilkan konten buku dari Google Books secara langsung di halaman web. 


## :computer: Role atau peran user :computer:
### Guest
- Pengguna yang belum memiliki akun atau belom login ke website
- User Guest bisa mengakses halaman browse buku untuk melihat daftar buku yang ada pada database
- User Guest juga bisa mengakses halaman detail buku setelah meng-klik judul buku pada halaman browse buku
- User Guest juga bisa mengakses halaman rankingBuku untuk melihat list-list buku dari user lain (Guest tidak bisa menambahkan list buku sendiri)

### User
- Pengguna yang sudah memilki akun dan sudah login ke website
- User bisa mengakses fitur Koleksi buku 
- User bisa membaca buku yang terdapat dalam daftar koleksi
- User bisa mengakses halaman rankingBuku dan mempost list buku favorite-nya
-User bisa melakukan permintaan/request pada halaman browse buku untuk menambahkan buku baru ke database
- User bisa mengakses halaman review buku dan memposting review buku sendiri

### Admin
- Pengguna yang memiiki seluruh `hak akses` dari `user` dan hak akses khusus
- Admin dapat menerima pesan request buku dari user.
- Admin dapat menambahkan buku berdasarkan request user ke database 