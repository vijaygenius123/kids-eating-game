import cv2
from cvzone.FaceMeshModule import FaceMeshDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = FaceMeshDetector(maxFaces=2)

ids_list = [0, 17, 78, 292]

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
        cv2.line(img, face[ids_list[0]], face[ids_list[1]], (0, 255, 0), 3)
        cv2.line(img, face[ids_list[2]], face[ids_list[3]], (0, 255, 255), 3)
    cv2.imshow("Capture", img)
    cv2.waitKey(1)
