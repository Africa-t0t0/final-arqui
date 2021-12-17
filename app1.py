
from flask import Flask, request, send_file, render_template, send_from_directory
from PIL import ImageFilter, Image
import base64, requests, io, psycopg2, os
from werkzeug.wrappers import response
app = Flask(__name__)

# HOST = os.environ.get('HOST')
# PORT = os.environ.get('PORT')
# DATABASE = os.environ.get('DATABASE')
# USER = os.environ.get('USER')
# PASSWORD = os.environ.get('PASSWORD')
HOST = "192.168.1.87"
PORT = "5432"
DATABASE = "examen"
USER = "admin"
PASSWORD = "admin"

DOWNLOAD_DIRECTORY = "./"

@app.route('/send', methods=['POST'])
def send():
    name = request.form['name']
    image = request.files['image']
    filter = request.form['filter']
    url = 'http://localhost:5001/recive'
    payload = {'name': name, 'filter': filter}
    files = {'image': image}
    headers = {}
    response = requests.request("POST", url, data = payload, files = files)
    return send_from_directory(DOWNLOAD_DIRECTORY, path='new.jpg', as_attachment=True)

@app.route('/recive', methods=['POST'])
def recive():
    name = request.form['name']
    image = request.files['image']
    filter = request.form['filter']
    img = Image.open(image)
    img = img.save('new.jpg')
    conn = psycopg2.connect(
            host= HOST,                    
            port= PORT,
            database= DATABASE,
            user= USER,
            password=PASSWORD)
    cur = conn.cursor()
    query1 = """CREATE TABLE IF NOT EXISTS imagenes (
        id SERIAL PRIMARY KEY,
        name VARCHAR,
        filter VARCHAR,
        created DATE DEFAULT CURRENT_DATE)"""
    cur.execute(query1)
    conn.commit()
    query2 = """INSERT INTO imagenes (name, filter) VALUES (%s, %s);"""
    values = (name, filter,)
    cur.execute(query2, values)
    conn.commit()
    

    return ''



if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True, port=5000)