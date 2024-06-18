# Lint
"""
Lint adalah proses pengecekan kode atas kemungkinan terjadi kesalahan (error), termasuk dalam proses ini adalah mengecek kesesuaian terhadap arahan gaya penulisan kode (style guide) PEP8. Aplikasi yang digunakan untuk proses ini disebut linter. 
"""

# silakan buka terminal Anda dan jalankan kode di bawah ini sesuai yang Anda pilih.

# Pycodestyle (sebelumnya bernama pep8)
"""
Pycodestyleadalah aplikasi open source (berlisensi MIT/Expat) untuk membantu mengecek kode terkait gaya penulisan kode dengan konvensi PEP8. Untuk instalasi, silakan buka terminal Anda dan jalankan kode berikut.
"""
# pip install pycodestyle

# Pylint
"""
Pylintadalah aplikasi open source (berlisensi GPL v2) untuk melakukan analisis kode Python, mengecek untuk kesalahan (error) pemrograman, memaksakan standar penulisan kode dengan mengecek penulisan kode yang tidak baik, serta memberikan saran untuk refactoring sederhana. Untuk instalasi, silakan buka terminal Anda dan jalankan kode berikut.
"""
# pip install pylint

# Flake8
"""
Flake8adalah aplikasi open source (berlisensi MIT) yang membungkus sejumlah kemampuan aplikasi lain, seperti pycodestyle, pyflakes, dan (skrip/fitur) lainnya. Untuk instalasi, silakan buka terminal Anda dan jalankan kode berikut.
"""
# pip install flake8


# Buat sebuah file bernama kalkulator.py dan masukkan kode berikut.
class Kalkulator:
    """kalkulator tambah kurang"""
    def __init__(self, _i):
        self.i = _i
    def tambah(self, _i): return self.i + _i
    def kurang(self, _i):
    return self.i - _i

"""
Mari kita jalankan file atau script tersebut dengan aplikasi yang telah diinstal. Buka kembali terminal Anda, pastikan membuka direktori tempat file atau script Anda berada.
"""
"""
Pycodestyle
Untuk menguji menggunakan pycodestyle, jalankan kode berikut.
"""
# pycodestyle kalkulator.py


"""
Pylint
Untuk menguji menggunakan pylint, jalankan kode berikut.
"""

pylint kalkulator.py