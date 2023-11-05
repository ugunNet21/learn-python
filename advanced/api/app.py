from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    url = "https://dummyjson.com/products/1"
    response = requests.get(url)
    data = response.json()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)