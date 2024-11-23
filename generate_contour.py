import cv2

#Open video file or webcam

video_path = "videoopencv.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Cannot open video.")
    exit()

while True:
    # Read a frame from the video
    ret, frame = cap.read()
    if not ret:
        break  # Exit loop if no frame is read

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply edge detection (Canny)
    edges = cv2.Canny(blurred, 100, 200)

    # Find contours from the edges
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours on the original frame
    frame_with_contours = frame.copy()
    cv2.drawContours(frame_with_contours, contours, -1, (0, 255, 0), 2)

    # Display the original frame and frame with contours
    cv2.imshow("Original Frame", frame)
    cv2.imshow("Contours", frame_with_contours)

    # Break the loop on 'q' key press
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
