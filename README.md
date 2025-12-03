# Yüz Tanıma Sistemi / Face Recognition System

[Türkçe](#türkçe) | [English](#english)

---

<a name="türkçe"></a>
## Türkçe: Basit Yüz Tanıma Sistemi

Merhabalar, bu proje, Python kullanarak geliştirilmiş basit ve etkili bir yüz tanıma sistemidir. `face_recognition` kütüphanesini kullanarak fotoğraflardan yüzleri öğrenir ve kameradan anlık olarak bu kişileri tanıyabilir.

Projeyi GitHub'a yüklerken kendi fotoğraflarımı ve oluşturulan model dosyasını kişisel veriler içerdiği için kaldırdım. Ancak endişelenmeyin, aşağıdaki adımları takip ederek sistemi kendi fotoğraflarınızla çok kolay bir şekilde çalıştırabilirsiniz.

### Örnek Video

Aşağıda sistemin nasıl çalıştığına dair kısa bir örnek videoyu indirebilirsiniz:
[Örnek Videoyu İndir/İzle](sample-video/sample-video.mp4)

### Gereksinimler

Projenin çalışması için gerekli kütüphaneler `requirements.txt` dosyasında belirtilmiştir. Aşağıdaki komut ile paketleri yükleyiniz.

```bash
pip install -r requirements.txt
```

### Nasıl Çalışır?

Sistem temel olarak iki aşamadan oluşur:
1. **Eğitim (`training.py`):** `photos` klasöründeki fotoğrafları tarar, yüzleri analiz eder ve bu bilgileri `model.pickle` dosyasına kaydeder.
2. **Tanıma (`main.py`):** Kameranızı açar, `model.pickle` dosyasındaki bilgileri kullanarak ekrandaki yüzleri tanımaya çalışır.

### Kurulum ve Kullanım

Projeyi bilgisayarınıza indirdikten sonra şu adımları izleyebilirsiniz:

#### 1. Fotoğrafları Hazırlama
`photos` klasörünün içinde `kisi-1` ve `kisi-2` adında iki örnek klasör bıraktım.
- Bu klasörlerin isimlerini tanınmasını istediğiniz kişinin ismiyle değiştirin (örneğin: `ahmet`, `ayse`).
- İçine o kişiye ait fotoğrafları koyun (ne kadar çok ve net fotoğraf olursa o kadar iyi çalışır).
- **Önemli:** Fotoğrafları `1.jpg`, `2.jpg` gibi numaralandırarak kaydetmeniz önerilir.
- Eğer daha fazla kişi eklemek isterseniz, `photos` klasörü altına yeni klasörler oluşturup içine fotoğrafları atmanız yeterli.

#### 2. Modeli Eğitme
Fotoğrafları ayarladıktan sonra eğitim scriptini çalıştırın:
```bash
python training.py
```
Bu işlem `model.pickle` adında bir dosya oluşturacaktır. Bu dosya, yüzlerin sayısal haritasını içerir.

#### 3. Sistemi Başlatma
Eğitim tamamlandıktan sonra ana programı çalıştırabilirsiniz:
```bash
python main.py
```
Kamera açılacak ve tanımladığınız kişileri gördüğünde isimlerini ekranda gösterecektir. Çıkmak için 'q' tuşuna basabilirsiniz.

---

<a name="english"></a>
## English: Simple Face Recognition System

Hello! This is a simple and effective face recognition system built with Python. It utilizes the `face_recognition` library to learn faces from photos and recognize them in real-time via webcam.

I have removed my personal photos and the pre-trained model file for privacy reasons. However, you can easily run the system with your own photos by following the steps below.

### Sample Video

You can download/watch a short sample video of the system in action here:
[Download/Watch Sample Video](sample-video/sample-video.mp4)

### Requirements

The necessary libraries are listed in `requirements.txt`. You can install them easily using the following command:

```bash
pip install -r requirements.txt
```

### How It Works

The system consists of two main stages:
1. **Training (`training.py`):** Scans photos in the `photos` directory, analyzes faces, and saves the encoding data to `model.pickle`.
2. **Recognition (`main.py`):** Opens your webcam and attempts to recognize faces using the data from `model.pickle`.

### Setup and Usage

After cloning the repository, follow these steps:

#### 1. Prepare Photos
I have left two sample folders named `kisi-1` and `kisi-2` inside the `photos` directory.
- Rename these folders to the name of the person you want to recognize (e.g., `john`, `jane`).
- Place photos of that person inside their respective folder (more photos yield better accuracy).
- **Note:** It is recommended to name photos simply, like `1.jpg`, `2.jpg`, etc.
- To add more people, simply create new folders under `photos` and add their images.

#### 2. Train the Model
Once photos are in place, run the training script:
```bash
python training.py
```
This will generate a `model.pickle` file containing the facial encodings.

#### 3. Start the System
After training is complete, run the main program:
```bash
python main.py
```
The webcam will open and display the names of recognized people. Press 'q' to quit.
