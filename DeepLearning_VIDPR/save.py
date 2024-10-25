import cv2

# Open the video camera
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open the video camera.")
    exit()

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'avc1')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Write the frame to the output file
    out.write(frame)

    # Display the resulting frame
    cv2.imshow('Webcam', frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture and output
cap.release()       # Release the camera
out.release()       # Release the VideoWriter
cv2.destroyAllWindows()  # Close all OpenCV windows
