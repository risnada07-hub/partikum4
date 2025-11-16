def hitung_nilai_akhir(tugas, uts, uas):
    """
    Menghitung nilai akhir berdasarkan bobot: Tugas (30%), UTS (35%), UAS (35%).
    """
    bobot_tugas = 0.30
    bobot_uts = 0.35
    bobot_uas = 0.35
    
    nilai_akhir = (tugas * bobot_tugas) + (uts * bobot_uts) + (uas * bobot_uas)
    return round(nilai_akhir, 2)

def tambah_data_nilai():
    """
    Fungsi utama untuk menambahkan data mahasiswa dan menghitung nilai akhir.
    """
    data_mahasiswa = []
    
    print("=== Program Input Nilai Mahasiswa ===")
    
    while True:
        # Meminta input data
        print("\nMasukkan data mahasiswa:")
        nama = input("Nama Mahasiswa: ")
        
        # Memastikan input nilai adalah angka
        try:
            nilai_tugas = float(input("Nilai Tugas (0-100): "))
            nilai_uts = float(input("Nilai UTS (0-100): "))
            nilai_uas = float(input("Nilai UAS (0-100): "))
        except ValueError:
            print("**Input nilai tidak valid. Harap masukkan angka.**")
            continue # Lanjut ke iterasi berikutnya
            
        # Hitung Nilai Akhir
        nilai_akhir = hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas)
        
        # Simpan data ke dalam list
        data_mahasiswa.append({
            'Nama': nama,
            'Tugas': nilai_tugas,
            'UTS': nilai_uts,
            'UAS': nilai_uas,
            'Nilai Akhir': nilai_akhir
        })
        
        # Tampilkan pertanyaan untuk menambah data (y/t?)
        tambah_lagi = input("\nTambah data lagi (y/t)? ").strip().lower()
        
        if tambah_lagi == 't':
            break # Keluar dari perulangan jika jawaban 't' (Tidak)
        elif tambah_lagi != 'y':
            print("Pilihan tidak dikenal. Asumsi 'y' (Ya).")
            
    # Tampilkan daftar data
    print("\n" + "="*40)
    print("           DAFTAR NILAI MAHASISWA")
    print("="*40)
    
    if data_mahasiswa:
        # Menampilkan header tabel
        print(f"| {'No':<3} | {'Nama':<15} | {'Tugas':<5} | {'UTS':<5} | {'UAS':<5} | {'Akhir':<5} |")
        print("-" * 40)
        
        # Menampilkan data per mahasiswa
        for i, data in enumerate(data_mahasiswa, 1):
            print(f"| {i:<3} | {data['Nama']:<15} | {data['Tugas']:<5.1f} | {data['UTS']:<5.1f} | {data['UAS']:<5.1f} | {data['Nilai Akhir']:<5.1f} |")
        print("-" * 40)
    else:
        print("Tidak ada data mahasiswa yang dimasukkan.")

if __name__ == "__main__":
    tambah_data_nilai()