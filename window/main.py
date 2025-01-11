import cv2
import numpy as np
import mss

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