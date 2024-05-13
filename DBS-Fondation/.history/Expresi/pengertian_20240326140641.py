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