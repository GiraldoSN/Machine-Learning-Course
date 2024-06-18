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

