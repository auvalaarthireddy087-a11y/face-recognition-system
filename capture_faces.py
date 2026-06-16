import cv2
import os

person_name = "Arthi"
save_path = f"dataset/{person_name}"

os.makedirs(save_path, exist_ok=True)

cap = cv2.VideoCapture(0)

count = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Capture Faces", frame)

    key = cv2.waitKey(1)

    if key == ord('s'):
        count += 1
        filename = os.path.join(save_path, f"{count}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Saved: {filename}")

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()