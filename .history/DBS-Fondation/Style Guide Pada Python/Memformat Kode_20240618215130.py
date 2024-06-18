"""
black
black adalah proyek open source yang dikembangkan di repository Python Software Foundation (PSF) dengan lisensi MIT. Untuk mendapatkan gambaran, versi online (tidak resmi) ada di https://black.now.sh.

Untuk instalasi, silakan buka terminal Anda dan jalankan kode berikut.
"""
# pip install black

"""
YAPF (Yet Another Python Formatter)
YAPF adalah proyek open source yang dikembangkan di repository Google dengan lisensi Apache.

Untuk instalasi, silakan buka terminal Anda dan jalankan kode berikut.
"""
# pip install yapf


"""
autopep8
autopep8 adalah proyek open source (berlisensi MIT) yang termasuk paling awal untuk memformat kode dengan bantuan lint pycodestyle.

Untuk instalasi, silakan buka terminal Anda dan jalankan kode berikut.
"""
# pip install autopep8


# Buka script kalkulator.py dan salin kode berikut.
class Kalkulator:
    """kalkulator tambah kurang"""
    def __init__(self, _i):
        self.i = _i
    def tambah(self, _i): return self.i + _i
    def kurang(self, _i):
        return self.i - _i
    
"""
Mari jalankan file atau script tersebut dengan aplikasi yang telah kita instal. Buka kembali terminal Anda, pastikan membuka direktori tempat file atau script Anda berada.
"""
"""
black
Untuk menguji menggunakan black, jalankan kode berikut.
"""
# black kalkulator.py


"""
yapf
Untuk menguji menggunakan yapf, jalankan kode berikut.
"""