# memberikan jeda wkatu menggunakan for
import time
baris =5
kolom =3
for i in range(1, baris+1):
    print("Ketika i=%d:" % i, end=" ")
    for j in range(1, kolom+1):
        print("[baris %d, kolom %d]" % (i,j), end=" ")
        time.sleep(1)
    print()