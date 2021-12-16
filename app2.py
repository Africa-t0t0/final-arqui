
from flask import Flask, request, send_file
from PIL import ImageFilter, Image
import base64, requests, psycopg2, os
from werkzeug.wrappers import response
app = Flask(__name__)

# HOST = os.environ.get('HOST')
# PORT = os.environ.get('PORT')
# DATABASE = os.environ.get('DATABASE')
# USER = os.environ.get('USER')
# PASSWORD = os.environ.get('PASSWORD')
HOST = "192.168.0.10"
PORT = "5432"
DATABASE = "examen"
USER = "admin"
PASSWORD = "admin"


@app.route('/recive', methods=['POST'])
def recive():
    name = request.form['name']
    image = request.files['image']
    filter = request.form['filter']
    img = Image.open(image)
    if filter == 'blur':
        new = img.filter(ImageFilter.BLUR)
    elif filter == 'smooth':
        new = img.filter(ImageFilter.SMOOTH)
    elif filter == 'detail':
        new = img.filter(ImageFilter.DETAIL)
    elif filter == 'sharpen':
        new = img.filter(ImageFilter.SHARPEN)
    elif filter == 'contour':
        new = img.filter(ImageFilter.CONTOUR)
    elif filter == 'edge_enhance':
        new = img.filter(ImageFilter.EDGE_ENHANCE)
    new = new.save('new.jpg')
    new = open('new.jpg', 'rb')
    url = 'http://localhost:5000/recive'
    payload = {'name': name, 'filter': filter}
    files = {'image': new}
    headers = {}
    response = requests.request("POST", url, data = payload, files = files)
    new.close()
    return 'enviado desde 2'


if __name__ == '__main__':
    app.run(debug=True, port=5001)