# Pengantar Unit Testing
"""
Di sinilah kita butuh pengujian (tes) untuk fungsi-fungsi tersebut. Pengujian sebenarnya dapat dibedakan menjadi dua tipe, yaitu manual dan otomatis. 

Manual testing adalah proses pengujian yang dilakukan oleh seseorang yang ditunjuk sebagai tester (penguji). 
Testing otomatis merupakan hal yang sebaliknya. Ini adalah pengujian yang dilakukan secara otomatis terhadap kode-kode yang kita bangun berdasarkan rencana pengujian (test plan). 
Tidak hanya sekadar manual dan otomatis, ada juga unit testing dan integration testing.

Integration testing adalah pengujian yang bertujuan untuk menguji suatu sistem sebagai satu kesatuan. 
Unit testing adalah pengujian yang lebih spesifik dan fokus terhadap bagian-bagian kecil. 
Dalam Python, untuk melakukan unit testing dapat menggunakan library unittest. Layaknya sebuah framework pengujian, unittest mendukung beberapa hal esensial berikut.

Pengujian secara otomatis.
Kode awal proses (setup) dan akhir proses (shutdown) yang dapat digunakan ulang.
Penyatuan sejumlah pengujian dalam sebuah koleksi.
Terpisahnya framework pengujian dari framework pelaporan (reporting).
Library unittest mendukung sejumlah konsep penting yang berorientasi objek, antara lain berikut.

Test fixture merepresentasikan persiapan yang dibutuhkan untuk melakukan satu pengujian atau lebih serta proses pembersihannya (cleanup).
Test case adalah sebuah unit dari pengujian ketika ia mengecek sejumlah respons dari sebagian kelompok masukan. unittest menyediakan basis class dan TestCase yang akan digunakan untuk membuat kasus pengujian baru.
Test suite adalah sebuah koleksi dari kasus-kasus pengujian, koleksi dari test suite itu sendiri, atau gabungan keduanya.
Test runner adalah komponen yang akan mengatur (orchestrates) eksekusi dari pengujian-pengujian dan menyediakan keluaran untuk pengguna.

"""


# Penerapan Unit Test dengan Library unittest
"""
Unit melakukan unit testing, Anda bisa menggunakan library bawaan dari Python, yaitu unittest.
"""

# import unittest

# Berikut adalah salah satu penerapan unit testing dengan menggunakan library unittest.
import unittest
 
def koneksi_ke_db():
    print("[terhubung ke db]")
 
def putus_koneksi_db(db):
    print("[tidak terhubung ke db {}]".format(db))
 
class User:
    username = ""
    aktif = False
 
    def __init__(self, db, username):  # using db sample
        self.username = username
 
    def set_aktif(self):
        self.aktif = True
 
 
class TestUser(unittest.TestCase):
    # Test Case 1
    def test_user_default_not_active(self):
        db = koneksi_ke_db()
        dicoding = User(db, "dicoding")
        self.assertFalse(dicoding.aktif)  # tidak aktif secara default
        putus_koneksi_db(db)
 
    # Test Case 2
    def test_user_is_active(self):
        db = koneksi_ke_db()
        dicoding = User(db, "dicoding")
        dicoding.set_aktif()  # aktifkan user baru
        self.assertTrue(dicoding.aktif)
        putus_koneksi_db(db)
 
if __name__ == "__main__":
    # Test Runner
    unittest.main()