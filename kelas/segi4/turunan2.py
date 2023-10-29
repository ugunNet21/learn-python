# membuat kelas segi empat di dalam python
class SegiEmpat:
  def __init__(self, p, l):
    self.panjang = p
    self.lebar = l

  def luas(self)->int:
    return (self.panjang * self.lebar)

  def keliling(self)->int:
    return 4 * (self.panjang + self.lebar)

  # menambahkan fungsi print()
  def keliling(self):
    keliling = 4 * (self.panjang + self.lebar)
    print("Luas adalah:", keliling)

obj_segiempat = SegiEmpat(10, 5)
obj_segiempat.keliling()

