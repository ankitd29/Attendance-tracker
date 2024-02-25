from django.shortcuts import render, redirect
import cv2
import tensorflow as tf
import numpy as np

# Create your views here.
def index(request):
    context = {}
    return render(request, 'webcam/index.html', context)

def video(request):
    
    labels = {
        'Ankit Dighe': 0,
        'Neha Adhikari': 1,
        'Sanika Gadkari': 2
              }
    
    label = list(labels.keys())
    model = tf.keras.models.load_model(r'C:\Users\dell\FaceDetection\Cnn2.h5')

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    if face_cascade.empty():
        print("Error: Cascade Classifier not loaded!")

    cap = cv2.VideoCapture(0)

#    attendance_list = []

    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=8)
        print(len(faces))

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            face_crop = frame[y:y+h, x:x+w]
            image1 = cv2.resize(face_crop, (100, 100))
            image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
            image3 = image2.astype(np.float32)/255.0
            image4 = np.expand_dims(image3, axis = 0)
            output = model.predict(image4)
            predicted_class_index = output.argmax()
            

            predicted_student = label[predicted_class_index]
            #attendance_list.append(predicted_student)
            cl = max(output[0])
            str = f'{predicted_student} ({float(cl):.4f})'
            cv2.putText(frame, str, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
            #Object detection*, Object recognition*, wavelet transform, multi_range transform

        cv2.imshow('webcam', frame)
        if cv2.waitKey(1) & 0xFF == ord('x'):
            break

    cv2.destroyAllWindows()
    return redirect('webcam-index')