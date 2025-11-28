import cv2
import face_recognition
import pickle
import numpy as np

# --- AYARLAR ---
model_file = 'model.pickle'
TOLERANCE = 0.55
SCALE = 0.25

print("Sistem başlatılıyor...")

# 1. Model Dosyasını Yükle
try:
    with open(model_file, 'rb') as f:
        known_face_encodings, known_face_names = pickle.load(f)
    print(f"Model yüklendi. {len(known_face_names)} kişi tanınıyor.")
except FileNotFoundError:
    print(f"HATA: '{model_file}' bulunamadı! Önce 'egitim.py' dosyasını çalıştırın.")
    exit()

# 2. Kamera Başlatma
cap = cv2.VideoCapture(0)
print("Kamera açılıyor. Çıkış için 'q'.")

while True:
    success, img = cap.read()
    if not success: break

    imgS = cv2.resize(img, (0, 0), None, SCALE, SCALE)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(known_face_encodings, encodeFace, tolerance=TOLERANCE)
        faceDis = face_recognition.face_distance(known_face_encodings, encodeFace)

        matchIndex = np.argmin(faceDis)
        name = "UNKNOWN"
        color = (0, 0, 255)

        if matches[matchIndex]:
            name = known_face_names[matchIndex].upper()
            color = (0, 255, 0)

        y1, x2, y2, x1 = faceLoc
        y1, x2, y2, x1 = int(y1 / SCALE), int(x2 / SCALE), int(y2 / SCALE), int(x1 / SCALE)

        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
        cv2.rectangle(img, (x1, y2 - 35), (x2, y2), color, cv2.FILLED)
        cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow('Yuz Tanima Sistemi', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()