from deepface import DeepFace
from flask import Flask, render_template, Response, jsonify, request
import os
import base64;
import math;


app = Flask(__name__)

@app.route('/music')
def music():
    return render_template('musicpage.html', emotions=emotions, dominant_emotion=dominant_emotion)

@app.route('/')
def index():
    return render_template('page1.html')

@app.route('/detection')
def detect():
    return render_template('page2.html')
                            
@app.route('/analyse')
def analyse():
    global emotions, dominant_emotion
    objs = DeepFace.analyze(img_path = "./static/images/photo.jpeg", actions = ['emotion'])
    emotions_dict = objs[0].get('emotion')
    new_list = []
    for key, val in emotions_dict.items(): 
        new_list.append([key, int(math.floor(val))]) 
    emotions = new_list
    dominant_emotion = objs[0].get('dominant_emotion')
    print(objs)
    return render_template('musicpage.html', emotions=emotions, dominant_emotion=dominant_emotion)


@app.route('/photo_cap', methods=['POST'])
def photo_cap():
    request_data = request.get_json()
    photo_base64 = request_data['photo_cap']
    binary_data = base64.b64decode(str(photo_base64))
    image_name = "photo.jpeg"

    with open(os.path.join(app.root_path,"static/images",image_name), "wb") as f:
        f.write(binary_data)
    
    response = 'face detected'

    return response

if __name__ == '__main__':
    app.debug = True
    app.run(debug=False)