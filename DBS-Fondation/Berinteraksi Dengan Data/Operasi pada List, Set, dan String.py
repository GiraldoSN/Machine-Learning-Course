# len() -> Fungsi len() bertujuan untuk menghitung panjang atau banyaknya elemen dari list, set, dan string.
# Khusus pada string, program akan menghitung jumlah karakternya.

# List

contoh_list = [1, 3, 3, 5, 5, 5, 7, 7, 9]

print(contoh_list)
print(len(contoh_list))

"""
Output:
[1, 3, 3, 5, 5, 5, 7, 7, 9]
9
"""

# Dalam kode di atas, Anda menampilkan panjang dari anggota yang berada pada list.
# Anda bisa memperhatikan lebih detail setiap anggota list memang berjumlah 9 atau tidak.

# Set

contoh_list = set([1, 3, 3, 5, 5, 5, 7, 7, 9])

print(contoh_list)
print(len(contoh_list))

"""
Output:
{1, 3, 5, 7, 9}
5
"""

# Pada kode diatas set itu berperan untuk menghitung banyaknya jumlah yang ada dalam golongan tersebut tanpa ada urutan yang sama (double)

# String
contoh_list = "Belajar Python"

print(contoh_list)
print(len(contoh_list))

"""
Output:
Belajar Python
14
"""

# menghitung jumlah karakter string yang ada pada variabel "contoh_list". Perhatikan bahwa karakter space dihitung sebagai karakter string.

# min() dan max() -> Selain menghitung panjang atau banyaknya elemen, Anda juga dapat mengetahui berapa nilai minimum dan maksimum dari suatu list menggunakan fungsi min() dan max().

angka = [13, 7, 24, 5, 96, 84, 71, 11, 38]
print(min(angka))
print(max(angka))

"""
Output:
5
96            
"""

# Pada kode diatas akan mencari nilai terkecil (minimal) dan nilai terbesar (maksimal) pada variabel "angka" yang merupakan list.

# Count -> Fungsi count() digunakan untuk mengetahui berapa kali suatu objek muncul dalam list.

genap = [2, 4, 4, 6, 6, 6, 8, 10, 10]
print(genap.count(6))

"""
Output:
3
"""

# Namun, pada kode di bawah, program akan menghitung banyaknya substring/huruf "a" dalam string.

string = "Belajar Python di Dicoding sangat menyenangkan"
substring = "a"
print(string.count(substring))


"""
Output:
6
"""

# In dan Not In
# In dan not in merupakan operator yang diperuntukkan untuk mengetahui nilai atau objek yang ada dalam list. Anda bisa menggunakan operator ini untuk memastikan suatu nilai ada dalam list bahkan dalam string. Operator in dan not in akan mengembalikan nilai boolean True atau False.
kalimat = "Belajar Python di Dicoding sangat menyenangkan"
print('Dicoding' in kalimat)
print('tidak' in kalimat)
print('Dicoding' not in kalimat)
print('tidak' not in kalimat)

"""
Output:
True
False
False
True

"""