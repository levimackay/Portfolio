# =============================================================================
# LEVI'S AI SWING ANALYZER (Prototype v1.0)
#
# This is my first real swing at combining computer vision with baseball.
# The goal is to eventually have this thing tell you exactly why you're 
# swinging under the ball or why your head is moving too much.
#
# Right now, it's a solid proof-of-concept using MediaPipe to track 
# body positions in real-time.
# =============================================================================

import cv2
import mediapipe as mp
import time

# --- Setup Stuff ---
# This is where we get the MediaPipe engine running. 
# It's basically a pre-trained model that knows where human joints are.
print("Firing up the AI models... hang tight.")
mp_drawing = mp.solutions.drawing_utils  
mp_pose = mp.solutions.pose              
pose_tracker = mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Open the webcam. If you have multiple cameras, you might need to change 0 to 1.
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Uh oh. I can't find your webcam. Check the connection.")
    exit()

# Variables to keep track of where your head is
head_anchor_y = None
status = "READY - PRESS 'S' TO SET HEAD LEVEL"

print("All systems go. Let's see that swing.")

# --- The Main Loop ---
# This runs constantly, processing each frame from your camera.
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Empty camera frame. Skipping...")
        continue

    # Flip the image horizontally for a later selfie-view display
    # (Makes it feel more like a mirror, which is easier for drills)
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    
    # MediaPipe needs RGB, but OpenCV defaults to BGR. Logic, right?
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose_tracker.process(rgb_frame)
    
    # --- Input Handling ---
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        print("Shutting down. Go hit some bombs.")
        break
        
    if key == ord('s'):
        # Setting the 'anchor' - basically the height of your head at stance.
        if results.pose_landmarks:
            # Using the nose as the center point of the head.
            nose = results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE]
            head_anchor_y = nose.y
            status = "ANCHOR SET - STAY LEVEL"
        else:
            status = "ERROR: I DON'T SEE A HUMAN"

    # --- Draw the Skeleton ---
    if results.pose_landmarks:
        # This draws the lines and dots over your body.
        mp_drawing.draw_landmarks(
            frame, 
            results.pose_landmarks, 
            mp_pose.POSE_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(56, 189, 248), thickness=2, circle_radius=2), # LM Blue
            mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=1, circle_radius=1)
        )
        
        # --- Head Tracking Logic ---
        # This is where the actual 'analysis' happens.
        if head_anchor_y is not None:
            current_nose_y = results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y
            
            # Convert normalized (0-1) coordinates to actual pixels
            anchor_px = int(head_anchor_y * h)
            current_px = int(current_nose_y * h)

            # Draw the visual guides
            cv2.line(frame, (0, anchor_px), (w, anchor_px), (0, 255, 0), 2) # Green = Target
            cv2.line(frame, (0, current_px), (w, current_px), (0, 0, 255), 2) # Red = Current

            # If you move your head more than 20 pixels, we flag it.
            diff = anchor_px - current_px
            if abs(diff) > 20:
                status = "WATCH YOUR HEAD!" if diff < 0 else "STAY DOWN!"
            else:
                status = "SOLID - STAY THERE"

    # --- UI Overlay ---
    # Just making it look a bit cleaner for the portfolio.
    cv2.rectangle(frame, (0, 0), (w, 50), (15, 23, 42), -1) # Dark Slate Header
    cv2.putText(frame, status, (20, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (56, 189, 248), 2)
    cv2.putText(frame, "'S' to set anchor | 'Q' to quit", (w-300, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    # Show the result
    cv2.imshow('Levi\'s AI SwingOS Prototype', frame)

# Clean up
cap.release()
cv2.destroyAllWindows()
pose_tracker.close()
