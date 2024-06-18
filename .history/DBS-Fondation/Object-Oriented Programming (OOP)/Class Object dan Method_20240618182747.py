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