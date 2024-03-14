# Mengubah Huruf Besar/Kecil
# upper() -> semua huruf menjadi kapital
kata = "dicoding"
kata = kata.upper()
print(kata)

# lower() -> semua huruf kecil
kata = "DICODING"
kata = kata.lower()
print(kata)

# Awalan dan Akhiran
# rstrip() -> Metode rstrip() menghapus whitespace pada sebelah kanan atau akhir string.
print("Dicoding          ".rstrip())

# lstrip() -> Kebalikan dari rstrip(), lstrip() bertugas untuk menghapus whitespace pada sebelah kiri atau awal string.
print("Dicoding".lstrip())
# Pada kode di atas, Anda menghapus spasi yang berada di sebelah kiri sebelum string "Dicoding" menggunakan metode ".lstrip()".?

# strip() -> Metode ini bertugas untuk menghapus whitespace pada bagian awal dan akhir string.
print("Dicoding".strip())
# Pada kode di atas, Anda menghapus spasi yang berada di sebelah kiri dan kanan setelah string "Dicoding" menggunakan metode "strip()".

# Jika ingin menghilangkan karakter selain whitespace, Anda bisa mengikuti contoh berikut.
kata = "CodeCodeDicodingCodeCode"
print(kata.strip("Code"))

"""
Output:
Dicoding
"""
# Anda dapat mengganti whitespace dengan kata atau hal lainnya. Caranya adalah memberikan nilai pada ".strip()". Kode di atas menghapus kata "Code" pada variabel "kata".

# startswith() -> Metode startswith() bertujuan untuk menemukan suatu kata pada awal string. Metode ini mengembalikan nilai True.
print("Dicoding Indonesia".startswith("Dicoding"))

"""
Output:
True
"""
# Pada kode di atas, Anda mencari string "Dicoding" pada string pertama "Dicoding Indonesia".
# Operasi ini mengembalikan nilai True karena pada string "Dicoding Indonesia" memang diawali dengan string "Dicoding".

# endswith() -> Metode endswith() bertujuan untuk menemukan suatu kata pada akhir string. Metode ini juga mengembalikan nilai True jika menemukannya, sedangkan jika tidak menemukan kata yang diinginkan, nilai False dikembalikan.
print("Dicoding Indonesia".endswith("Dicoding"))

"""
Output:
False
"""
# Pada kode di atas, Anda mencari string "Dicoding" pada string terakhir "Dicoding Indonesia".
# Operasi ini mengembalikan nilai False karena pada string "Dicoding Indonesia" tidak diakhiri dengan string "Dicoding", tetapi diakhiri dengan string "Indonesia".

# Memisah dan Menggabung String
# join() ->
print(" ".join(["Dicoding", "Indonesia", "!"]))

"""
Output:
Dicoding Indonesia !
# """
# Pada kode di atas, Anda menggabungkan string "Dicoding", "Indonesia", dan "!" yang telah disimpan pada variabel list.
# Perhatikan bahwa pada sintaks awal sebelum ".join()" Anda menambahkan single quotes di sana. Single quotes ini bermaksud agar Anda menentukan delimiter pada setiap kata/nilai yang ingin Anda gabungkan. Pada kode di atas, delimiter-nya adalah whitespace atau spasi.

# Anda juga bisa menambahkan delimiter lain, contohnya berikut.
print("123".join(["Dicoding", "Indonesia"]))

"""
Output:
Dicoding123Indonesia
"""
# Pada kode di atas, Anda memasukkan delimeter "123" sehingga output-nya adalah "Dicoding123Indonesia123".

# split() -> Kebalikan dari metode sebelumnya, metode split() bertujuan untuk memisahkan kata/substring berdasarkan delimiter.
print("Dicoding Indonesia !".split())

"""
Output:
['Dicoding','Indonesia','!']
"""
# Anda juga bisa menggunakan delimiter newline (\n) untuk memisahkan setiap baris pada string multiline.
print(
    """Halo,
aku ikan,
aku suka sekali menyelam
aku tinggal di perairan.
Badanku licin dan renangku cepat.
Senang berkenalan denganmu.""".split(
        "\n"
    )
)

"""
Output:
['Halo,', 'aku ikan,', 'aku suka sekali menyelam', 'aku tinggal di perairan.', 'Badanku licin dan renangku cepat.', 'Senang berkenalan denganmu.']
"""

