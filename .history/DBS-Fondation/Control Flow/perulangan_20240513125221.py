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