# contoh pengunaan eksepsi dengan python# Contoh penanganan eksepsi dengan Python

# Contoh penanganan eksepsi dengan Python

def main():
  # Kode yang mungkin menghasilkan eksepsi
  try:
    a = 1 / 0
  except ZeroDivisionError:
    # Kode yang akan dijalankan jika terjadi eksepsi ZeroDivisionError
    print("Terjadi pembagian dengan nol")
  else:
    # Kode yang akan dijalankan jika blok try tidak menghasilkan eksepsi
    print("Tidak ada eksepsi")
  finally:
    # Kode yang akan dijalankan dalam semua kasus
    print("Berakhir")

if __name__ == "__main__":
  main()
