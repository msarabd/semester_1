angka = 23579
print("Kode rahasia hari ini >>", angka)
print(f"\nB : Apakah {angka} adalah angka ganjil? (Y:BIRU, T:MERAH)")

if angka % 2 == 1:
    warna = "BIRU"
    print(f"R : {angka} adalah bilangan ganjil, tekan tombol {warna}.")
    print(f"(Batman menekan tombol {warna})")
    print(f"(Laser mati, pintu baja kiri terbuka) \n")
    list_barang = ["Lampu", "Kotak masuk", "Obor emas", "Peta kuno", "Gembok tua"]
    print("List barang =", list_barang)

    barang_ambil = set()
    for i in list_barang:
        if i.lower().count("o") >= 1 and i.lower().count("m") >= 1:
            barang_ambil.add(i)

    print(f"\n(Batman mengambil = {barang_ambil})")
    print("(Lantai bergetar dan sebuah lubang tersembunyi terbuka)")

else:
    warna = "MERAH"
    print(f"R : {angka} bukan bilangan ganjil, tekan tombol {warna}.")
    print(f"(Batman menekan tombol {warna})")
    print(f"(Laser mati, pintu baja kanan terbuka) \n")
    print("(Batman menemukan Riddler)")