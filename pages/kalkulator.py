# Definisikan fungsi untuk melakukan operasi aritmatika kita akan membuat dengan python
def operasi_aritmatika(operasi, angka1, angka2):
    if operasi == '+':
        return angka1 + angka2
    elif operasi == '-':
        return angka1 - angka2
    elif operasi == '*':
        return angka1 * angka2
    elif operasi == '/':
        return angka1 / angka2
    else:
        raise ValueError("Operasi tidak valid")
# Minta pengguna memasukan operasi dan dua angka
operasi = input('Masukan operasi (+, -, *, /) : ')
angka1 = int(input('Masukan angka pertama : '))
angka2 = int(input('Masukan angka kedua : '))

# Lakukan operasi aritmatika dan cetak hasilnya
hasil = operasi_aritmatika(operasi, angka1, angka2)
print('Hasilnya adalah: ', hasil)
