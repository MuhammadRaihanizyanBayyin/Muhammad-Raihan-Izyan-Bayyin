import csv
from datetime import datetime

# Daftar film yang tersedia
films = [
    {"judul": "Godzilla x kong:The New Empire", "harga_tiket": 50000, "jam_tayang": ["10:00", "13:00", "16:00", "19:00"]},
    {"judul": "Avangers:Endgame", "harga_tiket": 45000, "jam_tayang": ["11:00", "14:00", "17:00", "20:00"]},
    {"judul": "Jurassic World", "harga_tiket": 55000, "jam_tayang": ["09:00", "12:00", "15:00", "18:00"]},
    {"judul": "Guardians of the Galaxy", "harga_tiket": 48000, "jam_tayang": ["10:30", "13:30", "16:30", "19:30"]}
]

# Fungsi untuk menampilkan daftar film dan jam tayang
def tampilkan_daftar_film():
    print("\nDaftar Film yang Tersedia:")
    for index, film in enumerate(films, start=1):
        print(f"{index}. {film['judul']}")
        print(f"   Harga Tiket: Rp {film['harga_tiket']}")
        print(f"   Jam Tayang: {', '.join(film['jam_tayang'])}")
        print()

# Fungsi untuk memilih film dan jam tayang
def pilih_film():
    while True:
        try:
            pilihan = int(input("Pilih nomor film yang ingin ditonton (1-4): "))
            if 1 <= pilihan <= len(films):
                film_pilihan = films[pilihan - 1]
                print(f"\nAnda memilih film: {film_pilihan['judul']}")
                return film_pilihan
            else:
                print("Pilihan tidak valid. Coba lagi.")
        except ValueError:
            print("Masukkan angka yang valid.")

# Fungsi untuk memilih jam tayang
def pilih_jam_tayang(film):
    while True:
        print("\nJam tayang yang tersedia:")
        for i, jam in enumerate(film['jam_tayang'], start=1):
            print(f"{i}. {jam}")
        try:
            pilihan_jam = int(input("Pilih jam tayang (1-4): "))
            if 1 <= pilihan_jam <= len(film['jam_tayang']):
                jam_tayang_pilihan = film['jam_tayang'][pilihan_jam - 1]
                print(f"\nJam tayang yang Anda pilih: {jam_tayang_pilihan}")
                return jam_tayang_pilihan
            else:
                print("Pilihan tidak valid. Coba lagi.")
        except ValueError:
            print("Masukkan angka yang valid.")

# Fungsi untuk memilih jumlah tiket
def pilih_jumlah_tiket():
    while True:
        try:
            jumlah_tiket = int(input("Masukkan jumlah tiket yang ingin dipesan: "))
            if jumlah_tiket > 0:
                return jumlah_tiket
            else:
                print("Jumlah tiket harus lebih dari 0.")
        except ValueError:
            print("Masukkan angka yang valid.")

# Fungsi untuk menghitung total harga
def hitung_total_harga(harga_tiket, jumlah_tiket):
    return harga_tiket * jumlah_tiket

# Fungsi untuk menyimpan riwayat pemesanan ke CSV
def simpan_riwayat_pemesanan(judul, jumlah_tiket, jam_tayang, total_harga):
    # Menyimpan riwayat pemesanan ke file CSV
    filename = "riwayat_pemesanan.csv"
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([judul, jumlah_tiket, jam_tayang, total_harga, datetime.now().strftime('%Y-%m-%d %H:%M:%S')])
    print("Riwayat pemesanan telah disimpan.")

# Fungsi utama untuk menjalankan sistem pemesanan tiket bioskop
def sistem_pemesanan_tiket():
    while True:
        tampilkan_daftar_film()
        film_pilihan = pilih_film()
        jam_tayang_pilihan = pilih_jam_tayang(film_pilihan)
        jumlah_tiket = pilih_jumlah_tiket()
        
        total_harga = hitung_total_harga(film_pilihan['harga_tiket'], jumlah_tiket)
        
        print(f"\nTotal harga tiket: Rp {total_harga}")
        
        # Menyimpan riwayat pemesanan
        simpan_riwayat_pemesanan(film_pilihan['judul'], jumlah_tiket, jam_tayang_pilihan, total_harga)
        
        # Menanyakan apakah pengguna ingin memesan lagi
        ulangi = input("\nApakah Anda ingin memesan tiket lagi? (ya/tidak): ").lower()
        if ulangi != 'ya':
            print("Terima kasih telah menggunakan sistem pemesanan tiket bioskop.")
            break

# Menjalankan sistem pemesanan tiket
if __name__ == "__main__":
    sistem_pemesanan_tiket()
