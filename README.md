# Attendance-tracker
This repositry contains an attendance tracking system which tracks faces and marks attendance of the recognized person in an excel sheet.

We have tried and used various implementations such as the face-recognition library, CNN implementation and VGG-16 models to obtain results.
We created a custom dataset of 1000 images which classified the images into 3 classes. After the image acquisiton process, the images were segmented to detect just the faces and then enhanced using haarcascade technique. 
After the preprocessing steps, the CNN model was trained to extract features from the images. 
We also tried using the pre-trained VGG-16 model, however a better accuracy was acheived on the CNN model.
A flow of the project:
![image](https://github.com/ankitd29/Attendance-tracker/assets/136194305/43eb7fc6-40f7-4bc5-a921-a286aa2581c6)


## Model Results

The model gave a training accuracy of 97% and a validation accuracy of 89 %
![image](https://github.com/ankitd29/Attendance-tracker/assets/136194305/6bd9f3cd-fac9-46eb-8a8b-975ddf0599df)
![image](https://github.com/ankitd29/Attendance-tracker/assets/136194305/b505c37b-726b-460b-8fab-8f57d09614d4)

## References

[An approach for Face Detection and Face Recognition using OpenCV and Face Recognition Libraries in Python](https://ieeexplore.ieee.org/document/10113066)  
[A New Deep Neural Architecture Search Pipeline for Face Recognition](https://ieeexplore.ieee.org/document/9091879)
