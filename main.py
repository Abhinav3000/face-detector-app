import cv2
from facenet_pytorch import MTCNN
from PIL import Image

# Initialize the face detector
mtcnn = MTCNN(keep_all=True)

# Open webcam (0 = default cam)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert OpenCV BGR frame to PIL RGB image
    img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    # Detect faces
    boxes, _ = mtcnn.detect(img)

    # Draw face boxes
    if boxes is not None:
        for box in boxes:
            x1, y1, x2, y2 = [int(val) for val in box]
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Show the frame with detected boxes
    cv2.imshow('Face Detection Live', frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
