from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)
# api url
api_url = "https://dummyjson.com/products/"


@app.route("/")
def index():
    response = requests.get(api_url)
    data = response.json()
    return render_template("index.html", data=data)


@app.route("/add_product", methods=["POST"])
def add_product():
    # mendapatkan data yang dikirm dalam permintaan POST
    new_product_data = request.form

    # kirim data ke API dengan metode POST
    response = requests.post(api_url, data=new_product_data)
    if response.status_code == 201:
        return jsonify({"message": "Produk berhasil ditambahkan"})
    else:
        response_data = response.json()
        error_message = response_data.get("error")
        print("Pesan kesalahan:", error_message)
        return jsonify({"error": "Gagal menambahkan produk"})


# app untuk delete
@app.route("/delete_product", methods=["DELETE"])
def delete_product():
    # kirim permintaan delete ke API
    response = requests.delete(api_url)
    if response.status_code == 204:
        return jsonify({"message": "Produk berhasil dihapus!"})
    else:
        return jsonify({"error": "Gagal menghapus produk."})


if __name__ == "__main__":
    app.run(debug=True)
