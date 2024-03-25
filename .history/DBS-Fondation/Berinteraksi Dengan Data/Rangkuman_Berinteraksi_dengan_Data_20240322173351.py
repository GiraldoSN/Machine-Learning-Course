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
# Hannya ada beberapa nilai yang akan dianggap bernilai false, yakni berikut:
# a. Nilai yang sudah didefinisikan bernilai salah: None dan False.
# b. Angka nol dari semua tipe numerik: 0, 0.0, 0j, Decimal(0), Fraction(0,1).
# c. Urutan (sequence) dan koleksi (collection) yang kosong: "", (), {}, set(), range(0).

# 3. String merupakan karakter yang berurutan. Ketika Anda membuat variable bernilai string maka akan diawali dengan single quote ('') atau double quote("").
# "Dicoding Indonesia"


# Tipe Data Collection
# Selain tipe data primitif yang menyimpan single value, ada tipe data lain, yakni tipe data collection. Tipe data ini menyimpan satu atau lebih data primitif sebagai satu kelompok. Berikut adalah tipe data yang masuk ke dalam tipe data collection.
# 1. List
# List merupakan jenis kumpulan data terurut (ordered sequence) dan salah satu tipe data yang sering digunakan pada Python.

# Melakukan inisialisasi list pada Python cukup mudah: menggunakan kurung siku "[]" dan setiap elemennya dipisahkan dengan koma.
# x = [1, 2.2, "Dicoding"] Perlu diingat bahwa nilai yang ada dalam sebuah list selalu dimulai dari indeks ke-0. Artinya, nilai "1" pada list di atas merupakan indeks ke-0.

# 2. Tuple merupakan jenis dari list yang tidak dapat diubah elemennya. Umumnya, tuple digunakan untuk data yang bersifat sekali deklarasi dan dapat dieksekusi lebih cepat. Anda dapat mendeklerasikan tuple dengan menggunakan tanda kurung "()" dan setiap elemen di dalamnya dipisahkan dengan koma.
# x = (1, "Dicoding", 1+3j)

# 3. Set merupakan kumpulan item bersifat unik dan tanpa urutan (unordered collection). Anda dapat melakukan inisialisasi variabel set dengan menggunakan tanda kurawal "{}" dan setiap elemennya dipisahkan dengan koma.
# x = {1, 2, 3 , 7, 13}

# 4. dictionary pada Python merupakan kumpulan pasangan key-value yang bersifat tidak berurutan. Dictionary dapat digunakan untuk menyimpan data kecil hingga besar. Pada Python, dictionary didefinisikan dengan kurawal dan tambahan definisi berikut:
# a. Setiap elemen pasangan key-value dipisahkan dengan koma (,).
# b. Key dan value dipisahkan dengan titik dua (:).
# c. Key dan value dapat berupa tipe variabel/objek apa pun.
# x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }

# Konversi antara Tipe Data
# 1. Konversi integer ke float: float().
# 2. Konversi float ke integer: int().
# 3. Konversi dari-dan-ke string: str(), float(), int().

# Transformasi Angka, Karakter, dan String
# 1. Mengubah Huruf Besar/Kecil
# a. upper()
# b. lower()

# 2. Awalan dan Akhiran
# Menghapus karakter whitespace pada suatu string.
# a. rstrip()
# b. lstrip()
# c. strip()
# d. startswith()
# e. endswith()

# Memisah dan Menggabung String

