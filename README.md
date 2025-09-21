# Dizziness Detector

A web-based Dizziness Detector** that uses HTML, CSS, and JavaScript for the frontend, and Python with Flask for the backend.
The system leverages **Mediapipe**, **OpenCV**, and **NumPy** to capture live facial motion through the camera and estimate the probability of dizziness in real time.

## Features
- Detects live facial motion via webcam.
- Calculates dizziness probability as a percentage.
- Real-time analysis with visual feedback.
- Simple and responsive web interface.

## Tech Stack
- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Python, Flask  
- **Libraries:** Mediapipe, OpenCV, NumPy  

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/YasirMondal/Dizziness-Detector
Navigate to the project folder:

bash
cd your-repo
Create a virtual environment (optional but recommended):

bash
python -m venv venv

Activate it:

Windows:
bash
venv\Scripts\activate

Linux / Mac:
bash
source venv/bin/activate
Install required libraries manually:

bash
pip install numpy
pip install opencv-python
pip install mediapipe
pip install flask
Running the App
Start the Flask backend:

bash
python app.py
Open your browser and go to:

http://127.0.0.1:5000
Allow camera access when prompted. The app will detect your face and show dizziness probability in real time.

Usage Tips
Use in a well-lit environment for best detection results.

Make sure your webcam is working properly.

📄 License
© 2025 Yasir Mondal. All rights reserved.
This project is not licensed for public use without permission.

📧 Contact

For questions or feedback, reach out to mondalyasir386@gmail.com.
