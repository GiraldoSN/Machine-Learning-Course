# Statement Gabungan

if foo == 'blah':
    do_blah_thing()
do_one()
do_two()
do_three()

"""
Saat trailing comma bersifat redundan, Anda akan merasakan kemudahannya saat menggunakan VCS (Version Control System), atau pada kode yang mungkin ditambahkan dalam beberapa waktu ke depan. Pola yang disarankan adalah meletakkan nilai atau string pada sebuah baris baru, mengikuti indentasi, menambahkan trailing comma, dan menutup kurung/kurawal/siku pada baris selanjutnya.

Tidak umum jika Anda menempatkan trailing comma pada baris letak Anda menutup kurung/kurawal/siku seperti di bawah ini, kecuali dalam tuple dengan satu elemen, seperti yang dijelaskan di atas.
"""

FILES = [
    'setup.cfg',
    'tox.ini',
    ]
initialize(FILES,
           error=True,
           )

# Anotasi Fungsi

""""
"""