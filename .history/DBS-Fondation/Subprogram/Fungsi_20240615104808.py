# Fungsi dalam Matematika
"""
Fungsi dalam pemrograman sebenarnya didasari oleh konsep pemetaan (asosiasi) dan fungsi dalam matematika. Fungsi pada matematika merupakan pemetaan antara dua himpunan nilai, yaitu domain dan range. Kita bisa bayangkan fungsi sebagai sebuah mesin yang memiliki input (domain) dan output (range). Output tersebut pasti terkait dengan input bagaimana pun kondisinya.
"""

"""
Dalam Python, fungsi terbagi menjadi dua jenis.

Built-in Functions
Built-in functions atau dalam bahasa Indonesia berarti fungsi bawaan adalah kumpulan fungsi yang sudah terintegrasi dengan bahasa pemrograman Python sehingga tidak perlu mengimpor modul atau library tambahan. Fungsi bawaan ini menyediakan fungsi-fungsi inti dan dasar dari bahasa Python. Contoh dari fungsi bawaan adalah print(), len(), type(), range(), dan sebagainya.
User-defined Functions
User-defined functions atau dalam bahasa Indonesia berarti fungsi yang didefinisikan pengguna adalah jenis fungsi yang kita definisikan sendiri untuk melakukan tugas spesifik tertentu. Contoh dari user-defined functions adalah fungsi yang telah kita buat di awal materi ini tentang mencari luas persegi panjang.
"""


def mencari_luas_persegi_panjang(panjang, lebar):
    luas_persegi_panjang = panjang * lebar
    return luas_persegi_panjang


persegi_panjang_pertama = mencari_luas_persegi_panjang(5, 10)
print(persegi_panjang_pertama)

persegi_panjang_kedua = mencari_luas_persegi_panjang(4, 15)
print(persegi_panjang_kedua)

"""
Output:
50
60
"""

# Library dalam Python terdiri dari dua jenis.
# Python Standard Library
"""
 tidak perlu melakukan instalasi untuk menggunakan Python Standard Library. Contoh Python Standard Library adalah "os", "datetime", "re", dan sebagainya. Anda bisa melihat banyaknya jenis library ini pada laman website berikut.
"""

# External Library
"""
Contoh dari external library adalah TensorFlow yang merupakan library populer untuk menyelesaikan permasalahan pemelajaran mesin (machine learning). 
"""
# Fungsi -> print(), len(), mencari_luas_persegi_panjang()
# Built-in functions -> print(), len(), range()
# User-defined functions -> mencari_luas_persegi_panjang()
# Modul -> Math, dan semua file yang kita buat sendiri dengan ekstensi ".py" (main.py, var.py, dan lain sebagainya)
# Package -> NumPy, Pandas
# Library -> Matplotlib, TensorFlow, Beautiful Soup

# Membuat Fungsi
def mencari_luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

"""
Fungsi yang kita buat sebelumnya terdiri dari beberapa elemen, yakni berikut.

def digunakan sebagai pernyataan bahwa kita membuat fungsi.
"mencari_luas_persegi_panjang" merupakan nama fungsi yang kita tentukan. 
Setiap fungsi memiliki parameter bertujuan untuk menyimpan nilai yang akan digunakan oleh fungsi dalam proses eksekusinya. Dalam contoh mencari luas persegi panjang, parameter "panjang, lebar" akan menyimpan setiap input yang masuk, seperti jika Anda memasukkan panjang 5cm dan lebar 10cm.
Setiap definisi fungsi harus diakhiri dengan colon atau titik dua ":" untuk menandakan awal blok kode fungsi.
Setelah function header selesai, selanjutnya kita definisikan function body yang berisi kode untuk dieksekusi. Dalam contoh mencari luas persegi panjang, kita memasukkan rumus luas persegi di bagian ini. Hasil dari rumus tersebut disimpan dalam variabel "luas_persegi_panjang". 
Terakhir, kita menggunakan return keyword yang merupakan bagian dari return statement. Return statement bertujuan untuk mengembalikan nilai atau hasil eksekusi fungsi tersebut. Dalam contoh di atas, kita mengembalikan variabel "luas_persegi_panjang" sebagai hasil dari proses eksekusi fungsi.
"""

# Memanggil Fungsi
"""
def mencari_luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

mencari_luas_persegi_panjang(10,5)   # Ini adalah pemanggil fungsi
"""
# Maka dari itu, umumnya programmer akan menggunakan variabel untuk menyimpan hasil dari eksekusi fungsi.

def mencari_luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)
print(persegi_panjang_pertama)

"""
Output:
50
"""

# Docstring
"""
Docstring adalah akronim dari documentation string, bertujuan untuk membuat dokumentasi terhadap fungsi yang dibuat. Umumnya, dokumentasi yang dijelaskan berupa argumen, return, deskripsi fungsi, dan sebagainya.
"""

def mencari_luas_persegi_panjang(panjang,lebar):
    """
    Fungsi ini digunakan untuk menghitung luas persegi panjang.

    Args:
        panjang (int): Panjang persegi panjang.
        lebar (int): Lebar persegi panjang.

    Returns:
        int: Luas persegi panjang hasil perhitungan.
    """

    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)
print(persegi_panjang_pertama)

"""
Output:
50
"""

