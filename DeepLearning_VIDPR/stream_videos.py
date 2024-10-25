import cv2

# Initialize VideoCapture objects for webcam and two video files
cap_webcam = cv2.VideoCapture(0)  # Webcam
cap_video1 = cv2.VideoCapture('vd1.mp4')  # First video file
cap_video2 = cv2.VideoCapture('vd2.mp4')  # Second video file

# Check if the webcam is opened successfully
if not cap_webcam.isOpened():
    print("Error: Could not open the video camera.")
    exit()

# Check if the video files are opened successfully
if not cap_video1.isOpened():
    print("Error: Could not open the first video file.")
    exit()

if not cap_video2.isOpened():
    print("Error: Could not open the second video file.")
    exit()

while True:
    # Capture frame from webcam
    ret_webcam, frame_webcam = cap_webcam.read()
    
    # Capture frame from first video
    ret_video1, frame_video1 = cap_video1.read()
    
    # Capture frame from second video
    ret_video2, frame_video2 = cap_video2.read()
    
    # If webcam frame is not captured, break the loop
    if not ret_webcam:
        print("Error: Failed to capture frame from webcam.")
        break
    
    # If first video frame is not captured, reset the video to start
    if not ret_video1:
        cap_video1.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Reset to the first frame
        ret_video1, frame_video1 = cap_video1.read()  # Read again
    
    # If second video frame is not captured, reset the video to start
    if not ret_video2:
        cap_video2.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Reset to the first frame
        ret_video2, frame_video2 = cap_video2.read()  # Read again

    # Show the frames in separate windows
    cv2.imshow('Webcam', frame_webcam)
    cv2.imshow('First Video', frame_video1)
    cv2.imshow('Second Video', frame_video2)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture objects and close all OpenCV windows
cap_webcam.release()
cap_video1.release()
cap_video2.release()
cv2.destroyAllWindows()




# Second Code


# import cv2

# video_sources = [
#     'vd1.mp4',
#     'vd2.mp4',
# ]

# caps = [cv2.VideoCapture(src) for src in video_sources]

# for i, cap in enumerate(caps):
#     if not cap.isOpened():
#         print(f"Error: Could not open video stream {i+1} from source: {video_sources[i]}")
#         exit()

# while True:
#     frames = [cap.read()[1] for cap in caps]

#     if any(frame is None for frame in frames):
#         print("Error: Could not read one or more frames.")
#         break

#     for i, frame in enumerate(frames):
#         window_name = f'Video {i+1}'
#         cv2.imshow(window_name, frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# for cap in caps:
#     cap.release()
# cv2.destroyAllWindows()
