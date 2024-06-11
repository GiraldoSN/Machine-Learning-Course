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
    "C1": {"SK": (3000000, 3800000), "K": (4000000, 5000000), "C": (5100000, 6000000), "B": (6100000, 7000000), "SB": (7000000, float('inf'))},
    "C2": {"SK": (2000000, 3000000), "K": (3500000, 4500000), "C": (5000000, 6000000), "B": (6500000, 7500000), "SB": (8000000,, "kosong",float('inf'))},
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
