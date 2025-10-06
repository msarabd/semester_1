tuple_angka = ((1, 5, 9), (2, 4, 8), (10, 20, 30), (4, 4, 4), (1, 2, 3))
print("Tuple angka =", tuple_angka)

for i in tuple_angka:
    jumlah = sum(i)
    if jumlah % 3 != 0:
        print(f"jumlah = {jumlah} >> pada tuple ke {i}")
        print(f"(Tuple {i} tidak habis dibagi 3) \n")
        kunci_tuple = i
        print("Maka, kode mesin =", kunci_tuple)
        break

print("(Batman memasukkan kode, lalu pintu terbuka) \n")
print("'SELAMAT DATANG, DETEKTIF'")
print("(Robin bergumam dengan nada mencekam) \n")
print("'AKU SEBENARNYA MENYEMBUNYIKAN BEBERAPA EASTER EGG SELAMA PENEYELIDIKAN KITA' \n'AKU BOSAN HANYA MENJADI PEMBANTUMU' \n'AKULAH THE NEW RIDDLER' \n")
print("||GAME OVER||")
