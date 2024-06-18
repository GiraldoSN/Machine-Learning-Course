# Deklarasi Matriks

"""
Deklarasi sekaligus inisialisasi nilai matriks.
Cara pertama adalah mendeklarasikan matriks sekaligus menginisialisasikan nilainya dengan ukuran N baris dan M Kolom (NxM). Cara ini dilakukan jika kita telah mengetahui nilai yang perlu diberikan.
"""

"""
Jika nilai yang diberikan adalah bilangan real, tipe elemen adalah float.
Mari lihat implementasi kodenya di bawah ini.
"""

matriks = [[1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1]]
     
print(matriks)

"""
Output:
[[1, 0, 0, 0, 0],[0, 1, 0, 0, 0],[0, 0, 1, 0, 0],[0, 0, 0, 1, 0],[0, 0, 0, 0, 1]]
"""

"""
<n> sebagai jumlah baris matriks yang ingin dibuat dan <m> sebagai jumlah kolom matriks yang diinginkan.
"""
matriks = [[0 for j in range(4)] for i in range(3)]

print(matriks)

"""
Output:
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

"""

"""
Jika kita ingin mengakses nilai 12 pada matriks di atas, nilai tersebut berada pada indeks baris ke-2 dan indeks kolom ke-1. Dalam pemrograman, nilai tersebut bisa diasumsikan dengan "[2][1]" dengan nilai 2 adalah indeks atau nomor baris dan nilai 1 adalah indeks atau nomor kolom.

Mari lihat penerapannya di bawah ini.
"""

var_mat = [[1, 2, 3, 4, 5],
           [6, 7, 8, 9, 10],
           [11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20],
           [21, 22, 23, 24, 25]]
           
print(var_mat[2][1])

"""
Output:
12
"""