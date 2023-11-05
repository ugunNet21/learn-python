def operasi_bilangan(operasi, angka1, angka2):
    if operasi == "tambah":
        return angka1 + angka2
    elif operasi == "kurang":
        return angka1 - angka2
    elif operasi == "kali":
        return angka1 * angka2
    else:
        return "Operasi tidak valid"

# Minta pengguna memasukan operasi dan angka
print("Mohon masukkan operasi (tambah/kurang/kali) dan dua bilangan: ")
operasi = input()
bilangan1 = int(input("Masukan angka ke-1 : "))
bilangan2 = int(input("Masukan angka ke-2 : "))
hasil = operasi_bilangan(operasi, bilangan1, bilangan2)
print(f"Hasil dari {bilangan1} {operasi} {bilangan2} adalah {hasil}")