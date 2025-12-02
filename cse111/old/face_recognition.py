import cv2

def load_face_detector():
    print("[INFO] Loading Haar cascade face detector...")
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    if face_cascade.empty():
        print("[ERROR] Could not load Haar cascade classifier. Check file path.")
    return face_cascade

def detect_faces(image, face_cascade):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    print(f"[INFO] Detected {len(faces)} face(s).")
    return faces

def draw_faces(image, faces):
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    return image

def start_webcam_detection():
    face_cascade = load_face_detector()
    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        print("[ERROR] Cannot open camera. Make sure you granted camera permissions in System Settings.")
        return

    print("[INFO] Starting webcam... Click on the video window and press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[ERROR] Failed to grab frame. Exiting...")
            break

        faces = detect_faces(frame, face_cascade)
        frame_with_faces = draw_faces(frame, faces)

        cv2.imshow('Facial Recognition Demo', frame_with_faces)

        # Make sure the window has focus!
        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            print("[INFO] Quitting...")
            break

    cap.release()
    cv2.destroyAllWindows()
    print("[INFO] Webcam closed.")

if __name__ == "__main__":
    start_webcam_detection()
