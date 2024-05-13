# Struktur umum ekspresi yang sering dijumpai adalah <operan1> <operator> <operan2>. Namun, perlu Anda ketahui bahwa struktur umum tersebut merupakan struktur ekspresi biner (jenis ekspresi menggunakan dua operan).

# Operan dapat berupa nilai, variabel, konstanta, atau ekspresi lain.
# Operator merupakan suatu fungsi standar yang disediakan dalam bahasa pemrograman untuk melakukan beberapa hal dasar, seperti perhitungan aritmetika, logika, dan relasional. Contohnya adalah penjumlahan (+), pengurangan (-), perkalian (*), modulus (%), dan sebagainya.

x = 10
y = 2
result = x - y

print(result)

"""
Output:
8
"""

# Salah satunya adalah melakukan penggabungan dan replikasi pada list.
angka = [2, 4, 6, 8]
huruf = ["P", "Y", "T", "H", "O", "N"]
gabung = angka + huruf

print(gabung)

"""
Output:
[2, 4, 6, 8, 'P', 'Y', 'T', 'H', 'O', 'N']
"""

# Pada kode di atas, Anda menggabungkan dua list dengan menggunakan operator penjumlahan (+).
# Namun, pada kode di bawah ini, Anda mereplikasi list dengan menggunakan operator perkalian (*).

learn = ["P", "Y", "T", "H", "O", "N"]
replikasi = learn * 2

print(replikasi)

"""
Output:
['P', 'Y', 'T', 'H', 'O', 'N', 'P', 'Y', 'T', 'H', 'O', 'N']
"""

# Jenis-Jenis Ekspresi
# Biner, Contohnya (x + y), (x - y), (x * y), (x / y), (x ** y), (x < y), (x <= y), (x > y), (x >= y), (x % y), (x == y), (x != y).

# Uner, contohnya (x += 1), (x-=1), (not x).

# Ekspresi biner merupakan jenis yang memiliki dua operan. Operatornya meliputi penjumlahan (+), pengurangan (-), perkalian (*), pembagian (/), perpangkatan (**), lebih kecil dari (<), lebih kecil dari sama dengan (<=), lebih besar dari (>), lebih besar dari sama dengan (>=), modulus (%), sama dengan (==), dan tidak sama dengan (!=).

# Namun, ekspresi uner adalah jenis ekspresi yang memiliki bentuk dasar operasi dengan satu operan. Contohnya adalah increment (x+=1), decrement (x-=1), dan negasi (not x).

a = True
a = not a
print(a)

b = 6
b -= 1
print(b)

c = 6
c += 1
print(c)

d = 10
print(-d)

"""
Output:
False
5
7
-10
"""

# 1. Variabel a bernilai True, jika kita memberikan ekspresi "not a" yang artinya "not True", hasil yang didapat adalah False.
# 2. Baik increment maupun decrement, keduanya adalah pola yang sama untuk menambahkan dan mengurangi suatu variabel dengan jumlah tetap.
# a += 1 memiliki tujuan yang sama dengan struktur a = a + 1. Jika diasumsikan variabel a bernilai 1, seolah-olah kita melakukan operasi penjumlahan "1+1". Inilah alasan ia disebut dengan increment yang artinya kenaikan.
# Decrement dapat dijelaskan sebagai a -=1, memiliki tujuan yang sama dengan struktur a = a - 1. Jika diasumsikan variabel a bernilai 1, seolah-olah kita melakukan operasi pengurangan "1-1".

# Ekspresi Menurut Tipe Data yang Dihasilkan;
# Jenis Ekspresi aritmetika: <numerik> <operator> <numerik> = <numerik>; Contohnya: 2 + 2 = 4, 2 - 2 = 0
# Ekspresi relasional:
# <numerik> <operator> <numerik> = <boolean>
# contohnya: 3 < 10 = True, 1 > 10 = False
# Ekspresi logika: <boolean> <operator> <boolean> = <boolean>; contohnya: True or False = True
