from deepface import DeepFace
from flask import Flask, render_template, Response, jsonify, request
import os
import base64;


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('page1.html')

@app.route('/detection')
def detect():
    return render_template('page2.html')
                            
@app.route('/analyse')
def analyse():
    objs = DeepFace.analyze(img_path = "./static/images/photo.jpg", actions = ['emotion'])
    print(objs)
    return objs


@app.route('/photo_cap', methods=['POST'])
def photo_cap():
    request_data = request.get_json()
    photo_base64 = request_data['photo_cap']
    binary_data = base64.b64decode(str(photo_base64))
    image_name = "photo.jpeg"

    with open(os.path.join(app.root_path,"static/images",image_name), "wb") as f:
        f.write(binary_data)
    
    response = 'your response'

    return response

if __name__ == '__main__':
    app.debug = True
    app.run(debug=False)