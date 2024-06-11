"""
TODO:
Buatlah sebuah variabel bertipe list bernama "evenNumber" dengan ketentuan:
- variabel tersebut menampung bilangan genap dari 0 hingga 500 (ingat 0 dan 500 termasuk).

Tips:
Anda bisa menggunakan loop dan if atau list comprehension untuk memudahkan.
"""

# TODO: Silakan buat kode Anda di bawah ini.

evenNumber = [i for i in range(0, 501) if i % 2 == 0]
print(evenNumber)

"""
Kode ini menggunakan list comprehension untuk memudahkan pembuatan daftar bilangan genap. Berikut penjelasan singkatnya:

range(0, 501) menghasilkan bilangan bulat dari 0 hingga 500.
if i % 2 == 0 memfilter bilangan-bilangan tersebut agar hanya bilangan genap yang dimasukkan ke dalam daftar.
Hasilnya adalah sebuah list yang berisi bilangan genap dari 0 hingga 500.
"""