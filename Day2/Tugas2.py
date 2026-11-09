# A. Perhitungan Biaya Konsumsi
print("A. Perhitungan Biaya Konsumsi")
print("Harga satu paket konsumsi(Makan Siang dan Kudapan) Rp.35.000")

peserta_konsumsi = int(input("Masukan Jumlah Peserta : "))

harga_konsumsi = 35000
cadangan_konsumsi = peserta_konsumsi * 0.10
total_porsi = peserta_konsumsi + cadangan_konsumsi
biaya_konsumsi = total_porsi * harga_konsumsi

print(f"- Jumlah Konsumsi Yang Harus Disediakan, Termasuk Cadangan Adalah : {total_porsi} Porsi")
print(f"- Total Biayanya Adalah : Rp.{biaya_konsumsi:,.0f}".replace(",", "."))
print()

# B. Perhitungan Kebutuhan Cetak Sertifikat
print("B. Perhitungan Kebutuhan Cetak Sertifikat")

harga_rim = 65000
isi_per_rim = 500

peserta_sertifikat = int(input("Masukan Jumlah Peserta : "))

sertifikat_utama = peserta_sertifikat
cadangan_sertifikat = peserta_sertifikat * 0.05
total_kertas = sertifikat_utama + cadangan_sertifikat

kebutuhan_rim = total_kertas / isi_per_rim
biaya_sertifikat = kebutuhan_rim * harga_rim

print(f"- Jumlah Sertifikat Yang perlu Dicetak : {sertifikat_utama}")
print(f"- Jumlah Kertas Yang perlu Dicetak : {total_kertas}")
print(f"- Perkiraan Jumlah Rim Kertas Yang Diperlukan, Termasuk Cadangan : {kebutuhan_rim}")
print(f"- Total Biaya Pembelian Kertas Rp.{biaya_sertifikat:,.0f}".replace(",", "."))
print()

# C. Perhitungan Biaya Pendaftaran Peserta
print("C. Perhitungan Biaya Pendaftaran Peserta")
print(f"- Biaya Konsumsi : Rp.{biaya_konsumsi:,.0f}".replace(",", "."))
print(f"- Biaya Cetak Sertifikat : Rp.{biaya_sertifikat:,.0f}".replace(",", "."))

sewa_tempat = int(input("Masukan Biaya Sewa Tempat : Rp."))
dokumentasi = int(input("Masukan Biaya Dokumentasi : Rp."))

peserta_pendaftaran = int(input("Masukan Jumlah Peserta : "))
print()

total_operasional = biaya_konsumsi + biaya_sertifikat + sewa_tempat + dokumentasi
dana_darurat = total_operasional * 0.10

total_anggaran = total_operasional + dana_darurat

biaya_per_peserta = total_anggaran / peserta_pendaftaran

print(f"- Total Biaya Penyelenggaraan Acara : Rp.{total_operasional:,.0f}".replace(",", "."))
print(f"- Besar Dana Cadangan : Rp.{dana_darurat:,.0f}".replace(",", "."))
print(f"- Total Dana Yang Harus Dikumpulkan : Rp.{total_anggaran:,.0f}".replace(",", "."))
print(f"- Biaya Pendaftaran Peserta : Rp.{biaya_per_peserta:,.0f}".replace(",", "."))

a = input("Apakah Anda Ingin Mengulang Program? (y/n) : ")

loop = True
while loop:
    if a == "y":
        print()
        print("A. Perhitungan Biaya Konsumsi")
        print("Harga satu paket konsumsi(Makan Siang dan Kudapan) Rp.35.000")

        peserta_konsumsi = int(input("Masukan Jumlah Peserta : "))

        harga_konsumsi = 35000
        cadangan_konsumsi = peserta_konsumsi * 0.10
        total_porsi = peserta_konsumsi + cadangan_konsumsi
        biaya_konsumsi = total_porsi * harga_konsumsi

        print(f"- Jumlah Konsumsi Yang Harus Disediakan, Termasuk Cadangan Adalah : {total_porsi} Porsi")
        print(f"- Total Biayanya Adalah : Rp.{biaya_konsumsi:,.0f}".replace(",", "."))
        print()

        # B. Perhitungan Kebutuhan Cetak Sertifikat
        print("B. Perhitungan Kebutuhan Cetak Sertifikat")

        harga_rim = 65000
        isi_per_rim = 500

        peserta_sertifikat = int(input("Masukan Jumlah Peserta : "))

        sertifikat_utama = peserta_sertifikat
        cadangan_sertifikat = peserta_sertifikat * 0.05
        total_kertas = sertifikat_utama + cadangan_sertifikat

        kebutuhan_rim = total_kertas / isi_per_rim
        biaya_sertifikat = kebutuhan_rim * harga_rim

        print(f"- Jumlah Sertifikat Yang perlu Dicetak : {sertifikat_utama}")
        print(f"- Jumlah Kertas Yang perlu Dicetak : {total_kertas}")
        print(f"- Perkiraan Jumlah Rim Kertas Yang Diperlukan, Termasuk Cadangan : {kebutuhan_rim}")
        print(f"- Total Biaya Pembelian Kertas Rp.{biaya_sertifikat:,.0f}".replace(",", "."))
        print()
    