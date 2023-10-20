import cv2 
import mediapipe as mp

# inicializar o opencv e o mediapipe
webcam = cv2.VideoCapture(1)
facedetect = mp.solutions.face_detection
recognizer = facedetect.FaceDetection()
design = mp.solutions.drawing_utils

while True: 
    # ESC para o loop
    verify, frame = webcam.read()

    if not verify:
        break

    facelist = recognizer.process(frame)

    if facelist.detections: 
        for face in facelist.detections:
            #desenhar os rostos
            design.draw_detection(frame, face)
    cv2.imshow("faces at webcam", frame)

    if cv2.waitKey(5) == 27:
        break

webcam.release()
