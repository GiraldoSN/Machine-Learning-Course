"""
Matriks dalam pemrograman dapat kita simpulkan sebagai berikut.

Matriks adalah kumpulan data yang diatur dalam bentuk tabel dua dimensi dengan setiap elemennya terdefinisi berdasarkan baris dan kolom.
Setiap elemen matriks dapat diakses melalui metode indexing jika kedua indeks telah diketahui.
Elemen matriks dideklarasikan memiliki tipe homogen yang artinya elemen tersebut harus mempunyai tipe data yang sama. Jika elemen tersebut adalah bilangan real, seluruh elemen lainnya pun adalah bilangan real. Walaupun dalam list Python Anda dapat membuat matriks dengan tipe data berbeda, alangkah lebih baik jika tetap mengikuti aturan ini.
"""

matriks = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
            
print(matriks)

"""
Output:
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
"""

# pip show numpy
# pip install numpy

import numpy

matriks = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8 ,9]])
print(matriks)

"""
Output:
[[1 2 3]
 [4 5 6]
 [7 8 9]]
"""

# bandingkan ukuran memori yang digunakan jika kita menggunakan matriks Python dan matriks NumPy.
import numpy 
import sys

var_list= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
var_array= numpy.array([[1, 2, 3], [4, 5, 6], [7, 8 ,9]])

print("Ukuran keseluruhan elemen list dalam bytes = ",sys.getsizeof(var_list)*len(var_list))
print("Ukuran keseluruhan elemen NumPy dalam bytes = ", var_array.size*var_array.itemsize)


"""
Output:
Ukuran keseluruhan elemen list dalam bytes =  240
Ukuran keseluruhan elemen NumPy dalam bytes =  72
"""