def menu_login():
    password_benar = "Latihan"
    kesempatan = 3
    
    while kesempatan > 0:
        password_input = input("Masukkan password: ")
        
        if password_input == password_benar:
            print("Login Berhasil! Selamat datang di Lab Komputer.")
            return
        else:
            kesempatan -= 1
            print(f"Password salah! Sisa kesempatan: {kesempatan}")
            
    print("\nAkses ditolak. Anda telah salah memasukkan password sebanyak 3 kali dan keluar dari sistem.")

menu_login()