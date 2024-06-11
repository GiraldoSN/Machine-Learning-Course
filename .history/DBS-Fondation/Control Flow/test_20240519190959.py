# Mendefinisikan kriteria dan skala penilaian
kriteria = {
    'C1': {'SK': (3, 4), 'K': (4.1, 5), 'C': (5.1, 6), 'B': (6.1, 7), 'SB': (7, float('inf'))},
    'C2': {'SK': (2, 3), 'K': (3.5, 4.5), 'C': (5, 6), 'B': (6.5, 7.5), 'SB': (8, float('inf'))},
    'C3': {'SK': 'Macet', 'K': 'Diragukan', 'C': 'Tidak Lancar', 'B': 'DPK', 'SB': 'Lancar'},
    'C4': {'SK': (100, 200), 'K': (200, 300), 'C': (300, 400), 'B': (400, 500), 'SB': (500, float('inf'))}
}

skor = {'SK': 1, 'K': 2, 'C': 3, 'B': 4, 'SB': 5}

# Mendefinisikan bobot untuk masing-masing kriteria
bobot = {'C1': 0.25, 'C2': 0.25, 'C3': 0.25, 'C4': 0.25}

def evaluasi_kriteria(nilai, kriteria):
    for tingkat, batas in kriteria.items():
        if isinstance(batas, tuple):
            if batas[0] <= nilai <= batas[1]:
                return skor[tingkat]
        else:
            if nilai == batas:
                return skor[tingkat]
    return 0

def hitung_skor(c1, c2, c3, c4):
    skor_c1 = evaluasi_kriteria(c1, kriteria['C1'])
    skor_c2 = evaluasi_kriteria(c2, kriteria['C2'])
    skor_c3 = evaluasi_kriteria(c3, kriteria['C3'])
    skor_c4 = evaluasi_kriteria(c4, kriteria['C4'])
    
    total_skor = (skor_c1 * bobot['C1'] +
                  skor_c2 * bobot['C2'] +
                  skor_c3 * bobot['C3'] +
                  skor_c4 * bobot['C4'])
    
    return total_skor

# Contoh penggunaan sistem pendukung keputusan
gaji = 6.5  # Gaji dalam juta
income_lain = 5  # Income lain dalam juta
bi_checking = 'DPK'  # BI Checking
agunan = 450  # Agunan/Jaminan dalam juta

skor_total = hitung_skor(gaji, income_lain, bi_checking, agunan)
print(f"Skor Total: {skor_total}")

# Menentukan keputusan berdasarkan skor total
if skor_total >= 4.5:
    keputusan = "Sangat Baik"
elif skor_total >= 3.5:
    keputusan = "Baik"
elif skor_total >= 2.5:
    keputusan = "Cukup"
elif skor_total >= 1.5:
    keputusan = "Kurang"
else:
    keputusan = "Sangat Kurang"

print(f"Keputusan: {keputusan}")
