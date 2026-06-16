from deepface import DeepFace
import cv2
from datetime import datetime

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

attendance_marked = False

while True:

    ret, frame = cap.read()

    if not ret:
        break

    cv2.imwrite("temp.jpg", frame)

    status = "Arthi Absent"

    try:

        result = DeepFace.verify(
            img1_path="dataset/arthi.jpg",
            img2_path="temp.jpg",
            enforce_detection=False,
            detector_backend="opencv"
        )

        if result["verified"]:

            status = "Arthi Present"

            if not attendance_marked:

                with open("attendance.csv","a") as f:

                    now = datetime.now()

                    f.write(
                        f"Arthi,Present,{now}\n"
                    )

                attendance_marked = True

        else:

            status = "Unknown"

    except:

        status = "Arthi Absent"

    cv2.putText(
        frame,
        status,
        (50,50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
    )

    cv2.imshow("Real Face Attendance", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()