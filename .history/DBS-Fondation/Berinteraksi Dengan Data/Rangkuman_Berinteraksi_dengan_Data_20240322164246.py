# Abstraksi Data Abstraksi data merupakan kemampuan Anda untuk mengerti konteks dan merepresentasikannya menjadi bentuk lain sesuai dengan konteks masalahnya.

# Data Typing
# Deklarasi dan Inisialisasi
age = 17
salary = 5000000.0

print(type(age))
print(type(salary))

"""
Output:
<class 'int'>
<class 'float'>
 
"""

# Tipe Data dikelompokkan menjadi tipe data primitif dan tipe data collection.
# Tipe Data Primitif Tipe data primitif merupakan jenis data yang paling dasar dalam pemrograman. Tipe data ini menyimpan single value. Beberapa tipe data primitif sebagai berikut.
# 1. Numbers
# a. Integer: Bilangan bulat positif atau negatif dan tidak memiliki angka desimal. Contoh: 1; -20; 999; dan 0.
# b. Float: Bilangan riil yang dapat mewakili bilangan bulat atau bilangan desimal. Contoh: 3.14; 1; dan 4.01E+1
# c. Complex: Bilangan kompleks. (Kita tidak akan menggunakannya di kelas ini.) Contoh: 1+2j

# 2. Boolean merupakan tipe data yang hanya bernilai TRUE atau FALSE. Tipe data ini merepresentasikan nilai kebenaran (truth values).
# Sebenarnya, setiap variabel yang memiliki nilai bisa dievaluasi dan menghasilkan nilai true. Hanya ada beberapa nilai yang akan dianggap bernilai false, yakni berikut.
# Hannya ada beberapa nilai yang akan dianggap bernilai false, yakni berikut.
Nilai yang sudah didefinisikan bernilai salah: None dan False.
Angka nol dari semua tipe numerik: 0, 0.0, 0j, Decimal(0), Fraction(0,1).
Urutan (sequence) dan koleksi (collection) yang kosong: "", (), {}, set(), range(0).
