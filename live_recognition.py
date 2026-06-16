from deepface import DeepFace
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imwrite("temp.jpg", frame)

    try:
        result = DeepFace.find(
            img_path="temp.jpg",
            db_path="dataset",
            enforce_detection=False,
            silent=True
        )

        if len(result[0]) > 0:
            cv2.putText(
                frame,
                "Arthi Detected",
                (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

    except:
        pass

    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()