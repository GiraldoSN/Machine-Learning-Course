"""
Perulangan
Dalam kehidupan sehari-hari, sering kali kita menemui situasi yang harus dilakukan berulang kali. Misalnya dalam skenario berikut. 

"Setiap hari Rabu, pasar yang selalu dikunjungi oleh Ibu (pasar yang sama dengan cerita sebelumnya) selalu tidak menyediakan daging ayam. Maka dari itu, Ibu selalu membeli tempe sebagai gantinya.  Pada minggu biasa, Ibu hanya akan memotong 3 balok tempe karena jumlah anggota keluarga adalah 3 orang. Namun, pada minggu lain, Ibu kedatangan keluarga besar untuk makan bersama. Kali ini, Ibu tidak mengetahui total keluarga yang datang. Jadi, setelah memotong 1 balok tempe, Ibu akan selalu mengecek bahwa jumlah tersebut cukup atau tidak."

Pada skenario berikut, Ibu kedatangan keluarga besar di rumahnya dan berencana untuk membuat hidangan makanan berupa tempe. Ibu tidak mengetahui jumlah keluarga yang hadir sehingga setiap kali ada keluarganya yang datang, Ibu akan memotong 1 balok tempe untuk disajikan kepada 1 orang.
"""

"""
Perhatikan pada diagram di atas, Ibu akan selalu melakukan aktivitas berulang untuk memotong tempe hingga kondisinya terpenuhi. Kondisi yang dimaksud adalah jumlah keluarga yang hadir sama dengan jumlah tempe yang disajikan.

Dalam pemrograman, kita juga akan sering menemui masalah serupa yang mengharuskan untuk melakukan kode berulang. Contohnya menampilkan angka 1 hingga 10.
"""

print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)

"""
Output:
1
2
3
4
5
6
7
8
9
10
"""

"""
Pada kode di atas, program menampilkan angka dari 1 hingga 10 menggunakan sintaks yang berulang. Terlihat tidak efektif, bukan? Itulah yang menjadi tujuan dari materi perulangan ini, Anda akan belajar untuk membuat kode program yang efektif dan mudah dibaca oleh programmer lain.

Dalam Python, ada beberapa sintaks atau statement untuk melakukan perulangan. 
"""

"""
For
For termasuk sintaks dalam Python yang bersifat definite iteration. Definite iteration adalah sebuah proses iterasi atau perulangan ketika jumlah pengulangannya ditentukan secara eksplisit sebelumnya.

Format dari perulangan for sebagai berikut.
"""

"""
<iterable> merupakan segala object dalam Python yang dapat diiterasi seperti list, tuple, hingga string. Ada pula <var> merupakan variabel yang akan mengambil elemen berikutnya dari <iterable> setiap kali iterasi berjalan.

Mari lihat penerapannya di bawah ini.
"""

var_list = [1,2,3,4,5,6,7,8,9,10]
for i in var_list:
    print(i)

"""
Output:
1
2
3
4
5
6
7
8
9
10
"""

"""
Kode di atas merupakan program yang bertujuan untuk menampilkan angka dari 1 hingga 10 berdasarkan variable list yang sudah diinisialisasikan sebelumnya. Perhatikan bahwa program di atas sebenarnya sama dengan program pada contoh sebelumnya. Jika contoh sebelumnya menggunakan sintaks "print()" yang berulang, program di atas menggunakan sintaks atau statement for.

Pada program di atas, kita melakukan perulangan untuk menampilkan angka dari 1 hingga 10 yang sebelumnya telah diinisialisasikan pada variabel "var_list". Setiap iterasi atau perulangan yang berjalan, "i" akan mengambil elemen dari "var_list" satu per satu. Lalu, blok kode "print(i)" akan dijalankan dengan nilai "i" adalah nilai yang sudah diambil sebelumnya.

Anda juga bisa menggunakan tipe data string sebagai object <iterable>, silakan ubah variable "var_list" di atas dengan string apa pun yang Anda inginkan. Hasilnya program akan menampilkan setiap huruf dari string tersebut.

Anda juga dapat melakukan perulangan berdasarkan panjang suatu nilai dengan menggunakan fungsi "range()".
"""

for i in range(10):
    print(i)
    
"""
Jika Anda perhatikan lebih baik, program di atas menampilkan angka dari 0 hingga 9 padahal kita menentukannya "10". Mengapa itu terjadi? Pada dasarnya, "range()" adalah fungsi bawaan dalam Python yang akan menghasilkan urutan bilangan dimulai dari indeks ke-0.

Sintaksis umum dari fungsi "range()" sebagai berikut.
"""

"""
Berikut adalah penjelasan detail terkait fungsi "range()".

"Start" merupakan nilai awal dari urutan bilangan yang bersifat opsional, jika Anda tidak memasukkannya, nilai awal akan dianggap 0. 
"Stop" merupakan nilai batas yang wajib dimasukkan. Urutan akan berhenti sebelum mencapai nilai "stop" (eksklusif). 
"Step" merupakan nilai penambahan antara setiap dua bilangan dalam urutan yang bersifat opsional. Jika nilai tersebut tidak diberikan, secara default nilai yang dimasukkan adalah 1.
Di bawah ini contoh implementasinya. 
"""

for i in range(1,10,2):
    print(i)

"""
Output:
1
3
5
7
9
"""