from flask import Flask, flash, request, redirect, url_for, render_template
import urllib.request
import os
from werkzeug.utils import secure_filename
import json

app = Flask(__name__)

UPLOAD_FOLDER = 'static/images/uploads'

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

@app.route('/upload', methods=['POST'])
def upload():
    # Check if the request contains files
    if 'image1' not in request.files or 'image2' not in request.files:
        return 'No file(s) selected'

    # Get the files from the request
    image1 = request.files['image1']
    image2 = request.files['image2']

    # Save the images to the UPLOAD_FOLDER
    filename1 = secure_filename(image1.filename)
    filename2 = secure_filename(image2.filename)
    image1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename1))
    image2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename2))

    # Return a success message
    return 'Images uploaded successfully'


@app.route('/guidelines')
def guidelines():
    return render_template('guidelines.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
