# Definisi skala penilaian
SK = 1
K = 2
C = 3
B = 4
SB = 5

# Rentang nilai untuk setiap kriteria
def nilai_gaji(gaji):
    if 3 <= gaji <= 4:
        return SK
    elif 4.1 <= gaji <= 5:
        return K
    elif 5.1 <= gaji <= 6:
        return C
    elif 6.1 <= gaji <= 7:
        return B
    elif gaji > 7:
        return SB
    else:
        return 0

def nilai_income_lain(income):
    if 2 <= income <= 3:
        return SK
    elif 3.5 <= income <= 4.5:
        return K
    elif 5 <= income <= 6:
        return C
    elif 6.5 <= income <= 7.5:
        return B
    elif income > 8:
        return SB
    else:
        return 0

def nilai_bi_checking(bi_check):
    if bi_check == 'Macet':
        return SK
    elif bi_check == 'Diragukan':
        return K
    elif bi_check == 'Tidak Lancar':
        return C
    elif bi_check == 'DPK':
        return B
    elif bi_check == 'Lancar':
        return SB
    else:
        return 0

def nilai_agunan(agunan):
    if 100 <= agunan <= 200:
        return SK
    elif 200 <= agunan <= 300:
        return K
    elif 300 <= agunan <= 400:
        return C
    elif 400 <= agunan <= 500:
        return B
    elif agunan > 500:
        return SB
    else:
        return 0

# Contoh data alternatif nasabah
data_nasabah = [
    {'nama': 'A1', 'gaji': 4.5, 'income_lain': 3.0, 'bi_checking': 'Diragukan', 'agunan': 250},
    {'nama': 'A2', 'gaji': 6.0, 'income_lain': 6.5, 'bi_checking': 'Lancar', 'agunan': 450},
    # Tambahkan data nasabah lainnya hingga A50
    # Contoh data dummy tambahan
    {'nama': 'A3', 'gaji': 7.5, 'income_lain': 8.5, 'bi_checking': 'Lancar', 'agunan': 600},
    {'nama': 'A4', 'gaji': 3.5, 'income_lain': 3.5, 'bi_checking': 'Macet', 'agunan': 150},
]

def hitung_skor_nasabah(nasabah):
    skor_c1 = nilai_gaji(nasabah['gaji'])
    skor_c2 = nilai_income_lain(nasabah['income_lain'])
    skor_c3 = nilai_bi_checking(nasabah['bi_checking'])
    skor_c4 = nilai_agunan(nasabah['agunan'])
    
    total_skor = skor_c1 + skor_c2 + skor_c3 + skor_c4
    return total_skor

# Tambahkan skor ke data nasabah
for nasabah in data_nasabah:
    nasabah['skor'] = hitung_skor_nasabah(nasabah)

def cari_nasabah(nama):
    for nasabah in data_nasabah:
        if nasabah['nama'] == nama:
            return nasabah
    return None

# Contoh penggunaan
nama_nasabah = input("Masukkan nama nasabah (misal: A1, A2, dst): ")
nasabah = cari_nasabah(nama_nasabah)

if nasabah:
    print(f"Data Nasabah {nama_nasabah}:")
    print(f"Gaji: {nasabah['gaji']} (Skor: {nilai_gaji(nasabah['gaji'])})")
    print(f"Income Lain: {nasabah['income_lain']} (Skor: {nilai_income_lain(nasabah['income_lain'])})")
    print(f"BI Checking: {nasabah['bi_checking']} (Skor: {nilai_bi_checking(nasabah['bi_checking'])})")
    print(f"Agunan: {nasabah['agunan']} (Skor: {nilai_agunan(nasabah['agunan'])})")
    print(f"Total Skor: {nasabah['skor']}")
else:
    print(f"Nasabah dengan nama {nama_nasabah} tidak ditemukan.")
# Mendefinisikan data nasabah
nasabah = {}

# Mendefinisikan skala penilaian
penilaian = {
    "SK": 1,
    "K": 2,
    "C": 3,
    "B": 4,
    "SB": 5
}

# Mendefinisikan rentang kriteria
kriteria = {
    "C1": {"SK": (3000000, 4000000), "K": (4100000, 5000000), "C": (5100000, 6000000), "B": (6100000, 7000000), "SB": (7000000, float('inf'))},
    "C2": {"SK": (2000000, 3000000), "K": (3500000, 4500000), "C": (5000000, 6000000), "B": (6500000, 7500000), "SB": (8000000, float('inf'))},
    "C3": {"SK": "Macet", "K": "Diragukan", "C": "Tidak Lancar", "B": "DPK", "SB": "Lancar"},
    "C4": {"SK": (100000000, 200000000), "K": (200000000, 300000000), "C": (300000000, 400000000), "B": (400000000, 500000000), "SB": (500000000, float('inf'))}
}

# Fungsi untuk mengkonversi nilai ke skala penilaian
def konversi_nilai(kriteria, nilai):
    for key, value in kriteria.items():
        if isinstance(value, tuple) and value[0] <= nilai <= value[1]:
            return key
        elif isinstance(value, str) and value == nilai:
            return key
    return "SK"

# Fungsi untuk memasukkan data nasabah
def masukkan_data(nasabah_id):
    c1 = float(input("Masukkan Gaji (C1) untuk {}: ".format(nasabah_id)))
    c2 = float(input("Masukkan Income Lain (C2) untuk {}: ".format(nasabah_id)))
    c3 = input("Masukkan BI Checking (C3) untuk {} (Macet/Diragukan/Tidak Lancar/DPK/Lancar): ".format(nasabah_id))
    c4 = float(input("Masukkan Agunan/Jaminan (C4) untuk {}: ".format(nasabah_id)))

    nasabah[nasabah_id] = {
        "C1": penilaian[konversi_nilai(kriteria["C1"], c1)],
        "C2": penilaian[konversi_nilai(kriteria["C2"], c2)],
        "C3": penilaian[konversi_nilai(kriteria["C3"], c3)],
        "C4": penilaian[konversi_nilai(kriteria["C4"], c4)]
    }

# Fungsi untuk menampilkan data nasabah
def tampilkan_data(nasabah_id):
    if nasabah_id in nasabah:
        print("Data untuk {}:".format(nasabah_id))
        for key, value in nasabah[nasabah_id].items():
            print("{}: {}".format(key, value))
    else:
        print("Data untuk {} tidak ditemukan.".format(nasabah_id))

# Menu utama
def menu():
    while True:
        print("\nMenu:")
        print("1. Masukkan data nasabah")
        print("2. Tampilkan data nasabah")
        print("3. Keluar")
        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == "1":
            nasabah_id = input("Masukkan ID Nasabah: ")
            masukkan_data(nasabah_id)
        elif pilihan == "2":
            nasabah_id = input("Masukkan ID Nasabah yang ingin ditampilkan: ")
            tampilkan_data(nasabah_id)
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

# Menjalankan menu utama
menu()
