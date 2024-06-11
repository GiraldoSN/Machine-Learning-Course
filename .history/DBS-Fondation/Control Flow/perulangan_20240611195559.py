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

"""
Pada program di atas, kita menampilkan bilangan ganjil yang dimulai dari 1 hingga 10. Perhatikan bahwa program di atas mendefinisikan nilai "1" sebagai "start", nilai "10" sebagai "stop", dan nilai "2" sebagai "step". Ingat bahwa "stop" bersifat eksklusif, yang artinya nilai terakhirnya tidak akan disertakan. 

Dengan begitu, program di atas akan menampilkan kode dari 1 hingga 10 dengan setiap bilangan ke-2 dan kelipatannya akan dilewati atau tidak dicetak.
"""

"""
While
While termasuk sintaks dalam Python yang bersifat indefinite iteration. Indefinite iteration adalah sebuah proses iterasi yang akan berhenti ketika memenuhi kondisi tertentu.

Format dari perulangan while sebagai berikut.
"""

"""
Kondisi merupakan ekspresi yang akan dievaluasi dan menghasilkan nilai true atau false. Selama hasil evaluasi bernilai true, program akan terus berjalan hingga menghasilkan nilai false.

Berikut implementasinya.
"""

counter = 1
while counter <= 5:
    print(counter)
    counter += 1
    
"""
Pada contoh di atas, kita menggunakan perulangan "while" untuk menampilkan angka 1 hingga 5. Variabel "counter" diinisialisasi dengan nilai 1 sebelum perulangan dimulai. Ini artinya perulangan akan dimulai dari 1 berdasarkan nilai variabel tersebut. Perulangan lalu berjalan dengan mengevaluasi variabel "counter" yang memiliki nilai "1". Hasil dari evaluasi tersebut bernilai true sehingga blok kode di dalamnya akan dijalankan.

Perhatikan bahwa kita menggunakan jenis ekspresi uner untuk melakukan increment. Increment adalah pola untuk menambahkan suatu variabel dengan nilai tetap. Dengan hal ini, setiap perulangan bernilai true maka variabel "counter" akan terus ditambah dengan nilai "1". Pada perulangan di atas, nilai variabel "counter" akan bertambah hingga nilainya adalah "5". Ketika nilai variabel "counter" menyentuh "5" maka hasil evaluasi akan bertambah menjadi "6", tetapi angka 6 tersebut tidak memenuhi kondisi "<=5" sehingga kode print() tidak akan dijalankan dan hanya akan memunculkan angka hingga 5.

Namun, Anda harus berhati-hati untuk tidak melakukan infinite loop, yakni sebuah kondisi ketika perulangan tidak berhenti karena tidak memenuhi kondisi yang diinginkan. Contohnya adalah ketika melakukan perulangan, kita tidak memberikan increment yang menyebabkan variabel atau counter tidak akan memenuhi kondisi while.
"""

counter = 1
while counter <= 5:
    print(counter)
    counter += 1

"""
Pada contoh di atas, kita melakukan perulangan while, tetapi tidak melakukan increment di baris akhir kode. Hal ini menyebabkan program akan terus berjalan dan akhirnya berhenti karena run time exceeded atau waktu berjalan melebihi yang ditentukan. 

Jika Anda menjalankan kode di atas pada IDE seperti notebook, program akan terus berjalan dan harus dihentikan dengan menekan CTRL + C.
"""

"""
For Bersarang 
Ketika Anda membuat perulangan, sering kali menemukan perulangan dalam perulangan atau disebut sebagai nested loop. 

Format dari nested loop sebagai berikut.
"""

"""
Anda dapat asumsikan bahwa ada dua perulangan, yakni "perulangan luar" dan "perulangan dalam". Program akan melakukan "perulangan luar" terlebih dahulu, lalu akan melakukan "perulangan dalam". "variabel_luar" akan mengambil nilai dari "iterable_luar", sedangkan "variabel_dalam" akan mengambil nilai dari "iterable_dalam".

Mari kita lihat implementasi dari for bersarang.
"""

"""
Output dari sebelah kiri dihasilkan dari perulangan for luar, sedangkan output dari sebelah kanan dihasilkan dari perulangan for dalam. Perhatikan lebih detail bahwa "perulangan luar" atau outer loop akan dilanjutkan jika "perulangan dalam" atau inner loop telah selesai. Semua perulangan tersebut dilakukan hingga kedua perulangan menghasilkan false dan berhenti.
"""

"""
Kontrol Perulangan
Selain membuat perulangan, kita juga dapat mengontrol perulangan dengan menggunakan beberapa pernyataan di antaranya sebagai berikut.

Break
Break statement adalah pernyataan untuk menghentikan perulangan dan kemudian program akan otomatis keluar dari perulangan tersebut, lalu dilanjutkan dengan mengeksekusi blok perulangan selanjutnya. Jika Anda memiliki perulangan yang bertingkat seperti for bersarang, break akan menghentikan perulangan sesuai dengan tingkatan atau letak perulangannya berada.
"""

