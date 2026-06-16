# 🎯 AI Face Recognition Attendance System

## 📌 Project Description

The AI Face Recognition Attendance System is a real-time attendance application developed using Python, OpenCV, DeepFace, and TensorFlow.

The system captures live video through a webcam and verifies the detected face with a stored image dataset. When the face matches, the system automatically marks attendance with the current date and time in a CSV file.

If the registered user is not detected, the system displays an absence status.

---

## 🚀 Features

* Real-time webcam access
* AI-based face verification using DeepFace
* Automatic attendance marking
* Present and Absent status display
* Attendance saved in CSV format
* Live video display using OpenCV

---

## 🛠️ Technologies Used

* Python
* OpenCV
* DeepFace
* TensorFlow
* NumPy
* CSV File Handling

---

## ⚙️ Project Workflow

1. Open webcam and capture live video.
2. Store the registered user's image in the dataset folder.
3. Compare the live webcam frame with the stored image using DeepFace.
4. If the face matches:

   * Display **"Arthi Present"**
   * Store attendance with date and time.
5. If the face is not detected:

   * Display **"Arthi Absent"**
6. Attendance is automatically saved in `attendance.csv`.

---

## 📂 Project Structure

face-recognition-system/

├── dataset/

│ └── arthi.jpg

├── attendance.csv

├── real_attendance.py

└── check_face.py

---

## 📊 Output

* Real-time face recognition using webcam.
* Displays attendance status on screen.
* Saves attendance records automatically.

---

## 🌍 Real World Applications

* College Attendance Systems
* School Attendance Management
* Office Employee Attendance
* Smart Classroom Applications

---

## 💡 Conclusion

This project demonstrates how Artificial Intelligence and Computer Vision can automate attendance management using face recognition technology. It provides a simple and efficient solution for real-time attendance tracking.
