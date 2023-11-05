import requests

# tentuka URL API
url = "https://dummyjson.com/products/1"

# mengirim permintaan GET ke URL
response = requests.get(url)

# memriksan apakah permintaan berhasil (kode status 200)
if response.status_code == 200:
    # Mengambil data dari json respons
    data  = response.json()
    # menampilkan data
    print(data)
else:
    # jika permintaan gagal mencetak pesan kesalahan
    print("Gagal mengambil data. Kode status :", response.status_code)