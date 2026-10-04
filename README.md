# Smart Attendance System Using Face Recognition

A webcam-based attendance system built with Python and OpenCV. It detects faces with a Haar cascade, recognizes them with the LBPH algorithm, and saves attendance with date and time to CSV files.

Final-year BCA team project, Harsha Institute of Management Studies, Bangalore University (2026). Guided by Prof. Sirajudheen.

## Features
- Menu-driven console application
- Camera check before starting
- Register a student (numeric ID + name); captures about 100 face samples
- Train the LBPH model on the captured images
- Real-time recognition; each student is marked once per session
- Attendance saved as a timestamped CSV in `Attendance/`
- Optional: email the latest attendance report

## Tech Stack
Python, OpenCV (opencv-contrib-python), NumPy, pandas, Pillow, yagmail

## How to Run
1. Clone the repo and install dependencies:
   pip install -r requirements.txt
2. Start the app:
   python main.py
3. Use the menu in order: 1 Check Camera, 2 Capture Faces, 3 Train Images, 4 Recognize & Attendance, 5 Auto Mail

## Notes
- Built for Windows (uses `cls`).
- Names must be alphabetic and IDs numeric when registering.
- For Auto Mail, add your own sender/receiver details in `automail.py`. Use an app password and never commit real credentials.
- Face images and attendance records are not included, for privacy.

## Acknowledgements
Based on an open-source face recognition attendance project. Modified for our college project with the help of AI tools.
