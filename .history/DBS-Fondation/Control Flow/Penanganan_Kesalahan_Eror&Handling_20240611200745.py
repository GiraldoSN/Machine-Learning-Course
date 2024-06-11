"""
Penanganan Kesalahan (Error Handling and Exception Handling)
Saat Anda membuat program, sering kali menemukan setidaknya dua jenis kesalahan berdasarkan kejadiannya.

Kesalahan sintaks (syntax errors) atau sering disebut juga sebagai kesalahan penguraian (parsing errors). 
Pengecualian (exceptions) atau sering disebut juga sebagai kesalahan saat beroperasi (runtime errors). 
"""

# Kesalahan Sintaks (Syntax Errors)
if 9>10:
print("Hello World!")

"""
Output:
File "/home/glot/main.py", line 2
    print("Hello World!")
    ^
IndentationError: expected an indented block
"""

i = 1
while i<3
    print("Dicoding")
    i+=1

"""
Output:
  File "/home/glot/main.py", line 2
    while i<3
             ^
SyntaxError: invalid syntax
"""

# Pengecualian (Exceptions)
print(angka)

"""
Output:
Traceback (most recent call last):
  File "/home/glot/main.py", line 1, in <module>
    print(angka)
NameError: name 'angka' is not defined
"""

# Mari lihat contoh pengecualian selanjutnya.

bukan_angka = '1'
bukan_angka + 2


"""
Output:
Traceback (most recent call last):
  File "/home/glot/main.py", line 2, in <module>
    bukan_angka + 2
TypeError: can only concatenate str (not "int") to str
"""

# Penanganan Pengecualian
z = 0
print(1/z)

"""
Output:
Traceback (most recent call last):
  File "/home/glot/main.py", line 2, in <module>
    print(1/z)
ZeroDivisionError: division by zero
"""

z=0
try:
    print(1/z)
except ZeroDivisionError:
    print("Anda tidak bisa membagi angka dengan nilai nol.")

"""
Output:
Anda tidak bisa membagi angka dengan nilai nol.
"""