# Fundamental Prosedur
# Berikut adalah contoh prosedur dalam Python.
def greeting(name):
    print("Halo " + name + ", Selamat Datang!")

"""
Kita sebenarnya bisa menambahkan pernyataan return, tetapi kita tidak menyertakan return value setelahnya.
"""

def greeting(name):
    print("Halo " + name + ", Selamat Datang!")
    return

# Mendefinisikan dan Memanggil Prosedur

def greeting(name):
    print("Halo " + name + ", Selamat Datang!")

greeting("Dicoding Indonesia")

"""
Output: 
Halo Dicoding Indonesia, Selamat Datang!
"""


def greeting():
    print("Halo Selamat Datang!")

greeting()

"""
Output: 
Halo Selamat Datang!
"""