# 1. Leni ingin sekali mengetahui deret angka dari 1 sampai 50 dimana
# ketika bertemu dengan kelipatan 5 maka outputnya adalah“pass”. 
# Tolong bantu Leni dengan masalahnya kali ini.

for i in range(1, 51):
    if i % 5 == 0:
        print("pass")
    else:
        print(i)


# 2. Buat program yang dapat menginputkan sejumlah n untuk diisi nama-nama hewan,
# kemudian mencetak kembali hewan yang telah diinputkan tersebut

n = int(input("Masukkan jumlah hewan yang ingin diinputkan: "))
hewan = []
for i in range(n):
    nama_hewan = input(f"Masukkan nama hewan ke-{i + 1}: ")
    hewan.append(nama_hewan)

print("Hewan yang telah diinputkan:")
for h in hewan:
    print(h)


# 3. Buat program yang meminta user memasukkan n bilangan, lalu tampilkan mana 
# saja bilangan genap dan mana yang ganjil

n = int(input("Masukkan jumlah bilangan yang ingin diinputkan: "))
bilangan = []
for i in range(n):
    num = int(input(f"Masukkan bilangan ke-{i + 1}: "))
    bilangan.append(num)

print("Bilangan genap:")
for b in bilangan:
    if b % 2 == 0:
        print(b)

print("Bilangan ganjil:")
for b in bilangan:
    if b % 2 != 0:
        print(b)


# 4. Tampilkan deret angka dari 1 sampai 80 dimana yang ditampilkan
# hanya yang kelipatan 3 dan 5 saja

for i in range(1, 81):
    if i % 3 == 0 and i % 5 == 0:
        print(i)


# 5. Buat sistem login sederhana, tidak ada batas salah 
# username/password.
# Username: dasproRPL
# Password: RPLfire!123

while True:
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username == "dasproRPL" and password == "RPLfire!123":
        print("Login berhasil!")
        break