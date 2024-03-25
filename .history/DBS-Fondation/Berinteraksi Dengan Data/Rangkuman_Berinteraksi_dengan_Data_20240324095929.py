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
# Mengubah string menjadi UPPERCASE atau lowercase.
# a. upper()
# b. lower()

# Contoh mengubah string menjadi huruf besar (UPPERCASE)
string_upper = "hello, world!".upper()
print(string_upper)  # Output: HELLO, WORLD!

# Contoh mengubah string menjadi huruf kecil (lowercase)
string_lower = "HELLO, WORLD!".lower()
print(string_lower)  # Output: hello, world!


# 2. Awalan dan Akhiran
# Menghapus karakter whitespace pada suatu string.
# a. rstrip()
# b. lstrip()
# c. strip()
# d. startswith()
# e. endswith()

# Contoh penggunaan rstrip() untuk menghapus whitespace di sebelah kanan string
text1 = "    Hello, world!    "
text1_stripped = text1.rstrip()
print(text1_stripped)  # Output: "    Hello, world!"

# Contoh penggunaan lstrip() untuk menghapus whitespace di sebelah kiri string
text2 = "    Hello, world!    "
text2_stripped = text2.lstrip()
print(text2_stripped)  # Output: "Hello, world!    "

# Contoh penggunaan strip() untuk menghapus whitespace di kedua sisi string
text3 = "    Hello, world!    "
text3_stripped = text3.strip()
print(text3_stripped)  # Output: "Hello, world!"

# Metode yang digunakan untuk memeriksa apakah string dimulai dengan substring yang diberikan
text4 = "    Hello, world!    "
text4_startswith = text4.startswith("Hello")  # Mengembalikan True jika string dimulai dengan "Hello"
print(text4_startswith)  # Output: False

text4 = "    Hello, world!    "
text4_startswith = text4.startswith(" ")  # Mengembalikan True jika string dimulai dengan spasi
print(text4_startswith)  # Output: True

# Mutode yang digunakan untuk memeriksa apakah string diakhiri dengan substring yang diberikan
text5 = "    Hello, world!    "
text5_endswith = text5.endswith("world!")  # Mengembalikan True jika string diakhiri dengan "world!"
print(text5_endswith)  # Output: False

text5 = "    Hello, world!    "
text5_endswith = text5.endswith(" ")  # Mengembalikan True jika string diakhiri dengan spasi
print(text5_endswith)  # Output: True

# 3. Memisah dan Menggabung String
#Fungsi-fungsi untuk memisahkan dan menggabungkan string.
join()
split()

# 4. Mengganti Elemen String
# Metode yang bertujuan untuk mengganti elemen string dengan elemen string lainnya.
# a. replace()

# 5.Fungsi-fungsi yang bertujuan untuk melakukan pengecekan pada string dan mengembalikan nilai Boolean.
# a. sisupper()
# b. islower()
# c. isalpha()
# d. isalnum()
# e. isdecimal()
# f. isspace()
# g. istitle()

# 6. Formatting pada String
# Fungsi-fungsi untuk pemformatan string.
# a. zfill()
# b. rjust()
# c. ljust()
# d. center()

# 7. String Literals
# literals adalah serangkaian karakter yang diapit oleh tanda kutip baik tunggal (') maupun ganda (").

# String dapat ditulis mudah dalam Python dengan cara diapit oleh tanda petik tunggal. Namun, dalam kondisi tertentu, dibutuhkan petik tunggal di tengah string (misalnya struktur kepemilikan dalam Bahasa Inggris—Dicoding's Cat atau penyebutan Jum'at pada hari dalam bahasa Indonesia).

# Solusinya adalah menggunakan escape character yang memungkinkan Anda untuk menggunakan karakter yang sebelumnya tidak bisa dimasukkan dalam string. Umumnya diawali dengan backslash (\) dan diikuti karakter tertentu yang diinginkan. Beberapa contoh escape charactersebagai berikut.

# a. \' Single quote
# b. \" Double quote
# c. \t Tab
# d. \n Newline (line break)
# e. \\ Backslash

