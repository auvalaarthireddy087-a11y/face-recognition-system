# Real-Time Face Recognition & Automated Attendance System

An advanced, production-grade computer vision and deep learning application engineered in Python. This system automates identity verification and attendance logging by combining high-throughput video stream ingestion with deep convolutional neural networks (CNNs). The pipeline orchestrates frame capture via physical hardware peripherals, processes facial localization spatial constraints, generates high-dimensional geometric embeddings, evaluates matching confidence, and records transactional records into a structured CSV database log.

---

## 🏗️ System Architecture & End-to-End Workflow

The application runs a continuous, multi-threaded pipeline across four primary decoupled phases:

1. **High-Throughput Video Acquisition:** The system establishes an active IO hardware hook to the onboard webcam peripheral, ingesting raw image matrices continuously at a target frames-per-second (FPS) rate.
2. **Spatial Localization & Preprocessing:** Frames are evaluated via a structural face cascade or neural detector. The system isolates the absolute boundaries of target faces, crops the coordinates into isolated Regions of Interest (ROIs), normalizes pixel value scales, and prepares the tensor for network injection.
3. **Deep Biometric Feature Extraction:** The cropped face array is passed to an evaluation engine backend (such as VGGFace). The deep layers map the structural ratios of facial topography (distance between eyes, nose bridge height, jaw curves) into a high-dimensional mathematical vector (embedding).
4. **Distance Matching Engine & Throttle Logging:** The calculated live vector is matched against stored reference vectors using spatial proximity formulas. If a match breaches the confidence boundary, identity is verified. The storage loop verifies if the user was flagged recently to prevent logging spam, then safely appends raw logs down to storage.

---

## 📁 Repository Blueprint & Subsystem Mapping

* **dataset/**: Centralized local facial biometrics repository containing reference directories.
    * **Arthi/**: Target identity folder for subject: Arthi containing ground-truth anchor images.
* **attendance.csv**: Main tabular database ledger processing structured, timestamped output logs.
* **attendance_system.py**: Primary production application orchestrator layout.
* **camera_test.py**: Low-level hardware diagnostic & FPS stability script to verify webcam streams.
* **capture_faces.py**: Data ingestion module tracking camera snapshots for new user enrollment.
* **check_face.py**: Isolated script executing deterministic dual-image validation checks.
* **deepface_test.py**: Benchmarking sandbox evaluating deep network topologies and backend weights.
* **face_detection.py**: Spatial tracking, array scaling, and bounding box calculator module.
* **live_recognition.py**: Live execution loop balancing thread consumers and UI display windows.
* **real_attendance.py**: I/O transaction framework binding classifications to final database updates.
* **test.py**: Isolated staging environment for experimental patches and minor code updates.

---

## 🛠️ Technology Stack & Low-Level Dependencies

* **Language Runtime Environment:** Python 3.13.5
* **Real-time Graphics & Matrix Computing:** OpenCV (`opencv-python`) — Manages active media streaming, frame rendering pipelines, graphical interface window bindings, and coordinate overlay calculations.
* **Deep Neural Networks Engine:** DeepFace & TensorFlow — Handles background neural layers, loads pre-trained topological configurations, handles weights, and calculates matrix-based vector distances.
* **Structured Data Processing:** Pandas & NumPy — Powers matrix manipulations, relational dataset parsing, and fast file transaction writes.
