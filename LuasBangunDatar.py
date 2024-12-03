# Membuat Modul Untuk Menghitung Luas Bangun Datar

def lingkaran(jari2):
    phi = 3.14
    hitung = phi*jari2**2
    print(f'Hasil Dari luas lingkaran {jari2} = {hitung}')
lingkaran(20)

def persegi(sisi):
    hitung = sisi * sisi
    print(f'Hasil Dari luas persegi {sisi} * {sisi} = {hitung}')
persegi(6)

def jajargenjang(alas,tinggi):
    hitung = alas * tinggi
    print(f'Hasil Dari luas jajargenjang {alas} * {tinggi} = {hitung}')
jajargenjang(12,6)

def persegi_panjang(panjang,lebar):
    hitung = panjang * lebar
    print(f'Hasil Dari luas persegi panjang {panjang} * {lebar} = {hitung}')
persegi_panjang(20,5)

def segitiga(alas,tinggi):
    hitung = 1/2 * alas * tinggi
    print(f'Hasil dari luas segitiga {1/2} * {alas} * {tinggi} = {hitung}')
segitiga(30,5)