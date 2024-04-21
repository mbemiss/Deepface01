from deepface import DeepFace

img_path = "F:/AI School/MS Adv Prog/Faces/1200-156820425-fair-woman.jpg"

# perform face recognition
result = DeepFace.analyze(img_path)

# print these results
first_face = result[0]
print("Face recognition result: ")
print("Emotion: ", first_face['emotion'])
print("Gender: ", first_face['gender'])
print("Race: ", first_face['race'])
print("The dominant characteristics are as follows:")
print("Emotion: ", first_face['dominant_emotion'])
print("Gender: ", first_face['dominant_gender'])
print("Race: ", first_face['dominant_race'])
print("Age: ", first_face['age'])
