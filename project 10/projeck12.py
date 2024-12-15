import csv
import os

# Nama file untuk menyimpan data karyawan
namafile = "data_karyawan.csv"

# Fungsi untuk inisialisasi file CSV jika belum ada
def init_csv():
    if not os.path.exists(namafile):
        with open(namafile, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Nama", "Jabatan", "Gaji"])
        print("File CSV berhasil dibuat.")

# Fungsi untuk menambah karyawan baru
def tambah_karyawan(id, nama, jabatan, gaji):
    with open(namafile, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id, nama, jabatan, gaji])
    print(f"Karyawan dengan ID {id} berhasil ditambahkan.")

# Fungsi untuk menghapus karyawan berdasarkan ID
def hapus_karyawan(id):
    rows = []
    with open(namafile, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != id:
                rows.append(row)
    
    with open(namafile, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print(f"Karyawan dengan ID {id} berhasil dihapus.")

# Fungsi untuk menampilkan seluruh data karyawan
def tampilkan_karyawan():
    with open(namafile, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(', '.join(row))

# Main program
init_csv()
while True:
    print("\n--- Sistem Manajemen Data Karyawan ---")
    print("1. Tambah Karyawan")
    print("2. Hapus Karyawan")
    print("3. Tampilkan Data Karyawan")
    print("4. Keluar")
    
    pilihan = input("Masukkan pilihan (1/2/3/4): ")
    
    if pilihan == '1':
        id = input("Masukkan ID: ")
        nama = input("Masukkan Nama: ")
        jabatan = input("Masukkan Jabatan: ")
        gaji = input("Masukkan Gaji: ")
        tambah_karyawan(id, nama, jabatan, gaji)
    
    elif pilihan == '2':
        id = input("Masukkan ID karyawan yang ingin dihapus: ")
        hapus_karyawan(id)
    
    elif pilihan == '3':
        tampilkan_karyawan()
    
    elif pilihan == '4':
        print("Keluar dari program.")
        break
    
    else:
        print("Pilihan tidak valid. Coba lagi.")