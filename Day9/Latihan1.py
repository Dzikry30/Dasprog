def deret_fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

n = 10
print(f"Deret Fibonacci ({n} angka):", deret_fibonacci(n))

def volume_tabung(jari_jari, tinggi):
    phi = 3.14  
    vol = phi * (jari_jari ** 2) * tinggi
    return vol

r = 7
t = 10
print(f"Volume tabung dengan r={r} dan t={t} adalah: {volume_tabung(r, t)}")

def hitung_total_rata(*angka):
    total = sum(angka)
    jumlah_data = len(angka)
    if jumlah_data > 0:
        rata_rata = total / jumlah_data
    else:
        rata_rata = 0
        
    print(f"Input: {', '.join(map(str, angka))}")
    print(f"Total: {' + '.join(map(str, angka))} = {total}")
    print(f"Rata-rata = {total}/{jumlah_data} = {rata_rata}")

hitung_total_rata(2, 3, 5, 10)