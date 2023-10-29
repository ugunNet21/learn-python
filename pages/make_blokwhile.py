# membuat pengulangan blok bersarang menggunakan while
baris = 5
i =1
while i <= baris:
    j = 1
    while j<= i:
        print("%d" % (i * j), end=" ")
        j += 1
        print()
        i += 1