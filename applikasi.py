import Hitung 
import LuasBangunDatar as bangundatar 
from LuasBangunRuang import kubus
from LuasBangunRuang import balok
from LuasBangunRuang import tabung 
from LuasBangunRuang import limas
from LuasBangunRuang import prisma 
# Modul Hitung
print('=========== Modul Hitung ==========')
Hitung.tambah(20,20)
Hitung.kurang(30,20)
Hitung.kali(40,8)
Hitung.bagi(30,6)
Hitung.pangkat(10,2)

print('=========== Modul Luas Bangun Datar ==========')
# Modul Luas bangun datar
bangundatar.lingkaran(20)
bangundatar.persegi(6)
bangundatar.jajargenjang(12,6)
bangundatar.persegi_panjang(20,5)
bangundatar.segitiga(30,5)

print('=========== Modul Luas Bangun Ruang ==========')
# Modul Luas bangun ruang
kubus(2)
balok(2,4,6)
tabung(8,4)
limas(4,8)
prisma(8,4)