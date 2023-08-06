import cv2
import numpy as np
import tensorflow as tf

class_names = ['drink', 'eat', 'hello', 'help', 'love', 'morning', 'okay', 'please', 'stop', 'thankyou']

# Load the TensorFlow Lite model
interpreter = tf.lite.Interpreter(model_path="trained_model.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Open webcam
cam_capture = cv2.VideoCapture(0)

while True:
    # Capture the image from webcam
    _, image_frame = cam_capture.read()

    # Preprocess the image (resize and normalize)
    target_size = (224, 224)  # Adjust to match your model's input size
    resized_image = cv2.resize(image_frame, target_size)
    preprocessed_image = resized_image.astype('float32') / 255.0
    input_data = np.expand_dims(preprocessed_image, axis=0)

    # Set the input tensor
    interpreter.set_tensor(input_details[0]['index'], input_data)

    # Run inference
    interpreter.invoke()

    # Get the output tensor
    output_data = interpreter.get_tensor(output_details[0]['index'])

    # Post-process the output (interpret the classification)
    predicted_class_idx = np.argmax(output_data)
    predicted_class = class_names[predicted_class_idx]

    # Display the classification result on the image
    cv2.putText(image_frame, f"Class: {predicted_class}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # Display the image with the classification result
    cv2.imshow("Image Classification", image_frame)

    # Exit the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam
cam_capture.release()
cv2.destroyAllWindows()
