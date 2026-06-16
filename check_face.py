from deepface import DeepFace

print("Testing...")

result = DeepFace.verify(
    img1_path="dataset/arthi.jpg",
    img2_path="dataset/arthi.jpg",
    enforce_detection=False
)

print(result)