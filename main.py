import os

import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = FaceMeshDetector(maxFaces=2)

ids_list = [0, 17, 78, 292]
mouth_top = ids_list[0]
mouth_bottom = ids_list[1]
mouth_left = ids_list[2]
mouth_right = ids_list[3]

eatables_folder = "Objects/eatable"
non_eatables_folder = "Objects/noneatable"

eatables_list = os.listdir(eatables_folder)
non_eatables_list = os.listdir(non_eatables_folder)
eatables = []
non_eatables = []

for obj in eatables_list:
    print(obj)
    eatables.append(cv2.imread(f'{eatables_folder}/{obj}', cv2.IMREAD_UNCHANGED))

for obj in non_eatables_list:
    print(obj)
    non_eatables.append(cv2.imread(f'{non_eatables_folder}/{obj}', cv2.IMREAD_UNCHANGED))

print(eatables)
print(non_eatables)

while True:
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img, draw=False)
    if faces:
        # print(faces[0])
        face = faces[0]
        '''
        for id, point in enumerate(face):
            cv2.putText(img, str(id), point, cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 0, 255), 1)
        '''
        for id in ids_list:
            cv2.circle(img, face[id], 5, (255, 0, 255), 5)
        cv2.line(img, face[mouth_top], face[mouth_bottom], (0, 255, 0), 3)
        cv2.line(img, face[mouth_left], face[mouth_right], (0, 255, 255), 3)

        vertical, _ = detector.findDistance(face[mouth_top], face[mouth_bottom])
        horizontal, _ = detector.findDistance(face[mouth_left], face[mouth_right])

        ratio = int(vertical / horizontal * 100)
        if (ratio > 60):
            mouthStatus = "Open"
        else:
            mouthStatus = "Closed"
        cv2.putText(img, mouthStatus, [50, 50], cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 255), 2)

        img = cvzone.overlayPNG(img, eatables[0], (300, 300))

    cv2.imshow("Capture", img)
    cv2.waitKey(1)
