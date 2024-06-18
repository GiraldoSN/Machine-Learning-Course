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

"""
Pada ilustrasi tersebut, kita mengalikan matriks "[5, 0], [1, -2]" dengan konstanta "2". Nilai konstanta tersebut kemudian dikalikan dengan setiap elemen matriks. Kalkulasinya dapat kita urai seperti berikut. 

Pertama, konstanta "2" akan dikalikan dengan elemen 5 yang menghasilkan nilai 10 (2 X 5 = 10).
Kedua, konstanta "2" akan dikalikan dengan elemen 0 yang menghasilkan nilai 0 (2 X 0 = 0).
Ketiga, konstanta "2" akan dikalikan dengan elemen 1 yang menghasilkan nilai 2 (2 X 1 = 2).
Terakhir, konstanta "2" akan dikalikan dengan elemen -2 yang menghasilkan nilai -4 (2x-2 = -4).
Jika kita ubah ke dalam pemrograman, hasilnya sebagai berikut.
"""

# Membuat matriks 2x2
var_mat = [[5, 0],
          [1, -2]]
def_mat = [[0 for j in range(2)] for i in range(2)]

for i in range(len(var_mat)):
  for j in range(len(var_mat[0])):
    def_mat[i][j] = var_mat[i][j]*2

print(def_mat)

"""
Output:
[[10, 0], [2, -4]]
"""

# menggunakan library NumPy
