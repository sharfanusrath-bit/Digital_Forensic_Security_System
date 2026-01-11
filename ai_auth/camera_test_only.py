import cv2

cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("Camera not accessible")
    exit()

print("Camera opened successfully")

while True:
    ret, frame = cam.read()
    if not ret:
        print("Failed to read frame")
        break

    cv2.imshow("Camera Test Window", frame)

    # VERY IMPORTANT: press ESC to exit
    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()
