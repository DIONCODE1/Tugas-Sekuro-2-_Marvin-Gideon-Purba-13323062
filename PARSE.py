#Nama : Marvin Gideon Purba
#NIM : 13323062 
#Parsing video to images 
import cv2 as cv
import os


video_path = 'videoopencv.mp4'
output_folder = 'OpenCV'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
cap = cv.VideoCapture(video_path)
frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.png")
    cv.imwrite(frame_filename, frame)
    frame_count += 1

cap.release()
print(f"Frame berhasil disimpan di folder: {output_folder}")

#sourcecode : https://docs.opencv.org/4.x/d9/df8/tutorial_root.html
