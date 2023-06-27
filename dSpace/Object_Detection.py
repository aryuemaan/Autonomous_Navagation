import cv2
import numpy as np
import tensorflow as tf

# Load the pre-trained SSD model
model_path = 'path/to/ssd/model'
model = tf.saved_model.load(model_path)
infer = model.signatures['serving_default']

# Define the class labels
class_labels = ['background', 'car', 'pedestrian', 'cyclist']

# Load the video feed from the camera
cap = cv2.VideoCapture(0)  # Use 0 for default camera

while True:
    ret, frame = cap.read()

    # Preprocess the frame for input to the model
    input_data = cv2.resize(frame, (300, 300))
    input_data = np.expand_dims(input_data, axis=0)
    input_data = input_data / 255.0  # Normalize pixel values to [0, 1]
    input_data = input_data.astype(np.float32)

    # Perform inference
    detections = infer(tf.constant(input_data))

    # Extract relevant information from detections
    num_detections = int(detections['num_detections'][0])
    detection_classes = detections['detection_classes'][0][:num_detections]
    detection_scores = detections['detection_scores'][0][:num_detections]
    detection_boxes = detections['detection_boxes'][0][:num_detections]

    # Process the detections
    for i in range(num_detections):
        class_id = int(detection_classes[i])
        class_label = class_labels[class_id]
        score = detection_scores[i]
        box = detection_boxes[i]

        # Filter out low confidence detections
        if score > 0.5:
            height, width, _ = frame.shape
            ymin, xmin, ymax, xmax = box
            xmin = int(xmin * width)
            xmax = int(xmax * width)
            ymin = int(ymin * height)
            ymax = int(ymax * height)

            # Draw bounding box and label on the frame
            cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
            cv2.putText(frame, f'{class_label}: {score:.2f}', (xmin, ymin - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Object Detection', frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close all windows
cap.release()
cv2.destroyAllWindows()
