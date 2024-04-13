from deepface import DeepFace

objs = DeepFace.analyze(img_path = "./static/photo.jpg", 
        actions = ['emotion']
    )
print(objs)