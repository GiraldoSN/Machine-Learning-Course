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

"