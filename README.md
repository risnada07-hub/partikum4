# partikum4 
# Inisialisasi list kosong untuk menyimpan data semua mahasiswa
data_mahasiswa = []

# --- Fungsi untuk Menghitung Nilai Akhir ---
def hitung_nilai_akhir(tugas, uts, uas):
    """
    Menghitung nilai akhir berdasarkan bobot:
    Tugas: 30%, UTS: 35%, UAS: 35%
    """
    bobot_tugas = 0.30
    bobot_uts = 0.35
    bobot_uas = 0.35
    
    nilai_akhir = (tugas * bobot_tugas) + (uts * bobot_uts) + (uas * bobot_uas)
    return round(nilai_akhir, 2)

# --- Proses Input Data (Looping) ---
print("====================================")
print("     SISTEM INPUT NILAI PRAKTIKUM   ")
print("====================================")

while True:
    # Simbol Proses (Input Data)
    print("\n--- Input Data Mahasiswa Baru ---")
    
    # Input Nama
    nama = input("Masukkan Nama Mahasiswa: ")
    
    # Input Nilai (Pastikan input adalah angka)
    try:
        nilai_tugas = float(input("Masukkan Nilai Tugas (0-100): "))
        nilai_uts = float(input("Masukkan Nilai UTS (0-100): "))
        nilai_uas = float(input("Masukkan Nilai UAS (0-100): "))
    except ValueError:
        print(" Kesalahan: Nilai harus berupa angka.")
        continue # Lanjut ke iterasi berikutnya
        
    # Hitung nilai akhir saat data dimasukkan
    nilai_akhir = hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas)

    # Simpan data ke dalam list sebagai dictionary
    data_mahasiswa.append({
        'Nama': nama,
        'Tugas': nilai_tugas,
        'UTS': nilai_uts,
        'UAS': nilai_uas,
        'Nilai Akhir': nilai_akhir
    })
    
    # Simbol Keputusan (Tambah data lagi?)
    tambah_lagi = input("\nTambah data mahasiswa lagi? (y/t): ").lower()
    
    if tambah_lagi == 't':
        # Keluar dari loop jika pengguna memilih 't'
        break 

# --- Proses Menampilkan Daftar Data ---
print("\n====================================")
print("       DAFTAR NILAI AKHIR MAHASISWA   ")
print("====================================")

if not data_mahasiswa:
    # Kasus jika tidak ada data yang dimasukkan
    print("Tidak ada data mahasiswa yang direkam.")
else:
    # Tampilkan Header Tabel
    print(f"{'No.':<4} | {'Nama':<20} | {'Tugas':<6} | {'UTS':<5} | {'UAS':<5} | {'Nilai Akhir':<12}")
    print("-" * 62)
    
    # Tampilkan Data setiap mahasiswa
    for i, data in enumerate(data_mahasiswa):
        print(
            f"{i+1:<4} | {data['Nama']:<20} | {data['Tugas']:<6.1f} | {data['UTS']:<5.1f} | {data['UAS']:<5.1f} | {data['Nilai Akhir']:<12.2f}"
        )

# --- Selesai ---
print("\n====================================")
print("           PROGRAM SELESAI          ")
print("====================================")
