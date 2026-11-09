# # soal 1
print('\n=== soal 1 ===')
x = 10

print('9') if x < 9 else print('8') if x < 8 else print('7') if x < 7 else print('6') if x < 6 else print('5') if x < 5 else print('4') if x > 4 else print('3') if x < 3 else print('2') if x < 2 else print('1')

# # soal 2
print('\n=== soal 2 ===')

nilai = float(input('masukan nilai anda: '))

if nilai < 0 or nilai > 100:
    print('nilai tidak walid')

elif nilai > 90:
    print('Nilai A')
    print('Keterangan : Sangat Baik')

elif nilai > 85:
    print('Nilai B+')
    print('Keterangan : Sangat Baik')

elif nilai > 80:
    print('Nilai B')
    print('Keterangan : Baik')

elif nilai > 70:
    print('Nilai C')
    print('Keterangan : Baik')

elif nilai > 60:
    print('Nilai D')
    print('Keterangan : Perlu Perbaikan')

else:
    print('Nilai E')
    print('Keterangan : Perlu Perbaikan')

# soal 3
print('\n=== Soal 3 ===')

umur = int(input("Masukkan umur: "))
jenis_kelamin = input("Masukkan jenis kelamin (pria/wanita): ").lower()
tinggi = float(input("Masukkan tinggi badan (cm): "))
iq = int(input("Masukkan IQ: "))

if umur >= 18 and umur <= 25 and iq >= 130:
    if jenis_kelamin == "wanita" and tinggi >= 170:
         print("Memenuhi kriteria model catwalk")

    elif jenis_kelamin == "pria" and tinggi >= 175:

        print("Memenuhi kriteria model catwalk")

    else:
         print("Tidak memenuhi kriteria model catwalk")

else:
    print("Tidak memenuhi kriteria model catwalk")


# soal 4
print('\n=== Soal 4 ===')
menu = ["Nasi Goreng", "Mie Goreng", "Ayam Geprek"]

makanan = input("Masukkan nama makanan: ")

if makanan in menu:
    print("Menu tersedia")
else:
    print("Menu tidak tersedia")