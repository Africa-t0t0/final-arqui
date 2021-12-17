
from flask import Flask, request, send_file, redirect, render_template, send_from_directory
from PIL import ImageFilter, Image
import base64, requests, os, time
from io import BytesIO
from werkzeug.wrappers import response
app = Flask(__name__)


DOWNLOAD_DIRECTORY = "./"

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
    elif filter == 'edge_enhance_more':
        new = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    elif filter == 'emboss':
        new = img.filter(ImageFilter.EMBOSS)
    new = new.save('new.jpg')
    new = open('new.jpg', 'rb')
    url = 'http://localhost:5000/recive'
    payload = {'name': name, 'filter': filter}
    files = {'image': new}
    headers = {}
    response = requests.request("POST", url, data = payload, files = files)
    # img.close()
    new.close()
    return send_from_directory(DOWNLOAD_DIRECTORY, path='new.jpg', as_attachment=True)


if __name__ == '__main__':
    app.run(host = '0.0.0.0' ,debug=True, port=5001)