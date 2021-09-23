import cv2
import numpy as np

cap = cv2.VideoCapture('videos/Safety Cone Placement.mp4')

while True:
    success, img = cap.read()
    cv2.imshow('Result', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break