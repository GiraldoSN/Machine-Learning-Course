"""
TODO:
Buatlah sebuah fungsi bernama "minimal" dengan ketentuan berikut.
- Menerima dua buah argumen berupa number, yaitu a dan b.
- Mengembalikan nilai terkecil antara a atau b.
- Bila nilai keduanya sama, kembalikan dengan nilai a.
"""

# TODO: Silakan buat kode Anda di bawah ini.

"""
TODO:
Buatlah sebuah fungsi bernama "minimal" dengan ketentuan berikut.
- Menerima dua buah argumen berupa number, yaitu a dan b.
- Mengembalikan nilai terkecil antara a atau b.
- Bila nilai keduanya sama, kembalikan dengan nilai a.
"""

# TODO: Silakan buat kode Anda di bawah ini.
# Nama file: minimal_function.py


def minimal(a, b):
    if a < b:
        return a
    else:
        return b


# Contoh penggunaan fungsi
if __name__ == "__main__":
    print("Minimal antara 3 dan 5 adalah:", minimal(3, 5))  # Output: 3
    print("Minimal antara 10 dan 2 adalah:", minimal(10, 2))  # Output: 2
    print("Minimal antara 4 dan 4 adalah:", minimal(4, 4))  # Output: 4
