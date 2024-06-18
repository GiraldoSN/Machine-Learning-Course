class Mobil:
    # Atribut
    warna = "Merah"

mobil_1 = Mobil()
print(mobil_1.warna)

"""
Output:
Merah
"""

# mengubah atribut tersebut sesuai kebutuhan
class Mobil:
    # Atribut
    warna = 'Merah'

mobil_1 = Mobil()
mobil_1.warna = "Biru"
print(mobil_1.warna)

"""
Output:
Biru
"""

# Atribut
class Mobil:
    # Atribut kelas
    warna = "Merah"

mobil1 = Mobil()
print(mobil1.warna)

mobil2 = Mobil()
print(mobil2.warna)

# Mengubah atribut kelas
Mobil.warna = "Hitam"

print(mobil1.warna)
print(mobil2.warna)

"""
Output:
Merah
Merah
Hitam
Hitam
"""


mobil1 = Mobil()
print(mobil1.warna)
 
mobil2 = Mobil()
print(mobil2.warna)


# Mengubah atribut kelas
Mobil.warna = "Hitam"

# Class Constructor

class Mobil:
    # Atribut Instance
    def __init__(self):
        self.warna = 'Merah'
        
mobil_1 = Mobil()
mobil_2 = Mobil()

print(mobil_1.warna)
print(mobil_2.warna)

# Mengubah atribut instance
mobil_1.warna = "Hitam"

# Menampilkan kembali atribut warna
print(mobil_1.warna)
print(mobil_2.warna)

"""
Output:
Merah
Merah
Hitam
Merah
"""

# Jika sebelumnya kita hanya menggunakan parameter self saja dalam class constructor, parameter lain pun dapat ditambahkan sesuai kebutuhan.ika sebelumnya kita hanya menggunakan parameter self saja dalam class constructor, parameter lain pun dapat ditambahkan sesuai kebutuhan.

class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
        
mobil_1 = Mobil('Merah', 'DicodingCar', 160)

print(mobil_1.warna)
print(mobil_1.merek)
print(mobil_1.kecepatan)

"""
Output:
Merah
DicodingCar
160
"""

def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
        
# Method

def my_decorator(func):
    def wrapper():
        print("Sebelum fungsi dieksekusi.")
        func()
        print("Setelah fungsi dieksekusi.")
    return wrapper

# Dekorasi fungsi dengan decorator
@my_decorator
def say_hello():
    print("Hello, world!")

# Memanggil fungsi yang sudah didekorasi
say_hello()

"""
Output:
Sebelum fungsi dieksekusi.
Hello, world!
Setelah fungsi dieksekusi.
"""

"""
Penjelasan dari contoh di atas adalah berikut.

Pertama, kita mendefinisikan sebuah fungsi bernama my_decorator. Dekorator ini menerima sebuah fungsi func sebagai parameternya.
Dalam fungsi my_decorator, kita mendefinisikan fungsi wrapper(). Fungsi wrapper() bertindak sebagai "pembungkus" yang menambahkan perilaku sebelum dan setelah eksekusi dari fungsi func.
Setelah itu, fungsi  my_decorator mengembalikan (return) fungsi wrapper sebagai hasilnya. Return ini juga menyebabkan fungsi wrapper dijalankan.
Kemudian, kita mendefinisikan fungsi say_hello(). Fungsi ini akan menjadi target dekorasi.
Untuk mendekorasi say_hello(), kita menggunakan simbol "@" diikuti dengan nama dekorator, yaitu @my_decorator sebelum mendefinisikan fungsi say_hello.
Jadi, secara alur, ketika fungsi say_hello() dipanggil, sebenarnya yang dieksekusi adalah fungsi wrapper() yang menjadi hasil dari dekorasi. Oleh karena itu, pesan "Sebelum fungsi dieksekusi." dicetak terlebih dahulu, kemudian fungsi say_hello() dieksekusi dan mencetak "Hello, world!", lalu akhirnya, pesan "Setelah fungsi dieksekusi." dicetak.
Dekorator sangat berguna untuk menambahkan fungsionalitas tambahan pada suatu fungsi atau metode tanpa harus mengubah kode asli dari fungsi tersebut. Anda bisa membaca lebih dalam mengenai dekorator pada laman ini.
"""

# Namun, kita menambahkan metode bernama "tambah_kecepatan" dan setiap metode ini dipanggil maka kecepatan mobil akan bertambah 10

class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):
        self.kecepatan += 10

mobil_1 = Mobil("Merah", "DicodingCar", 160)
print("Sebelum ditambahkan: ")
print(mobil_1.kecepatan)

mobil_1.tambah_kecepatan()        # Memanggil metode tambah_kecepatan.

print("Setelah ditambahkan: ")
print(mobil_1.kecepatan)

# Jadi, kita tidak bisa memanggil metode ini langsung melalui kelasnya
class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambah_kecepatan(self):
        self.kecepatan += 10
        
Mobil.tambah_kecepatan()

"""
Output:
Traceback (most recent call last):
  File "/home/glot/main.py", line 10, in <module>
    Mobil.tambah_kecepatan()
TypeError: tambah_kecepatan() missing 1 required positional argument: 'self'
"""

# Metode secara Statis (Static Method)
class Mobil:
    def __init__(self, merek):
        self.merek = merek
    
    @staticmethod
    def intro_mobil():
        print("Ini adalah metode dari kelas Mobil")
        
Mobil.intro_mobil()
mobil_1 = Mobil("DicodingCar")
mobil_1.intro_mobil()

"""
Output:
Ini adalah metode dari kelas Mobil
Ini adalah metode dari kelas Mobil
"""

# Metode dari Kelas (Class Method)
class Mobil:
    def __init__(self, merek):
        self.merek = merek

    @classmethod
    def intro_mobil(cls):
        print("Ini adalah metode dari kelas Mobil")
        
Mobil.intro_mobil()
mobil_1 = Mobil("DicodingCar")
mobil_1.intro_mobil()

"""
Output:
Ini adalah metode dari kelas Mobil
Ini adalah metode dari kelas Mobil
"""

# menambahkan argumen tambahan pada posisi pertama berupa kelas itu sendiri