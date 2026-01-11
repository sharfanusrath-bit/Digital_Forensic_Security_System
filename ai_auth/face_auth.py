import cv2

def face_authentication():
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        print("Camera not accessible")
        return False

    print("Camera opened. Press 'q' to capture image.")

    while True:
        ret, frame = cam.read()
        if not ret:
            print("Failed to grab frame")
            break

        cv2.imshow("AI Face Authentication", frame)

        # Press 'q' to capture and exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) > 0:
        print("Face detected – AI authentication successful")
        return True
    else:
        print("No face detected – authentication failed")
        return False
