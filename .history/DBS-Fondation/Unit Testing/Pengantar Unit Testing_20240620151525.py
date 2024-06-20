"""
Tidak hanya sekadar manual dan otomatis, dalam dunia testing yang begitu luas, Anda akan menemui berbagai jenis testing. Beberapa di antaranya adalah unit testing dan integration testing.
"""


"""
Integration testing adalah pengujian yang bertujuan untuk menguji suatu sistem sebagai satu kesatuan. Bayangkan Anda sedang mengecek lampu motor, tentu hal pertama yang dilakukan adalah menyalakan motor. Lalu, Anda melihat lampu motor tersebut yang sempat menyala, tetapi perlahan mati. Anda kemudian bertanya, mengapa lampunya mati?

Kejadian yang dijelaskan di atas erat dengan konsep integration testing karena dengan menyalakan motor, kita dapat menguji seluruh bagian motor lain, seperti lampunya.
"""


"""
Unit testing adalah pengujian yang lebih spesifik dan fokus terhadap bagian-bagian kecil. Bayangkan ketika mengecek lampu motor dan ternyata ia tidak menyala, Anda perlu mengecek lampu tersebut; apakah rusak? Atau ada kabel dari lampu tersebut yang tidak berfungsi? Hal-hal yang lebih spesifik tersebut adalah unit testing. Dalam pemrograman, bagian-bagian kecil tersebut berupa fungsi, kelas, dan sebagainya.

Pada materi ini, kita akan mempelajari unit testing menggunakan salah satu library bawaan Python, yaitu unittest. Unit test adalah proses pengujian perangkat lunak yang memastikan setiap unit/fungsi dari program teruji. Jika fungsionalitas dari aplikasi yang kita bangun terdiri dari prosedur-prosedur dan fungsi-fungsi yang kita tulis, kita perlu melakukan unit test untuk setiap prosedur atau fungsi yang ada.

Layaknya sebuah framework pengujian, library unittest mendukung beberapa hal esensial berikut.

Pengujian secara otomatis.
Kode awal proses (setup) dan akhir proses (shutdown) yang dapat digunakan ulang.
Penyatuan sejumlah pengujian dalam sebuah koleksi.
Terpisahnya framework pengujian dari framework pelaporan (reporting).
Library unittest mendukung sejumlah konsep penting yang berorientasi objek, antara lain berikut.

Test fixture merepresentasikan persiapan yang dibutuhkan untuk melakukan satu pengujian atau lebih serta proses pembersihannya (cleanup). Beberapa contohnya adalah menyiapkan basis data pengujian, direktori pengujian, atau mengaktifkan sebuah proses server.
Test case adalah sebuah unit dari pengujian ketika ia mengecek sejumlah respons dari sebagian kelompok masukan. Library unittest menyediakan basis class dan TestCase yang akan digunakan untuk membuat kasus pengujian baru.
Test suite adalah sebuah koleksi dari kasus-kasus pengujian, koleksi dari test suite itu sendiri, atau gabungan keduanya. Hal ini berguna untuk mengumpulkan pengujian-pengujian yang akan dieksekusi bersama.
Test runner adalah komponen yang akan mengatur (orchestrates) eksekusi dari pengujian-pengujian dan menyediakan keluaran untuk pengguna. Dalam hal ini, runner dapat menggunakan tampilan grafis, tampilan tekstual, atau mengembalikan nilai spesial yang menyatakan hasil dari pengujian.
"""