# Mengganti Elemen String -> replace()
string = "Ayo belajar Coding di Dicoding"
print(string.replace("Coding", "Pemrograman"))

"""
Output:
Ayo belajar Pemrograman di Dicoding
"""

# Pengecekan String -> isupper()

# islower() -> Kebalikannya, islower() akan mengembalikan nilai True jika semua huruf dalam string adalah huruf kecil (lowercase).

# isalpha() -> Metode ini mengembalikan nilai True jika semua karakter dalam string adalah huruf alfabet. Jika ada satu huruf lain yang bukan alfabet, seperti angka, nilai False akan dikembalikan.

kata = "dicoding"
print(kata.isalpha())

"""
Output:
True
"""
# isalnum() -> Metode isalnum() mengembalikan nilai True jika karakter dalam string adalah alfanumerik, yaitu hanya huruf atau hanya angka atau berisi keduanya. Jika tidak, nilai False akan dikembalikan.

kata = "dicoding123"
print(kata.isalnum())

"""
Output:
True
"""

# isdecimal() -> Metode isdecimal() akan mengembalikan nilai True jika karakter dalam string berisi hanya angka/numerik. Jika tidak, nilai False akan dikembalikan.

print("123".isdecimal())

"""
Output:
True
"""

# istitle() -> Metode istitle() mengembalikan nilai True jika string berisi huruf kapital pada setiap kata pertamanya. Jika tidak, nilai False dikembalikan.

print("Dicoding Indonesia".istitle())

"""
Output:
True
"""

# Formatting pada String

# zfill() -> Metode zfill() bertujuan untuk menambahkan nilai nol (0) di depan sebuah string dengan panjang tertentu. Tujuan dari metode ini
# adalah membantu untuk memastikan bahwa sebuah angka atau nilai memiliki panjang tetap, terutama ketika ingin menyimpan nilai dalam format yang konsisten.

teks = "Code"
tambah_number = teks.zfill(5)
print(tambah_number)

"""
Output:
0Code
"""


# rjust() -> Metode rjust() berguna untuk merapikan pencetakan teks. Dengan metode rjust() ini, Anda dapat membuat teks menjadi rata kanan
# sehingga tampilannya lebih rapi.

print("Dicoding".rjust(20))

"""
Output:
            Dicoding

"""

# Anda juga bisa menambahkan teks lain, tidak hannya whitespace

print('Dicoding'.rjust(20, '!'))

"""
Output:
!!!!!!!!!!!!Dicoding
"""

# ljust() -> Selanjutnya adalah metode ljust(), metode ini adalah kebalikan dari metode rjust()
# yang bertujuan untuk membuat teks menjadi rata kiri.

print('Dicoding'.ljust(20))

"""
Output:
Dicoding            '
"""

# enter() -> Metode center() menjadikan teks rata tengah. Metode ini akan menambahkan whitespace di sebelah kiri dan kanan secara default.
# Anda juga bisa mengganti whitespace tersebut dengan karakter lain.

print('Dicoding'.center(10, '-'))

"""
Output:
-Dicoding-

"""

# String Literals -> Umumnya, string ditulis dengan mudah di Python, diapit oleh tanda petik tunggal. 
# Namun, dalam kondisi tertentu, dibutuhkan petik tunggal di tengah string (misalnya, struktur kepemilikan dalam bahasa Inggris—Dicoding's Cat atau penyebutan Jum'at pada hari dalam bahasa Indonesia).

# Misalnya, kita menuliskannya sebagai berikut :

    # 1. st1 = "Jum'at" -> Python mengenali bahwa petik tunggal adalah bagian tidak terpisahkan dari string tersebut.
    
    # 2. st1 = 'Jum\'at' -> sebelum petik terdapat backslash (\) yang menandakan petik tunggal sebagai bagian dari string dan bukan akhir dari string. Escape character \' dan \" memungkinkan Anda untuk memasukkan karakter ' dan '' dalam bagian string.
    
# Beberapa contoh escape character lainnya sebagai berikut:

# \' Single quote
# \" Double quote
# \t Tab
# \n Newline (line break)
# \\ Backslash

print("Halo!\nKapan terakhir kali kita bertemu?\nKita bertemu hari Jum\'at yang lalu.")


"""
Output:
Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum'at yang lalu.
"""