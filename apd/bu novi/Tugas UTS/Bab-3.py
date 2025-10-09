tuple_angka = ((1, 5, 9), (2, 4, 8), (10, 20, 30), (4, 4, 4), (1, 2, 3))
print("Tuple angka =", tuple_angka)

for a in tuple_angka:
    jumlah = sum(a)
    if jumlah % 3 != 0:
        print(f"jumlah = {jumlah} >> pada tuple ke {a} \n")
        print(f"R : Tuple {a} tidak habis dibagi 3. \n")
        kunci_tuple = a
        print(f"B : Maka, kode mesin = {kunci_tuple}.")
        break

print("(Batman memasukkan kode, lalu pintu terbuka) \n")
print("R : SELAMAT DATANG, DETEKTIF....")
print("(Robin bergumam dengan nada mencekam) \n")
print("R : AKU SEBENARNYA MENYEMBUNYIKAN BEBERAPA EASTER EGG SELAMA PENYELIDIKAN KITA, TERUTAMA UNTUK KODE ANGKA GANJIL SEBELUMNYA (SEHARUSNYA KODENYA 97352). \nR : AKU BOSAN HANYA MENJADI PEMBANTUMU. \nR : AKULAH.... THE NEW RIDDLER.")
print("(Plot twist, ternyata Robin adalah The Riddler)\n")
print("||GAME OVER||")