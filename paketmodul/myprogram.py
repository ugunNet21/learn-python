# memembuat modul dengan mengimport modul
import mymodule
def main():
    print("Nilai A = %d" % mymodule.A)
    print(" 2 + 3 = %d " % mymodule.tambah(2,3))
    print(" 2 * 3 = %d " % mymodule.kali(2,3))
    if __name__ == '__main__':
        main()