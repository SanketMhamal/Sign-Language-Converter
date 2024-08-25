from function import *
from keras.utils import to_categorical
from keras.models import model_from_json
from keras.layers import LSTM, Dense
from keras.callbacks import TensorBoard
from keras.models import load_model
def run_sign_to_text():
    # Load the model
    json_file = open("model.json", "r")
    model_json = json_file.read()
    json_file.close()
    model = model_from_json(model_json)
    model.load_weights("model.h5")

    # Define colors for visualization
    colors = [(245,117,16) for _ in range(20)]

    # Function to visualize probabilities
    def prob_viz(res, actions, input_frame, colors, threshold):
        output_frame = input_frame.copy()
        for num, prob in enumerate(res):
            cv2.rectangle(output_frame, (0,60+num*40), (int(prob*100), 90+num*40), colors[num], -1)
            cv2.putText(output_frame, actions[num], (0, 85+num*40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
        return output_frame

    # Variables for detection
    sequence = []
    sentence = []
    accuracy = []
    predictions = []
    threshold = 0.8

    # Initialize video capture
    cap = cv2.VideoCapture(0)

    # Set mediapipe hands model
    mp_hands = mp.solutions.hands
    with mp_hands.Hands(
        model_complexity=0,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:

        while cap.isOpened():
            # Read feed
            ret, frame = cap.read()
            if not ret:
                break

            # Define active region for gesture detection
            cropframe = frame[40:400, 0:300]
            frame = cv2.rectangle(frame, (0,40), (300,400), 255, 2)
            
            # Make detections using mediapipe
            image, results = mediapipe_detection(cropframe, hands)

            # Extract keypoints from the results
            keypoints = extract_keypoints(results)
            sequence.append(keypoints)
            sequence = sequence[-30:]

            # Prediction logic
            try:
                if len(sequence) == 30:
                    res = model.predict(np.expand_dims(sequence, axis=0))[0]
                    predictions.append(np.argmax(res))

                    # Update sentence and accuracy if confident enough
                    if np.unique(predictions[-10:])[0] == np.argmax(res):
                        if res[np.argmax(res)] > threshold:
                            if len(sentence) > 0:
                                if actions[np.argmax(res)] != sentence[-1]:
                                    sentence.append(actions[np.argmax(res)])
                                    accuracy.append(f"{res[np.argmax(res)] * 100:.2f}%")
                            else:
                                sentence.append(actions[np.argmax(res)])
                                accuracy.append(f"{res[np.argmax(res)] * 100:.2f}%")

                    if len(sentence) > 1:
                        sentence = sentence[-1:]
                        accuracy = accuracy[-1:]
                    
            except Exception as e:
                pass

            # Display the output text on the frame
            cv2.rectangle(frame, (0,0), (300, 40), (245, 117, 16), -1)
            cv2.putText(frame, f"Output: {' '.join(sentence)} {' '.join(accuracy)}", (3, 30), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

            # Show the frame
            cv2.imshow('OpenCV Feed', frame)

            # Exit on 'q' key press
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()