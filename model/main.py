import cv2
import numpy as np
import mss
import model

# make a window
# Get the screen size
with mss.mss() as sct:
    monitor = sct.monitors[1]

# Create a named window
cv2.namedWindow("Live Screen", cv2.WINDOW_NORMAL)

while True:
    # Capture the screen
    with mss.mss() as sct:
        screenshot = sct.grab(monitor)
    
    # Convert the screenshot to a numpy array
    frame = np.array(screenshot)
    
    # Convert the color from BGRA to BGR
    frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
    
    # Display the frame
    cv2.imshow("Live Screen", frame)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the window
cv2.destroyAllWindows()

# Assuming model.py has a function called detect_objects that takes a frame and returns detections
detections = model.detect_objects(frame)

# Draw the detections on the frame
for detection in detections:
    x, y, w, h = detection['bbox']
    label = detection['label']
    confidence = detection['confidence']
    
    # Draw a rectangle around the detected object
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Put the label and confidence on the frame
    cv2.putText(frame, f"{label} ({confidence:.2f})", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)