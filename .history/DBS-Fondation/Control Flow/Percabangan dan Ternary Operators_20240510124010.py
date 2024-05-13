"""

Control flow adalah sebuah cara untuk memberi tahu program mengenai instruksi yang harus dijalankan dan di mana harus memulai dan berakhir. Pada materi sebelumnya, Anda telah mempelajari aksi sekuensial. Python akan menjalankan kode Anda berdasarkan deretan instruksi yang dibuat secara sekuensial.

Dalam Python, program dapat berupa blok kode. Python sangat memperhatikan indentasi untuk membangun sebuah blok kode. Salah satu blok pemrograman adalah perulangan. Perulangan adalah satu dari beberapa control flow. 

Control flow memungkinkan program untuk berjalan berdasarkan jalur eksekusi. Control flow terbagi menjadi beberapa jenis, yakni kondisi tertentu (percabangan), mengulang blok kode secara berulang (perulangan), melewati sebagian kode dan berhenti di kode tertentu, hingga mendefinisikan fungsi. 

Kita akan mempelajari fungsi pada modul yang berbeda. Untuk menggantikannya, materi ini akan fokus menjelaskan error dan exception handling yang bertujuan untuk mengontrol dan merespons kejadian yang tidak diinginkan ketika program berjalan.

Mari kita mulai pembahasan kita dari Percabangan dan Ternary Operators terlebih dahulu.


"""

"""
Percabangan
Dalam pemrograman, sebuah kode program dapat berjalan berdasarkan kondisi tertentu. Maknanya, Anda dapat memberikan instruksi berdasarkan "Jika-maka" (if-else). 

Misalnya dalam keadaan seperti berikut.

Jika Anda tidak menyelesaikan kelas Memulai Pemrograman dengan Python, maka Anda tidak lulus dari kelas Memulai Pemrograman dengan Python.
Jika jumlah variabel nama kurang dari dua, maka variabel tersebut tidak memenuhi kriteria kondisi.
Sebenarnya, kasus percabangan sering kita jumpai dalam kehidupan sehari-hari. Simak ilustrasi berikut.

"Setiap hari, Ibu selalu pergi ke pasar untuk membeli bahan makanan. Ibu selalu mengutamakan untuk membeli daging ayam di pasar. Jika daging ayam tidak tersedia, maka Ibu akan membeli tempe sebagai pengganti, lalu memasaknya."

"""


ketersediaan = "Daging ayam"

if ketersediaan == "Daging ayam":
    print("Ibu membeli dan memasak ayam")
else:
    print("Ibu membeli dan memasak tempe")

"""
Output:
Ibu membeli dan memasak ayam
"""

"""
Kode di atas merupakan program percabangan. Jika variabel "ketersediaan" bernilai "Daging ayam", maka akan mengembalikan string "Ibu membeli dan memasak ayam". Kita bisa asumsikan variabel "ketersediaan" sama seperti ketersediaan bahan makanan dari pasar yang ibu kunjungi. Jika pasar tersebut menyediakan "Daging ayam", variabel tersebut bernilai "Daging ayam".
"""


"""
Jika daging ayam tidak tersedia di pasar, maknanya variabel "ketersediaan" akan bernilai kosong atau bernilai bahan makanan lain. Dengan begitu, jika variabel "ketersediaan" tidak memiliki nilai "Daging ayam", variabel ketersediaan tidak lagi memenuhi kondisi "if ketersediaan == 'Daging ayam'". Jadi, program akan mengembalikan teks atau string "Ibu membeli dan memasak tempe".

Ingat bahwa Python adalah bahasa pemrograman case-sensitive, hal ini berlaku juga pada percabangan. Buktikan sendiri dengan mengubah "Daging ayam" menjadi "Daging Ayam". Apakah output program masih sama?

Dalam ilustrasi di atas, kita paham bahwa percabangan melibatkan if dan else statement. Anda dapat mengasumsikan statement sebagai instruksi. Selain if dan else statement, sebenarnya Python masih memiliki satu statement lagi yang sering digunakan, yakni elif. Mari kita pelajari satu per satu.
"""

"""
If
If adalah statement Python yang akan mengecek nilai variabel di dalamnya memenuhi kriteria suatu kondisi atau tidak. Jika memenuhi kriteria, kondisi tersebut bernilai true. Jika tidak memenuhi kriteria, kondisi akan bernilai false. Jika kondisi if bernilai true, kode yang berada dalam blok kode if akan dieksekusi.
"""

"""
Perlu diingat bahwa if merupakan blok kode. Jadi, Anda perlu memperhatikan indentasi untuk menjalankan kode, seperti yang ditunjukkan gambar.

Mari tinjau implementasi if pada kode di bawah ini.
"""

score = 100

if score == 100:
    print("Nilai Anda sempurna!")

"""
Output:
Nilai Anda sempurna!
"""

"""
Pada kode di atas, program akan mengecek nilai dari variabel "score". Kondisi yang harus terpenuhi adalah "if score == 100" atau bisa diartikan nilai dari variabel "score" harus bernilai "100". Program lalu mengecek variabel dan mengevaluasi nilainya berdasarkan kondisi yang harus dipenuhi. 

Pada kode di atas, kondisi terpenuhi dan program akan menjalankan kode yang berada dalam if statement. Kode tersebut merupakan fungsi "print()" untuk menampilkan teks atau string "Nilai Anda sempurna!".

Hal lain yang perlu diperhatikan adalah Python menganggap setiap nilai kosong (zero) dan null sebagai False. Sebaliknya, nilai yang tidak kosong (non-zero) dan tidak null (non-null) akan bernilai True. Untuk lebih mengetahui maksudnya, mari lihat kode berikut. 
"""

"""
Pada baris pertama kode program di atas, variabel "x" diinisialisasikan dengan string kosong "". Kemudian if statement mengevaluasi variabel "x" dan menghasilkan nilai salah (False). Hal ini terjadi karena variabel "x" berisi string kosong dan Python mengevaluasinya sebagai False. Sebab hasil kondisinya adalah False, blok kode dalam if tidak dijalankan.

Beberapa nilai yang dianggap sebagai false oleh Python sebagai berikut.

Nilai yang sudah didefinisikan bernilai salah: None dan False.
Angka nol dari semua tipe numerik: 0, 0.0, 0j, Decimal(0), Fraction(0,1).
Urutan (sequence) dan koleksi (collection) yang kosong: "", (), {}, set(), range(0).
Selain nilai di atas, Python akan menganggap semua nilai sebagai true.

Terakhir, if statement memiliki versi one-liner-nya. Ini memungkinkan Anda untuk membuat kode if dalam bentuk single statement atau satu baris, tanpa perlu memperhatikan indentasi dan membuat blok kode.
"""

score = 100

if score == 100: print("Nilai Anda sempurna!")

"""
Output:
Nilai Anda sempurna!
"""

