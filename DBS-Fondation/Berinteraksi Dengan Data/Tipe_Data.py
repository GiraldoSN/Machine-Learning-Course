# Integer adalah Bilangan bulat positif atau negatif dan tidak memiliki angka desimal.
# Contoh: 1; -20; 999; dan 0.

# Float adalah Bilangan riil yang dapat mewakili bilangan bulat atau bilangan desimal.
# Contoh: 3.14; 1; dan 4.01E+1

# Complex adalah Bilangan kompleks. (Kita tidak akan menggunakannya di kelas ini.)
# Contoh: 1+2j

# Berikut adalah implementasi tipe data numbers ke dalam Python.

x = 6
print(type(x))

x = 6.0
print(type(x))

x = 1 + 2j
print(type(x))

# Berikut adalah contoh tipe data numbers bersifat immutable yang artinya nilai di dalamnya tidak dapat diubah.
var = 10
print(var)
print(id(var))
var = 11
print(var)
print(id(var))

# Boolean memiliki dua sifat yakni true dan false

# Tipe data primitif kedua adalah boolean, yakni tipe data yang hanya bernilai TRUE atau FALSE. Tipe data ini
# merepresentasikan nilai kebenaran (truth values). Sebenarnya, setiap variabel yang memiliki nilai bisa dievaluasi
# dan menghasilkan nilai true. Hanya ada beberapa nilai yang akan dianggap bernilai false sebagai berikut.
# 1. Nilai yang sudah didefinisikan bernilai salah: None dan False.
# 2. Angka nol dari semua tipe numerik: 0, 0.0, 0j, Decimal(0), Fraction(0,1).
# 3. Urutan (sequence) dan koleksi (collection) yang kosong: “”, (), {}, set(), range(0).
x = True
print(type(x))

x = False
print(type(x))

# String merupakan karakter yang berurutan. Ketika Anda membuat variabel bernilai string tentu diawali dengan single quote
# (‘’) atau double quote (“”). Jalankan kode di bawah ini untuk mengetahui contoh tipe data string.

x = "Dicoding"
print(type(x))

# Beberapa fakta menarik lainnya dari string Python adalah berikut.
# 1. tiga single quote atau double quote untuk menyimpan string yang lebih dari satu baris (multi-line).
multi_line = """Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum’at yang lalu."""

print(multi_line)

# Pada kode di atas, Anda menampilkan string lebih dari satu baris (multi-line) menggunakan double quote (”””).
# 2.String merupakan urutan karakter yang setiap karakternya memiliki indeks. Anda dapat mengakses setiap karakter dari string (substring) dengan menggunakan metode indexing. Perlu diingat bahwa indeks selalu dimulai dari 0.
x = "Dicoding"
print(x[0])
# Pada kode di atas, diambil indeks ke-0 dari string “Dicoding” yakni huruf “D”. Metode indexing merupakan cara untuk mengambil spesifik elemen berdasarkan indeksnya

# 3. mengakses beberapa substring dengan menggunakan metode indexing dan slicing
x = "Dicoding"
print(x[2:])
# Pada kode di atas, diambil substring dari indeks ke-2 hingga indeks terakhir dengan menggunakan metode slicing. Metode slicing adalah cara yang sering digunakan untuk mendapatkan bagian dari suatu list atau array.
# Metode ini dapat diterapkan pada string untuk mengambil satu atau banyak substring. Kita akan mempelajari lebih detail pada materi list.

# menampilkan teks/string berdasarkan input dari pengguna dengan berbagai cara. Perhatikan metode di bawah ini dan jalankan kodenya menggunakan IDE atau notebook

# Formatted String
name = "Perseus Evans"
print(f"Hello, nama saya {name}")
# Pada kode di atas, Anda menampilkan string dengan menggunakan metode formatted string. Metode ini diperuntukkan untuk menampilkan variabel bertipe string dengan menggunakan huruf “f” di depan string dan menempatkan variabel di dalam kurung kurawal.

# %-formatting
name = "Perseus Evans"
print("Nama saya %s" % (name))
# Pada kode di atas, Anda menampilkan variabel string dengan menggunakan metode “%-formatting”. Metode ini adalah pendekatan lama yang masih didukung oleh Python. Metode ini menggunakan operator Modulo (%) untuk memasukkan nilai variabel ke dalam string dengan menggunakan format khusus yang ditentukan oleh tipe data variabel.

# str.format()
name = "Perseus Evans"
print("Nama saya {}".format(name))
# Pada kode di atas, Anda menampilkan variabel string dengan menggunakan metode “str.format()”. Metode ini memungkinkan penggabungan variabel/nilai ke dalam string dengan menempatkan tanda kurung kurawal atau {} sebagai penempatan variabel. Sekilas mirip dengan formatted string, pembedanya adalah pada penggunaan “.format” setelah string.

# Kuis Tipe Data
"""
TODO:
Buatlah variabel firstName, lastName, age, isMarried dengan ketentuan:
- firstName: isi dengan nama depan Anda bertipe data string.
- lastName: isi dengan nama belakang Anda bertipe data string.
- age: isi dengan umur Anda bertipe data integer.
- isMarried: isi dengan status pernikahan Anda bertipe data boolean.
Catatan:
- Value variabel harus berupa nilai sesungguhnya (literal) seperti string, 
  bilangan bulat (integer), dan boolean (benar atau salah).
"""

# Isi dengan informasi pribadi Anda
firstName = "NamaDepan"
lastName = "NamaBelakang"
age = 25  # Ganti dengan umur Anda
isMarried = False  # Ganti dengan status pernikahan Anda, True jika sudah menikah, False jika belum

# Cetak informasi yang telah diisi
print("First Name:", firstName)
print("Last Name:", lastName)
print("Age:", age)
print("Is Married:", isMarried)

# TODO: Silakan buat kode Anda di bawah ini.

"""
TODO:
Buatlah variabel dictionary dengan nama "data_diri",
variabel tersebut berisi identitas diri Anda berdasarkan ketentuan berikut.
- Memiliki key bernama "firstName":
    - Isi value dengan nama depan Anda, pastikan bertipe data string.
- Memiliki key bernama "lastName":
    - Isi value dengan nama terakhir Anda, pastikan bertipe data string.
- Memiliki key bernama "age":
    - Isi value dengan umur Anda, pastikan bertipe data integer.
- Memiliki key bernama "isMarried":
    - Isi value dengan status pernikahan Anda, pastikan bertipe data boolean.

Catatan:
- Value pada dictionary harus berupa nilai sesungguhnya (literal) seperti string, 
  bilangan bulat (integer), dan boolean (benar atau salah).
"""

data_diri = {
    "firstName": "NamaDepan",
    "lastName": "NamaBelakang",
    "age": 25,  # Ganti dengan umur Anda
    "isMarried": False,  # Ganti dengan status pernikahan Anda, True jika sudah menikah, False jika belum
}
# Cetak dictionary "data_diri"
print("Data Diri:")
for key, value in data_diri.items():
    print(f"{key}: {value}")

# TODO: Silakan buat kode Anda di bawah ini.
