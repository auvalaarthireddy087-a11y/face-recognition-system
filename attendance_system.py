import cv2
from datetime import datetime

cap = cv2.VideoCapture(0)

attendance_marked = False

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.putText(
        frame,
        "Arthi Present",
        (50, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    if not attendance_marked:
        with open("attendance.csv", "a") as f:
            now = datetime.now()
            f.write(f"Arthi,{now}\n")

        attendance_marked = True
        print("Attendance Marked")

    cv2.imshow("Attendance System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
