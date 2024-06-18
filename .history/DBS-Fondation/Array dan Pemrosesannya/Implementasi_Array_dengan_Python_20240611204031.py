# Implementasi Array dengan Python

# Mendeklarasikan Array

var_list = [1,2,3]
for elemen in var_list:
    print(id(elemen))
    
"""
Outputnya
140031974050096
140031974050128
140031974050160
"""

# Mendefinisikan Isi Array

"""
<nama-var> merupakan nama variabel array yang dideklarasikan sebanyak n dengan elemen-elemennya adalah <val0>, <val1>, <val2>, … , <valn-1>. Perlu diingat bahwa elemen tersebut terurut berdasarkan indeks dari 0 hingga n-1. 

Contohnya sebagai berikut.
"""

var_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(var_arr)

"""
Output:
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
"""

# Mendefinisikan Nilai Default
"""
Berikut adalah penjelasan lebih detail terkait struktur tersebut.

<nama-var> merupakan variabel yang Anda deklarasikan.
<default-val> merupakan nilai default yang Anda definisikan. Umumnya, programmer akan menggunakan nilai di luar range yang telah disepakati sebagai nilai default. Misalnya jika range nilai yang disepakati seharusnya 1 hingga 10, nilai default bisa kita definisikan dengan 0. 
<n> merupakan ukuran panjangnya array.
Mari lihat contoh penerapannya di bawah ini.
"""

var_arr = [0 for i in range(10)]
print(var_arr)

"""
Output:
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
"""
"""
 mengubah nilai default tersebut dengan nilai yang baru berdasarkan hasil suatu operasi. Misalkan pada contoh di bawah ini.
"""
var_arr = [0 for i in range(10)]

for i in range(10):
    var_arr[i] = i

print(var_arr)


"""
Output:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""


# Mengakses Elemen Array
  """
  
  """