# Membuat Modul Untuk Menghitung Luas Bangun Ruang

def kubus(rusuk):
    hasil = rusuk * rusuk * rusuk
    print(f'Hasil Dari luas volume kubus {rusuk} = {hasil}')

def balok(panjang,lebar,tinggi):
    hasil = panjang * lebar * tinggi
    print(f'Hasil Dari luas volume balok {panjang} * {lebar} * {tinggi} = {hasil}')

def tabung(jari2,tinggi):
    phi = 3.14
    hasil = phi*jari2*tinggi
    print(f'Hasil Dari luas volume tabung {phi} * {jari2} * {tinggi} = {hasil}')

def limas(alas,tinggi):
    hasil = 1/3 * alas * tinggi
    print(f'Hasil Dari luas volume limas {1/3} * {alas} * {tinggi} = {hasil}')

def prisma(alas,tinggi):
    hasil = 1/3 * alas * tinggi
    print(f'Hasil Dari luas volume prisma {1/3} * {alas} * {tinggi} = {hasil}')