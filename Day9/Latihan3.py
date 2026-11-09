def hitung_selisih_waktu(jam_mulai, menit_mulai, detik_mulai, jam_selesai, menit_selesai, detik_selesai):
    # Konversi waktu mulai dan selesai ke total detik
    total_detik_mulai = (jam_mulai * 3600) + (menit_mulai * 60) + detik_mulai
    total_detik_selesai = (jam_selesai * 3600) + (menit_selesai * 60) + detik_selesai
    
    selisih_detik = total_detik_selesai - total_detik_mulai
    
    jam = selisih_detik // 3600
    sisa_detik = selisih_detik % 3600
    menit = sisa_detik // 60
    detik = sisa_detik % 60
    
    print(f"Output: {jam} jam - {menit} menit - {detik} detik")


hitung_selisih_waktu(8, 10, 20, 9, 15, 30)