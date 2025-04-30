import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import cv2
import torch
import time

# Modül yükleme ve CUDA kontrolü
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"CUDA kullanılabilir: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"Kullanılan cihaz: {torch.cuda.get_device_name(0)}")

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
model.to(device)
model.eval()

# KAMERA : IP KAMERA
cap = cv2.VideoCapture("http://192.168.1.45:8080/video")# IP kamera URL'sini buraya girin

# Durum takibi için değişkenler
person_currently_present = False
last_seen_time = 0
exit_threshold_seconds = 3  # kişi 3 saniyeden fazla görünmezse çıktı say

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    detections = results.pred[0]

    person_detected_now = False

    for *box, conf, cls in detections:
        if model.names[int(cls)] == "person":
            person_detected_now = True
            x1, y1, x2, y2 = map(int, box)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
            cv2.putText(frame, "Person", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)

    current_time = time.time()

    # Kişi varsa zaman güncelle
    if person_detected_now:
        last_seen_time = current_time

        # Daha önce kişi yoktuysa, şimdi var → giriş bildir
        if not person_currently_present:
            print("Kişi tespit edildi.")
            person_currently_present = True

    else:
        # Kişi görünmüyorsa ve belirli süre geçtiyse artık yok say
        if person_currently_present and (current_time - last_seen_time > exit_threshold_seconds):
            print("Kişi çıktı.")
            person_currently_present = False

    cv2.imshow("IP Kamera - Kişi Tespiti", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
