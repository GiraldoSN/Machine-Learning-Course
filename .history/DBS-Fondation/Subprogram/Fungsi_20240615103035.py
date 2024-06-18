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
