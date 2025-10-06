angka = 13579
print("Kode rahasia hari ini >> ", angka)

if angka % 2 == 1:
    warna = "BIRU"
    print(f"{angka} adalah bilangan ganjil, tekan tombol {warna}")
else:
    warna = "MERAH"
    print(f"{angka} adalah bilangan ganjil, tekan tombol {warna}")

print(f"(Batman menekan tombol {warna})")
print(f"(Laser mati, pintu baja terbuka) \n")

list_barang = ["Lampu", "Kotak masuk", "Obor emas", "Peta kuno", "Gembok tua"]
print("List barang = ", list_barang)

barang_ambil = set()
for i in list_barang:
    if i.lower().count("o") >= 1 and i.lower().count("m") >= 1:
        barang_ambil.add(i)

print(f"(Batman mengambil = {barang_ambil})")
print("(Lantai bergetar dan sebuah lubang tersembunyi terbuka)")