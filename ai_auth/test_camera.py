import cv2

for i in range(3):
    cam = cv2.VideoCapture(i)
    if cam.isOpened():
        print(f"Camera found at index {i}")
        ret, frame = cam.read()
        if ret:
            cv2.imshow(f"Camera {i}", frame)
            cv2.waitKey(3000)
            cv2.destroyAllWindows()
        cam.release()
        break
    else:
        print(f"No camera at index {i}")
