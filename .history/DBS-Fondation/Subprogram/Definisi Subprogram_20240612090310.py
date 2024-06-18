# Salah satu kode yang sering berulang adalah rumus atau formula, perhatikan kode di bawah ini.
# Luas pertama
panjang = 5
lebar = 10

luas_persegi_panjang = panjang * lebar
print(luas_persegi_panjang)

# Luas kedua
panjang = 4
lebar = 15

luas_persegi_panjang = panjang * lebar
print(luas_persegi_panjang)

"""
Output:
50
60
"""

# Bandingkan kode sebelumnya dengan kode berikut.

def mencari_luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)
print(persegi_panjang_pertama)

persegi_panjang_kedua = mencari_luas_persegi_panjang(4,15)
print(persegi_panjang_kedua)

"""
Output:
50
60
"""

"""
Kode di atas merupakan program yang sama dengan sebelumnya dan bertujuan untuk mencari luas persegi panjang. Namun, kali ini kita menggunakan sebuah konsep yang disebut fungsi. Blok fungsi pada kode di atas dimulai dari "def" hingga "return".

Ini adalah tujuan akhir dari materi kali ini, Anda diharapkan memahami subprogram yang di antaranya adalah fungsi dan prosedur.

Subprogram adalah serangkaian instruksi dirancang untuk melakukan operasi yang sering digunakan dalam suatu program. Subprogram yang sering digunakan terdiri dari dua jenis, yakni berikut.

Fungsi
Fungsi adalah blok kode yang dapat menerima input, melakukan pemrosesan, dan mengembalikan output. Hasil atau output tersebut dinyatakan dalam sebuah tipe data yang eksplisit. Artinya, fungsi yang dibuat dapat ditentukan untuk mengembalikan tipe data integer, string, atau lainnya.
Prosedur
Prosedur adalah deretan instruksi yang jelas keadaan awal (initial state) dan keadaan akhirnya (final state). Prosedur mirip dengan program secara umum, tetapi memiliki cakupan yang kecil dan terbatas.
Sekarang, mari kita pelajari satu per satu mengenai fungsi dan prosedur.
"""