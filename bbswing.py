# =============================================================================
# AI-POWERED BASEBALL SWING ANALYZER
#
# Author: Levi Mackay
# Project: Foundational prototype for a real-time swing analysis tool.
#
# Description:
# This application leverages computer vision to provide biomechanical feedback
# on a baseball swing. It captures video from a webcam, uses the MediaPipe
# library to perform real-time pose estimation, and overlays a skeletal
# model onto the video feed. This serves as the core framework for a more
# advanced system intended to analyze specific metrics like head movement
# and bat path.
#
# Note: This is a foundational prototype and does not include detailed tracking.
#
# =============================================================================

# --- Imports ---
import cv2
import mediapipe as mp


# --- Initialization ---
''' This section sets up the necessary components for the application, including
the video capture device (webcam) and the MediaPipe pose estimation model. '''
print("Initializing models and camera...")
mp_drawing = mp.solutions.drawing_utils  
mp_pose = mp.solutions.pose              
pose_tracker = mp_pose.Pose()

# Initialize the video capture object to access the default webcam (index 0).
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Cannot open webcam. Please check its connection and permissions.")

# --- Head Tracking Variables ---
head_anchor_y = None
status = "PRESS 'S' TO SET ANCHOR"

print("Initialization complete. Starting video stream...")


# --- Main Application Loop ---
''' This loop continuously captures frames from the webcam, processes them to
detect human poses, and displays the annotated frames in real-time. '''
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame. Exiting.")
        break
    
    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose_tracker.process(rgb_frame)
    
    # Check for user key presses.
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        print("'q' pressed. Shutting down.")
        break
    if key == ord('s'):
        # 's' key sets the head anchor point.
        if results.pose_landmarks:
            # We use the nose landmark (index 0) as our proxy for the head's position.
            nose_landmark = results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE.value]
            # MediaPipe provides coordinates normalized to [0.0, 1.0]. We store the y-coordinate.
            head_anchor_y = nose_landmark.y
            print(f"Head anchor set at normalized Y: {head_anchor_y:.2f}")
            status = "ANCHOR SET"
        else:
            status = "NO PERSON DETECTED!"

    if results.pose_landmarks:
        ''' Draw the pose landmarks and connections on the original frame.
        The landmarks represent key points on the human body, and the connections
        illustrate the skeletal structure. '''
        mp_drawing.draw_landmarks(
            image=frame,                     
            landmark_list=results.pose_landmarks,  
            connections=mp_pose.POSE_CONNECTIONS, 
            landmark_drawing_spec=mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
            connection_drawing_spec=mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
        )
        if head_anchor_y is not None:
            # Get the current y-coordinate of the nose.
            current_head_y = results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE.value].y

            # Convert the normalized anchor and current positions to pixel coordinates.
            anchor_pixel_y = int(head_anchor_y * h)
            current_pixel_y = int(current_head_y * h)

            # Draw a green line for the anchor point (your target level).
            cv2.line(frame, (0, anchor_pixel_y), (w, anchor_pixel_y), (0, 255, 0), 2)
            # Draw a red line for the current head position.
            cv2.line(frame, (0, current_pixel_y), (w, current_pixel_y), (0, 0, 255), 2)

            # Determine if the head has moved up or down significantly.
            vertical_diff_pixels = anchor_pixel_y - current_pixel_y
            if abs(vertical_diff_pixels) > 15: # A 15-pixel threshold to avoid minor jitters.
                if vertical_diff_pixels > 0:
                    status = "HEAD MOVED UP"
                else:
                    status = "HEAD MOVED DOWN"
            else:
                status = "HEAD LEVEL"
    cv2.rectangle(frame, (0, 0), (w, 60), (0, 0, 0), -1)
    cv2.putText(frame, "Press 's' to set anchor, 'q' to quit", (10, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(frame, f"STATUS: {status}", (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2, cv2.LINE_AA)
    
    ''' Display the annotated frame in a window titled "AI Swing Analyzer". '''
    cv2.imshow("AI Swing Analyzer", frame)

    ''' Check for 'q' key press to exit the loop and terminate the application.'''
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("'q' pressed. Shutting down.")
        break


# --- Cleanup Phase ---
print("Releasing resources...")
cap.release()               
cv2.destroyAllWindows()     
print("Shutdown complete.")


# --- All done! :) ---
