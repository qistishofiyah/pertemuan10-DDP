# Membuat Modul Hitung
import math 

def tambah(bilangan1,bilangan2):
    hasil = bilangan1 + bilangan2 
    print(f'Hasil dari {bilangan1} + {bilangan2} = {hasil}')

def kurang(bilangan1,bilangan2):
    hasil = bilangan1 - bilangan2 
    print(f'Hasil dari {bilangan1} - {bilangan2} = {hasil}')

def kali(bilangan1,bilangan2):
    hasil = bilangan1 * bilangan2 
    print(f'Hasil dari {bilangan1} * {bilangan2} = {hasil}')

def bagi(bilangan1,bilangan2):
    hasil = bilangan1 / bilangan2 
    print(f'Hasil dari {bilangan1} / {bilangan2} = {hasil}')

def pangkat(bilangan1,bilangan2):
    hasil = math.pow(bilangan1,bilangan2) 
    print(f'Hasil dari {bilangan1} ^ {bilangan2} = {hasil}')

