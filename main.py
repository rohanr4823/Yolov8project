from ultralytics import YOLO
import cv2

def main():
    # Load YOLOv8 model (pretrained on COCO dataset)
    model = YOLO("yolov8n.pt")  # Nano version: fastest for real-time webcam

    # Open webcam (0 = default camera)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

        # Run YOLO object detection
        results = model(frame)

        # Draw results on the frame
        annotated_frame = results[0].plot()

        # Show the output
        cv2.imshow("YOLOv8 Webcam Detection", annotated_frame)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
