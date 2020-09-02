import cv2
print("hello world")
cap=cv2.VideoCapture(0)
label=input("Enter name:")
num=input("Enter number of photos to be taken:") or 10
num=int(num)
while True:
    ret,frame=cap.read()

    if not ret:
        continue

    cascade_classifier=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces=cascade_classifier.detectMultiScale(frame,1.3,5)

    faces=sorted(faces,key=lambda e:e[2]*e[3],reverse=True)

    if not faces:
        continue
    
    faces=[faces[0]]

    print(len(faces))
    for face in faces:
        x,y,w,h=face

        cropped_face=frame[y:y+h,x:x+w]
        print(cropped_face.shape)
        cropped_face=cv2.resize(cropped_face,(100,100))
        print(cropped_face.shape)
        
#   print(frame.shape)
    cv2.imshow("Feed",frame)
    if cv2.waitKey(1)&0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
