"""
TODO:
Sebuah variabel array diberikan dengan ketentuan berikut.
- Variabel array bernama "var_array" dengan nilai dari 0 hingga 100.
- Hitung nilai rata-rata dari elemen array tersebut.
- Simpan hasil perhitungan dalam variabel bernama "result".

Tips:
- Rumus menghitung rata-rata adalah jumlah seluruh elemen dibagi banyaknya elemen.
- Gunakan percabangan dan perulangan untuk mempermudah, 
  Anda tidak diperbolehkan memberikan nilai secara langsung.
"""
# Jangan ubah kode ini
var_array = [i for i in range(101)]

# TODO: Silakan buat kode Anda di bawah ini.
# Jangan ubah kode ini
var_array = [i for i in range(101)]

# Menghitung jumlah seluruh elemen dalam var_array
total_sum = 0
for number in var_array:
    total_sum += number

# Menghitung banyaknya elemen dalam var_array
number_of_elements = len(var_array)

# Menghitung nilai rata-rata
result = total_sum / number_of_elements

# Menampilkan hasil
print("Nilai rata-rata dari elemen var_array adalah:", result)
