# Capstone 1

# Data awal rempah-rempah
rempah_list = [
    {"nama": "Jahe", "harga_per_kg": 20000, "jumlah_terjual": 15},
    {"nama": "Kunyit", "harga_per_kg": 18000, "jumlah_terjual": 10},
    {"nama": "Temulawak", "harga_per_kg": 12000, "jumlah_terjual": 20},
    {"nama": "Vanili", "harga_per_kg": 1500000, "jumlah_terjual": 30},    
    {"nama": "Serai", "harga_per_kg": 18000, "jumlah_terjual": 5},
]

# Fungsi untuk menampilkan data
def tampilkan_rempah():
    if not rempah_list:
        print("Belum ada data.")
    else:
        for i, r in enumerate(rempah_list):
            print(f"{i + 1}. {r['nama']} - Harga: Rp{r['harga_per_kg']:,} - Terjual: {r['jumlah_terjual']} kg")

# Menu utama dengan loop
while True:
    print("\n=== MENU PENJUALAN REMPAH ===")
    print("1. Tampilkan Data (Read)")
    print("2. Tambah Data (Create)")
    print("3. Ubah Data (Update)")
    print("4. Hapus Data (Delete)")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        tampilkan_rempah()

    elif pilihan == "2":
        nama = input("Nama rempah: ")
        harga = int(input("Harga per kg: "))
        jumlah = int(input("Jumlah terjual (kg): "))
        rempah_list.append({"nama": nama, "harga_per_kg": harga, "jumlah_terjual": jumlah})
        print("Data berhasil ditambahkan.")

    elif pilihan == "3":
        tampilkan_rempah()
        idx = int(input("Masukkan nomor data yang ingin diubah: ")) - 1
        if 0 <= idx < len(rempah_list):
            nama = input("Nama baru: ")
            harga = int(input("Harga baru per kg: "))
            jumlah = int(input("Jumlah terjual baru (kg): "))
            rempah_list[idx] = {"nama": nama, "harga_per_kg": harga, "jumlah_terjual": jumlah}
            print("Data berhasil diubah.")
        else:
            print("Nomor tidak valid.")

    elif pilihan == "4":
        tampilkan_rempah()
        idx = int(input("Masukkan nomor data yang ingin dihapus: ")) - 1
        if 0 <= idx < len(rempah_list):
            del rempah_list[idx]
            print("Data berhasil dihapus.")
        else:
            print("Nomor tidak valid.")

    elif pilihan == "5":
        print("Terima kasih. Program selesai.")
        break

    else:
        print("Pilihan tidak valid. Coba lagi.")

