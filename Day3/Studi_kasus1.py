# Muhammmad Fahmi Dzikry
# 2601658

buah = ['apel', 'jeruk', 'ceri', 'jeruk', 'apel', 'mangga']

buah[2] = 'cherry'

nambah_buah = input('masukan nama buah :')
urutan_buah = int(input('masukan urutan :'))

buah.insert(urutan_buah, nambah_buah)

buah.sort()

print(f'hasil akhir : {buah}')