for i in range(2):  # Perulangan tingkat pertama
    print("Perulangan luar:", i)
    for j in range(10):  # Perulangan tingkat kedua
        print("Perulangan dalam:", j)
        if j == 1:
            break  # Menghentikan perulangan dalam jika j = 1


"""
Output:
Perulangan luar: 0
Perulangan dalam: 0
Perulangan dalam: 1
Perulangan luar: 1
Perulangan dalam: 0
Perulangan dalam: 1
"""

"""
Pada kode di atas, kita melakukan perulangan untuk menampilkan bilangan 0 hingga 1 pada "perulangan luar" atau for pertama. Lalu, kita membuat perulangan kedua untuk menampilkan bilangan dari 0 hingga 9. Namun, pada perulangan kedua atau "perulangan dalam" tersebut, kita akan melakukan break jika bertemu angka "1". Alhasil, perulangan dalam hanya akan menampilkan angka hingga 1 saja. Program akan berhenti karena ada statement break yang diberikan jika bertemu angka "1".

Contoh lainnya sebagai berikut.
"""

for huruf in 'Dico ding':
    if huruf == ' ':
        continue
    print('Huruf saat ini: {}'.format(huruf))

"""
Output:
Huruf saat ini: D
Huruf saat ini: i
Huruf saat ini: c
Huruf saat ini: o
Huruf saat ini: d   # Perhatikan bahwa harusnya sebelum ini ada spasi, namun dilewati.
Huruf saat ini: i
Huruf saat ini: n
Huruf saat ini: g
"""

"""
Pada contoh di atas, kita membuat perulangan yang sama dengan contoh sebelumnya. Namun, alih-alih ada spasi maka program akan berhenti, program akan mengabaikan spasi tersebut dan melanjutkannya pada perulangan selanjutnya.

Dalam contoh di atas, program berusaha untuk menampilkan teks "Dico ding" dengan kondisi jika bertemu " " (spasi) akan dilewati dan melakukan perulangan selanjutnya. Alhasil output yang dihasilkan adalah "d", "i", "c", "o", "d", "i", "n", "g" tanpa adanya spasi.
"""

"""
Else setelah For
Pada Python juga dikenal else setelah for yang berfungsi untuk perulangan bersifat pencarian. Else setelah for ini bisa dikatakan sebagai memberikan jalan keluar program saat pencarian tidak ditemukan.
"""

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 4:
        print("Angka ditemukan! Program berhenti!")
        break
else:
    print("Angka tidak ditemukan.")

"""
Output:
Angka tidak ditemukan.
"""

"""
Pada contoh di atas, kita membuat program untuk melakukan pencarian terhadap bilangan 6. Jika bilangan 6 tersebut merupakan elemen atau nilai yang berada list, program akan berhenti dan menampilkan teks "Angka ditemukan! Program berhenti!".

Namun, pada contoh di atas angka 6 bukan merupakan elemen dari list maka program akan menampilkan teks "Angka tidak ditemukan". Apa jadinya jika program menemukan angka? Silakan ganti "if num == 6" dengan "if num == 4" atau angka lain yang merupakan nilai yang berada dalam list.

Perlu diperhatikan oleh Anda, if dan else pada contoh tersebut berkaitan walaupun berbeda blok. Pada else setelah for, statement else tidak akan dieksekusi saat if pernah sekali saja benar. Dengan kata lain, break dalam if harus tidak terjadi untuk memicu else setelah for.
"""

"""
Else setelah While
Berbeda dengan else setelah for, pada statement else setelah while, blok statement else akan selalu dieksekusi saat kondisi pada while menjadi salah. 
"""

count = 0

while count < 3:
    print("Dicoding Indonesia")
    count += 1
else:
    print("Blok else dieksekusi karena kondisi pada while salah (3<3 == False).")


"""
Output:
Dicoding Indonesia
Dicoding Indonesia
Dicoding Indonesia
Blok else dieksekusi karena kondisi pada while salah (3<3 == False).
"""

"""
Pada contoh di atas, perulangan while akan terus terjadi dan else tidak akan dieksekusi jika kondisi while benar. Kondisi while akan terus benar pada kode di atas ketika variabel "count" bertambah dari 1 hingga 2 dan akan berhenti ketika variabel "count" bernilai 3 karena "3<3" adalah false atau salah.
"""

# Di sisi lain, jika menggunakan break akan seperti berikut.

n = 10
while n > 0:
    n = n - 1
    if n == 7:
        break
    print(n)
else:
    print("Loop selesai")

"""
Output:
9
8
"""

