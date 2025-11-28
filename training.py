import cv2
import face_recognition
import os
import pickle

dataset_path = 'photos'
model_file = 'model.pickle'

known_face_encodings = []
known_face_names = []

print("1/3 Veri seti taranıyor ve yüzler kodlanıyor...")

if not os.path.exists(dataset_path):
    print(f"HATA: '{dataset_path}' klasörü bulunamadı.")
    exit()

# Klasörleri gez
for person_name in os.listdir(dataset_path):
    person_folder = os.path.join(dataset_path, person_name)

    if os.path.isdir(person_folder):
        for filename in os.listdir(person_folder):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                img_path = os.path.join(person_folder, filename)

                # Resmi yükle ve RGB yap
                curImg = cv2.imread(img_path)
                if curImg is None: continue
                curImg = cv2.cvtColor(curImg, cv2.COLOR_BGR2RGB)

                # Yüzü kodla
                faces = face_recognition.face_encodings(curImg)

                if len(faces) > 0:
                    known_face_encodings.append(faces[0])
                    known_face_names.append(person_name)
                    print(f"İşlendi: {person_name} ({filename})")
                else:
                    print(f"UYARI: {filename} içinde yüz bulunamadı.")

print(f"2/3 Toplam {len(known_face_names)} yüz verisi çıkarıldı.")

# Verileri dosyaya kaydet (Serialization)
print(f"3/3 Veriler '{model_file}' dosyasına kaydediliyor...")
with open(model_file, 'wb') as f:
    pickle.dump([known_face_encodings, known_face_names], f)

print("Eğitim tamamlandı! Artık 'main.py' dosyasını çalıştırabilirsiniz.")