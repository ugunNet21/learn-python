import requests

# URL API untuk perminataan POST
url = "https://dummyjson.com/products/1"

# data yang ingin untuk permintaan POST
data = {
    "name": "Product 2",
    "price": 50,
}

# Mengirim permintaan POST dengan data
response = requests.post(url, json=data)

# Memeriksa apakah permintaan berhasil dengan status kode 200
if response.status_code == 200:
    # Mendapatkan respons dari API
    response_data = response.json()
    # Menampilkan respons dari API
    print(response_data)
else:
    # Jika permintaan gagal maka mencetak error message
    print("Error: ", response.status_code)