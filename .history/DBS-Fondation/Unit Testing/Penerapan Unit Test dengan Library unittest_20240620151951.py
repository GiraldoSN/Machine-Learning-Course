import unittest
 
class TestStringMethods(unittest.TestCase):
    # Ini adalah test case pertama (1)
    def test_strip(self):
        self.assertEqual('www.dicoding.com'.strip('c.mow'), 'dicoding')
    
    # Test case kedua (2)
    def test_isalnum(self):
        self.assertTrue('c0d1ng'.isalnum())
        self.assertFalse('c0d!ng'.isalnum())
    
    # Test case ketiga (3)
    def test_index(self):
        s = 'dicoding'
        self.assertEqual(s.index('coding'), 2)
        # cek s.index gagal ketika tidak ditemukan
        with self.assertRaises(ValueError):
            s.index('decode')
    
if __name__ == '__main__':
    # Test Runner
    unittest.main()
    
    
# Jalankan program di atas dengan mengeksekusi file yang telah Anda buat. 
"""
python <nama-file>.py

Ganti <nama-file> dengan nama file Anda dan hasil keluarannya seperti berikut.
"""


"""
Mari kita bahas satu per satu dari kode di atas.

Kelas TestStringMethods adalah sebuah kelas yang merupakan turunan (subclass) dari class unittest.TestCase sehingga proses tes dapat dilangsungkan tanpa banyak implementasi lain.
Ada tiga metode pada class tersebut yang semua namanya diawali dengan kata test. Hal ini merupakan konvensi (aturan) yang wajib diikuti untuk menginformasikan ke test runner bahwa sejumlah metode tersebut merepresentasikan tes yang akan dioperasikan.
Pada setiap metode, pengujian dilakukan dengan pemanggilan assert. Pada metode test_strip pengecekan kesamaan menggunakan assertEqual dilakukan untuk memastikan bahwa 'www.dicoding.com'.strip('c.mow') sama dengan ‘dicoding’.
Pada metode test_isalnum pengecekan bahwa fungsi bernilai benar (True) dilakukan dengan assertTrue untuk memastikan jika 'c0d1ng'.isalnum() bernilai benar, yakni ‘cOd1ng’ adalah betul bertipe alfanumerik. Kemudian juga ada pengecekan bahwa fungsi bernilai salah (False) dengan assertFalse untuk memastikan jika 'c0d!ng'.isalnum() betul bernilai salah karena ada karakter yang bukan alfanumerik yaitu ‘!’.
Pada metode test_index pengecekan kesamaan dilakukan seperti sebelumnya dengan menggunakan assertEqual bahwa pencarian substring coding menempati index sama dengan 2. Kemudian juga ada pengecekan bahwa ValueError akan dibangkitkan dengan menggunakan assertRaises(ValueError), jika pencarian index tidak berhasil ditemukan pada string yang sudah ditentukan.
Pada bagian terakhir kode, ada pemanggilan unittest.main() untuk mulai menjalankan test.
"""

"""
Anda bisa mencoba melihat keluaran lain dengan membuat gagal salah satu test. Misalnya pada metode test_isalnum, keduanya akan diubah menggunakan assertTrue sehingga salah satu fungsi akan gagal. Kodenya bisa Anda lihat di bawah
"""

def test_isalnum(self):
       self.assertTrue('c0d1ng'.isalnum())  # ini akan berhasil
       self.assertTrue('c0d!ng'.isalnum())  # ini akan gagal
       
"""
Berikut penjelasannya.

Layaknya yang sudah Anda duga bahwa akan ada pengujian yang gagal sehingga tertulis .F. yang menggambarkan bahwa pengujian metode kedua gagal (FAIL).
Berikutnya dijelaskan bahwa kegagalan ada dalam metode test_isalnum, yaitu sebuah metode dari class __main__.TestStringMethods.
Lebih jauh, diinformasikan bahwa test_isalnum yang gagal berada pada baris ke-10 pada kode Anda, yakni pada pengecekan self.assertTrue('c0d!ng'.isalnum()) yang memang tadi kita ubah dari assertFalse. Sistem pengujian juga melaporkan bahwa pembandingannya tidak sesuai, yakni False tidak bernilai benar seperti yang diharapkan dengan adanya pengujian assertTrue.
Rekap totalnya ada tiga tes yang dilakukan dalam 0.01 detik. Kemudian secara umum tes menghasilkan satu buah kegagalan (failure).
"""

# Untuk menyederhanakan kodenya dan lebih fokus pada pengujiannya, tulis simulasinya dalam satu file kode sebagai berikut.

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