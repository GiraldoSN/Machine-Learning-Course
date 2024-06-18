"""
Mari lihat contoh pewarisan di bawah ini, asumsikan bahwa kita perlu membuat kelas Mobil sebagai kelas dasar. Dari kelas Mobil ini, kita akan membuat kelas Mobil baru bernama Mobil Sport dengan fitur yang sama seperti kelas dasarnya. Namun, ada tambahan fitur baru pada kelas tersebut, yakni turbo untuk meningkatkan kecepatan mobil hingga 50 km/jam.
"""

class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambah_kecepatan(self):
        self.kecepatan += 10

mobil_1 = Mobil("Merah", "DicodingCar", 160)
print(mobil_1.kecepatan)

"""
Output:
160
"""

# Kita akan membuat sebuah kelas baru bernama "MobilSport" yang mewarisi atribut dan metode kelas Mobil dasar. Lalu, kita menambahkan metode baru, yaitu turbo untuk meningkatkan kecepatan sebesar 50.

class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambah_kecepatan(self):
        self.kecepatan += 10


class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50

# Kelas Mobil Dasar
mobil_1 = Mobil("Merah", "DicodingCar", 160)
print(mobil_1.kecepatan)

# Kelas Mobil Sport
mobil_sport_1 = MobilSport("Hitam", "DicodingSportCar", 160)
print(mobil_sport_1.kecepatan)
mobil_sport_1.turbo()
print(mobil_sport_1.kecepatan)

"""
Output:
160
160
210
"""


# Override
"""
Selanjutnya, seperti yang dijelaskan di awal, ketika kita membuat metode baru di kelas turunan (kelas baru) dengan nama yang sama seperti metode di kelas induk, itu akan menyebabkan metode baru menimpa (override) metode dari kelas induk.
"""

class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambah_kecepatan(self):     # tambah_kecepatan
        self.kecepatan += 10

class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50
    
    def tambah_kecepatan(self):     # tambah_kecepatan
        self.kecepatan += 20

# Kelas Mobil Sport
mobil_sport_1 = MobilSport("Hitam", "DicodingSportCar", 160)
print(mobil_sport_1.kecepatan)
mobil_sport_1.tambah_kecepatan()     # Memanggil metode baru tambah kecepatan()
print(mobil_sport_1.kecepatan)

"""
Output:
160
180
"""

"""
Pada contoh di atas, kita menambahkan metode baru bernama tambah_kecepatan. Metode ini juga ada di kelas mobil dasar. Namun, kita melakukan perbedaan pada metode baru ini berupa penambahan kecepatan yang awalnya sebesar 10 di kelas induk, menjadi sebesar 20 di kelas baru. Hasilnya, dapat kita lihat bahwa kecepatan kini bertambah 20 setiap kita memanggil metode tambah_kecepatan().

Namun, perlu dipahami bahwa menimpa bukan berarti mengubah metode dari kelas induk. Hal ini karena metode dari kelas baru tersebut merupakan hasil dari pewarisan sehingga tidak akan mengubah metode dari kelas induk. Silakan tambahkan kode berikut ke program di atas pada bagian akhir kode (sebelum komentar output).
"""

# Super

class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambah_kecepatan(self):
        self.kecepatan += 10


class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50
    
    def tambah_kecepatan(self):
        super().tambah_kecepatan()
        print("Kecepatan Anda meningkat! Hati-Hati!")

# Kelas Mobil Sport
mobil_sport_1 = MobilSport("Hitam", "DicodingSportCar", 160)
mobil_sport_1.tambah_kecepatan()     # Memanggil metode baru tambah kecepatan()
print(mobil_sport_1.kecepatan)

"""
Output:
Kecepatan Anda meningkat! Hati-hati!
170
"""