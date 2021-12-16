
from flask import Flask, request, send_file
from PIL import ImageFilter, Image
import base64, requests
app = Flask(__name__)

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
    new.show()
    return send_file(new, mimetype='image/jpeg')


if __name__ == '__main__':
    app.run(debug=True, port=5001)