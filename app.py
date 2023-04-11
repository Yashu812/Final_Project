from flask import Flask, flash, request, redirect, url_for, render_template
import urllib.request
import os
from werkzeug.utils import secure_filename
import json

app = Flask(__name__)

UPLOAD_FOLDER = 'static/images/uploads/'

app.secret_key = "yashashree"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/women')
def women():
    return render_template('women.html')

@app.route('/upload', methods=['POST', 'GET'])
def upload_image():
    if 'file1' not in request.files or 'file3' not in request.files:
        flash('No file part', 'missing')
        return redirect(request.url)
    file1 = request.files['file1']
    file3 = request.files['file3']

    if file1.filename == '' or file3.filename == '':
        flash('No image selected for uploading', 'empty')
        return redirect(request.url)

    if file1 and allowed_file(file1.filename):
        filename1 = secure_filename(file1.filename)
        file1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename1))
        # print('upload_image filename: ' + filename)
        # flash('Image successfully uploaded','success')
    if file3 and allowed_file(file3.filename):
        filename3 = secure_filename(file3.filename)
        file3.save(os.path.join(app.config['UPLOAD_FOLDER'], filename3))
        flash('Image successfully uploaded', 'success')
        return redirect(url_for('women'))
    else:
        flash('Allowed image types are - png, jpg, jpeg')
        return redirect(request.url)

@app.route('/guidelines')
def guidelines():
    return render_template('guidelines.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(port=8000, debug=True)
