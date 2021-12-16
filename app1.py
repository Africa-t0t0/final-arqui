
from flask import Flask, request, send_file
from PIL import ImageFilter, Image
import base64, requests
from werkzeug.wrappers import response
app = Flask(__name__)


@app.route('/recive', methods=['POST'])
def recive():
    name = request.form['name']
    image = request.files['image']
    filter = request.form['filter']
    url = 'http://localhost:5001/recive'
    payload = {'name': name, 'filter': filter}
    files = {'image': image}
    headers = {}
    response = requests.request("POST", url, data = payload, files = files)
    return response.text

if __name__ == '__main__':
    app.run(debug=True, port=5000)