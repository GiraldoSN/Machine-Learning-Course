"""
Kategori : Object-Oriented Programming (OOP)

Manakah kode di bawah ini yang merupakan kode untuk membuat object method dan tidak menghasilkan error?
"""

class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan


    def tambah_kecepatan(self):
        self.kecepatan += 10
        
