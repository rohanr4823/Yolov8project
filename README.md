# Object Detection using YOLOv8

<img width="225" height="225" alt="image" src="https://github.com/user-attachments/assets/8d1b98d9-710f-4a65-a556-7a76a509cc04" />


This project uses YOLOv8 for real-time ship detection. The model processes live video streams or webcam input and identifies ships instantly by drawing bounding boxes around them.

How it works in real time:

Video Capture – Frames are continuously captured from a camera or video file using OpenCV.

YOLOv8 Inference – Each frame is passed through the YOLOv8 model, which detects ships by predicting their class and bounding box.

Filtering – Non-maximum suppression (NMS) removes overlapping boxes, keeping only the best predictions.

Visualization – Detected ships are displayed in real time with labels and confidence scores using cvzone and OpenCV.

Output – The processed video stream shows detected ships live, making it useful for maritime surveillance and monitoring.

<img width="320" height="320" alt="image" src="https://github.com/user-attachments/assets/21a651bc-fa0a-4b44-a5bc-1453751f2e25" />
<img width="303" height="166" alt="image" src="https://github.com/user-attachments/assets/08ff6174-5dd5-45e0-b27a-387f0eaf16d0" />



Because YOLOv8 performs detection in a single forward pass, it can achieve high FPS (frames per second), enabling smooth real-time performance.
