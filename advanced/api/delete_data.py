import requests

# URL api Delete
url = "https://dummyjson.com/products/1"

# kirim permintaan delete
response = requests.delete(url)

# cek status kode response 200
if response.status_code == 200:
    print("Data berhasil dihapus")
else:
    print("Gagal menghapus data, periksa koneksi dan url yang anda gunakan", response.status_code)