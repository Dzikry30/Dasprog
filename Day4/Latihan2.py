# Nama : Muhahammad Fahmi Dzikry
# Nim  : 2601658

student = {
    "Alice": "Computer Science",
    "Bob": "Mathematics",
    "Charlie": "Physics",
    "David": "Computer Science",
    "Eva": "Mathematics"
}

prodi_count = {}

for jurusan in student.values():
    j_lower = jurusan.lower()

    if j_lower in prodi_count:
        prodi_count[j_lower] += 1
    else:
        prodi_count[j_lower] = 1

for jurusan, jumlah in prodi_count.items():
    print(f"prodi {jurusan} sebanyak {jumlah}")
