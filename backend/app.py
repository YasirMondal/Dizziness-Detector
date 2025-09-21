from flask import Flask, render_template, request, jsonify
import base64
import cv2
import numpy as np
import mediapipe as mp
import time

app = Flask(__name__, template_folder='../frontend', static_folder='../frontend')

# MediaPipe setup
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, refine_landmarks=True)

# Variables to track movement
prev_nose = None
movement_history = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    global prev_nose, movement_history

    data = request.get_json()
    img_data = data.get('image')
    if not img_data:
        return jsonify({"dizziness": 0, "message": "No image received"})

    # Decode base64 image
    header, encoded = img_data.split(',', 1)
    img_bytes = base64.b64decode(encoded)
    nparr = np.frombuffer(img_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Convert to RGB for MediaPipe
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(img_rgb)

    dizziness_score = 0

    if results.multi_face_landmarks:
        face = results.multi_face_landmarks[0]

        # Get nose tip landmark (landmark 1)
        nose_tip = face.landmark[1]
        nose_pos = np.array([nose_tip.x, nose_tip.y])

        if prev_nose is not None:
            # Calculate movement distance
            dist = np.linalg.norm(nose_pos - prev_nose)
            movement_history.append(dist)

            # Keep last 10 movements
            if len(movement_history) > 10:
                movement_history.pop(0)

            # Simple heuristic: average movement * 1000
            dizziness_score = min(int(np.mean(movement_history)*2500), 100)

        prev_nose = nose_pos

    return jsonify({"dizziness": dizziness_score, "message": "Frame analyzed"})

if __name__ == '__main__':
    app.run(debug=True)