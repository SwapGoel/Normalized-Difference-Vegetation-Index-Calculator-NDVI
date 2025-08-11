from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from sat_intel import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_and_process():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    file_path = os.path.join('uploads', filename)
    uploaded_file.save(file_path)
    save_ndvi(file_path)
    return render_template('results.html', image_url='static/ndvi_result.png')

if __name__ == '__main__':
    app.run()