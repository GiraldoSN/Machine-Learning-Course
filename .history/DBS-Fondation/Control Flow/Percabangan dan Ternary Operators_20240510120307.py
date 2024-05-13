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

"""