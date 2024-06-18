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