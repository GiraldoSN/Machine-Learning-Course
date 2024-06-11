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
