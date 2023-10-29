# membuat kelas segi empat di dalam python
class SegiEmpat:
    def __init__(self, p, l):
        self.panjang = p
        self.lebar = l

        # membuat objek dari kelas segiempat dengan panjang dan lebar yang sudah dis
        def luas(self) ->int:
            return self.panjang * self.lebar

        def keliling(self) ->int:
            return 4 * (self.panjang + self.lebar)

        print("Luas adalah :"  % luas)
        print("Keliling adalah :" % keliling)

        # menambahkan fungsi keliling
        def keliling(self):
            keliling = 4 * (self.panjang + self.lebar)
            print("Luas adalah :", keliling)

        obj_segiempat = SegiEmpat(10, 5)
        obj_segiempat.luas()
        obj_segiempat.keliling()