"""
Dokumentasi di atas memiliki tiga elemen, yakni berikut.

Deskripsi: Teks yang menjelaskan tujuan dari fungsi yang dibuat. Pada contoh di atas, kita mendefinisikan teks "Fungsi ini digunakan untuk menghitung luas persegi panjang" yang artinya fungsi ini ditujukan untuk menghitung luas persegi panjang. 
Argumen: bagian yang menjelaskan argumen yang diterima oleh fungsi. Dalam contoh di atas, argumen yang diterima adalah panjang dan lebar dengan keduanya termasuk bilangan bulat atau bertipe data integer. 
Return: Bagian ini menjelaskan nilai yang akan dikembalikan oleh fungsi. Dalam contoh di atas, fungsi akan mengembalikan nilai luas persegi panjang hasil perhitungan yang termasuk bilangan bulat atau bertipe data integer.
"""

"""
Argumen
Argumen adalah nilai yang akan diberikan kepada fungsi. Setidaknya ada dua jenis argumen yang dikenal dalam Python.
"""

"""
Keyword Argument adalah jenis argumen yang disertai dengan nama parameter (identifier) dan secara eksplisit disebutkan. Ketika nama parameter dalam sebuah argumen secara langsung disebutkan, artinya kita menggunakan keyword argument.
"""
def mencari_luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(panjang=5, lebar=10)

print(persegi_panjang_pertama)

"""
Output:
50
"""
# Kelebihan dari jenis argumen ini adalah walaupun kita harus menuliskan lebih banyak kata, urutan parameter fungsi tidak perlu dipikirkan.
def mencari_luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(lebar=10, panjang=5)

print(persegi_panjang_pertama)

"""
Output:
50
"""

"""
Positional Argument
Kebalikan dari keyword adalah positional, artinya Anda tidak menyebutkan nama parameter (identifier) secara eksplisit. Ketika memanggil fungsi, Anda hanya harus memasukkan nilai yang ingin diberikan. Namun, Anda harus mengikuti urutan dari parameter fungsi tersebut.
"""
def mencari_luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)

print(persegi_panjang_pertama)

"""
Output:
50
"""

"""
Parameter
Menurut dokumentasi resmi Python, ada 5 jenis parameter yang bisa kita atur.
"""

"""
Positional-or-Keyword
Jenis ini merupakan parameter default dalam Python. Dengan jenis ini, kita dapat menggunakan positional maupun keyword argument ketika memanggil fungsi.
"""

def greeting(nama, pesan):
    return "Halo, " + nama + "! " + pesan

print(greeting("Dicoding", "Selamat pagi!"))
print(greeting(pesan="Selamat sore!", nama="Dicoding"))

"""
Output:
Halo, Dicoding! Selamat pagi!
Halo, Dicoding! Selamat sore!
"""


"""
Positional-Only
Parameter ini hanya dapat dimanfaatkan dengan menggunakan jenis argumen posisi saat pemanggilan fungsi. Parameter ini ditentukan menggunakan sintaks "/".
"""

def penjumlahan(a, b, /):
    return a + b

print(penjumlahan(8, 50))

"""
Output:
58
"""

"""
Jenis ketiga adalah kebalikan dari yang sebelumnya. Kita harus menggunakan keyword argument untuk memanggil fungsi dengan jenis parameter ini. Ia ditentukan dengan sintaks "*" (asterisk).
"""

def greeting(*, nama, pesan):
    return "Halo, " + nama + "! " + pesan

print(greeting(pesan="Selamat sore!",nama="Dicoding"))

"""
Output:
Halo, Dicoding! Selamat sore!
"""

"""
Var-Positional (Variadic Positional Parameter)
Parameter ini menampung jumlah argumen posisi yang bervariasi saat pemanggilan fungsi. Parameter ini ditentukan dengan menggunakan sintaks *args.
"""

def hitung_total(*args):
    print(type(args))
    total = sum(args)
    return total

print(hitung_total(1, 2, 3))

"""
Output:
<class 'tuple'>
6
"""

"""
Var-Keyword (Variadic Keyword Parameter)
Parameter ini dapat menampung jumlah keyword argument yang bervariasi saat pemanggilan fungsi. Parameter ini ditentukan dengan menggunakan sintaks **kwargs yang berperan sebagai dictionary (seperti tipe datanya). Argumen pada pemanggil fungsi akan berperan sebagai value dan parameter (identifier) berperan sebagai key.
"""

def cetak_info(**kwargs):
    info = ""
    for key, value in kwargs.items():
        info += key + ': ' + value + ", "
    return info

print(cetak_info(nama="Dicoding", usia="17", pekerjaan="Python Programmer"))
"""
Output:
nama: Dicoding, usia: 17, pekerjaan: Python Programmer,
"""

# Fungsi Anonim (Lambda Expression)

mencari_luas_persegi_panjang = lambda panjang, lebar: panjang*lebar
print(mencari_luas_persegi_panjang(5,10))

"""
Output:
50
"""

# Variabel Global dan Lokal
# Variabel Global dan Lokal
a = 10

def add(b):
    result = a+b
    return result

bilanganPertama = add(20)
print(bilanganPertama)

"""
Output:
30
"""


# Variabel Lokal
def add(a, b):
    lokal_var = 5
    result = a+b-lokal_var
    return result

bilanganPertama = add(10,20)
print(bilanganPertama)

"""
Output:
25
"""


# enulis Modul pada Python

