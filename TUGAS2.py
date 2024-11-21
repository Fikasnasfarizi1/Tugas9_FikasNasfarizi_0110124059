print('##nomor 2##')
def genap_ganjil(bilangan):
    hitung = bilangan % 2 == 0
    return hitung

angka = 4
hasil = genap_ganjil(angka)
print(f"bilangan {angka} bernilai {hasil}")
angka = 7
hasil = genap_ganjil(angka)
print(f"bilangan {angka} bernilai {hasil}")