import math

print(math.sqrt(25)) 
print(math.pi) 

"""
Output:
5.0
3.141592653589793
"""

"""
Pada contoh di atas, hal pertama yang dilakukan adalah melakukan impor modul math untuk menyediakan berbagai fungsi dan konstanta matematika. Di bawahnya, kita mencoba melakukan operasi akar dari bilangan 25 yang hasilnya adalah 5. Kemudian, kita mencoba mendapatkan nilai pi dalam modul math yang bernilai “3.141592653589793”.
"""

"""
NumPy
Library NumPy adalah package fundamental yang sering digunakan untuk scientific computing pada Python. Library ini menyediakan objek array multidimensi, berbagai jenis objek lainnya, seperti masked array dan matrix, dan sebagainya.
"""


"""
Silakan buka command prompt dan jalankan kode berikut.
pip install numpy
Anda juga bisa menggunakan conda untuk menginstal NumPy, berikut sintaksnya.

conda install numpy
Berikut adalah contoh penggunaan NumPy.
"""


import numpy

matriks = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8 ,9]])
print(matriks)

"""
Output:
[[1 2 3]
 [4 5 6]
 [7 8 9]]
"""

"""
Matplotlib
Selanjutnya adalah matplotlibyang merupakan library untuk melakukan visualisasi data. Matplotlib termasuk jenis library eksternal sehingga Anda perlu melakukan instalasi matplotlib terlebih dahulu. Silakan jalankan kode berikut.
python -m pip install -U matplotlib
Anda bisa juga jalankan kode berikut jika ingin menggunakan conda.

conda install matplotlib
"""