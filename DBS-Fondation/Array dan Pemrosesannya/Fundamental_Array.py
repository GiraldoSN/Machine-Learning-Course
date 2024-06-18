# Fundamental Array

x = [1, 2, 3, 4, 5]
print(x)

"""
Output:
[1, 2, 3, 4, 5]
"""

import array

x = array.array("i",[1, 2, 3, 4, 5])
print(x)
print(type(x))

"""
Output:
array('i', [1, 2, 3, 4, 5])
<class 'array.array'>
"""

"""
"Selepas berakhirnya semester genap, para guru dari SMA Dicoding perlu merekap semua nilai ujian akhir semester. Salah satunya adalah guru matematika, guru tersebut perlu merekap nilai dari seluruh siswa yang ada di kelas IPA 1. Guru tersebut membuat program menggunakan Python untuk mempermudah proses rekap nilai."
"""

nama_siswa1 = 90
nama_siswa2 = 100
nama_siswa3 = 50
nama_siswa4 = 80
nama_siswa5 = 85
nama_siswa6 = 45
nama_siswa7 = 80
nama_siswa8 = 75
nama_siswa9 = 50
nama_siswa10 = 60

print(nama_siswa1)
print(nama_siswa2)
print(nama_siswa3)
print(nama_siswa4)
print(nama_siswa5)
print(nama_siswa6)
print(nama_siswa7)
print(nama_siswa8)
print(nama_siswa9)
print(nama_siswa10)

"""
Output:
90
100
50
80
85
45
80
75
50
60
"""

# bagaimana dengan 100 siswa? 1000 siswa?

siswa = [90, 100, 50, 80, 85, 45, 80, 75, 50, 60]

print(siswa)
print(siswa[0])


"""
Output:
[90, 100, 50, 80, 85, 45, 80, 75, 50, 60]
90
"""