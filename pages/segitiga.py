# kita akan menghitung luas segitiga
def luas_segitiga(alas, tinggi):
    return alas * tinggi /2
alas = float(input("Masukan Alas segitiga: "))
tinggi = float(input("Masukan TInggi segitiga: "))

# cetak luas segitiga
print ("Luas segitiga adalah", luas_segitiga(alas, tinggi))