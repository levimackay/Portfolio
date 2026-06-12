import cv2
import mediapipe as mp
import time


mp_drawing = mp.solutions.drawing_utils  
mp_pose = mp.solutions.pose              
pose_tracker = mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Can't find webcam.")
    exit()

head_anchor_y = None
status = "READY - PRESS 'S' TO SET HEAD LEVEL"

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        continue

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose_tracker.process(rgb_frame)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
        
    if key == ord('s'):
        if results.pose_landmarks:

            nose = results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE]
            head_anchor_y = nose.y
            status = "ANCHOR SET - STAY LEVEL"
        else:
            status = "ERROR: NO POSE DETECTED"

    if results.pose_landmarks:
        mp_drawing.draw_landmarks(
            frame, 
            results.pose_landmarks, 
            mp_pose.POSE_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(56, 189, 248), thickness=2, circle_radius=2),
            mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=1, circle_radius=1)
        )
        
        if head_anchor_y is not None:
            current_nose_y = results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y
            
            anchor_px = int(head_anchor_y * h)
            current_px = int(current_nose_y * h)


            cv2.line(frame, (0, anchor_px), (w, anchor_px), (0, 255, 0), 2)
            cv2.line(frame, (0, current_px), (w, current_px), (0, 0, 255), 2)

            diff = anchor_px - current_px
            if abs(diff) > 20:
                status = "WATCH YOUR HEAD!" if diff < 0 else "STAY DOWN!"
            else:
                status = "SOLID"


    cv2.rectangle(frame, (0, 0), (w, 50), (15, 23, 42), -1)
    cv2.putText(frame, status, (20, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (56, 189, 248), 2)
    cv2.putText(frame, "'S' to set anchor | 'Q' to quit", (w-300, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    cv2.imshow('SwingOS Prototype', frame)

cap.release()
cv2.destroyAllWindows()
pose_tracker.close()
