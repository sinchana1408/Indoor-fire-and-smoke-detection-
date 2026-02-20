
# 🔥 Indoor Fire and Smoke Detection using YOLOv8

## 📌 Project Overview

This project implements a real-time Indoor Fire and Smoke Detection System using YOLOv8 (You Only Look Once version 8). The model is trained to detect fire and smoke in indoor environments using computer vision and deep learning.

The system can be used for:
- Early fire detection
- CCTV monitoring systems
- Smart building safety systems
- Automated fire alert systems

---

## 🚀 Features

- 🔥 Detects Fire
- 💨 Detects Smoke
- 🎯 Real-time object detection
- 📦 Bounding box prediction with confidence score
- 🧠 Deep learning model (YOLOv8)
- 📊 High accuracy with optimized dataset

---

## 🛠 Technologies Used

- Python
- YOLOv8 (Ultralytics)
- OpenCV
- PyTorch
- Roboflow / Custom Dataset
- VS Code

---

## 📂 Project Structure


Indoor-fire-and-smoke-detection/
│
├── data/ # Dataset folder
│ ├── train/
│ ├── valid/
│ └── test/
│
├── train_yolo.py # Training script
├── data.yaml # Dataset configuration
├── requirements.txt # Dependencies
├── .gitignore
└── README.md


---

## 📊 Model Training

The model is trained using YOLOv8:

```python
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="data.yaml",
    epochs=50,
    imgsz=640
)
🧪 Detection
results = model("test.jpg")
results.show()

The output includes:

Bounding Box

Confidence Score

Class Label (Fire / Smoke)

📈 Evaluation Metrics

mAP (Mean Average Precision)

Precision

Recall

F1-Score

⚠ Challenges

False detection due to lighting conditions

Smoke-like fog detection

Small fire detection

Solutions:

Data augmentation

Multi-modal integration with sensors

Increasing dataset diversity

🔮 Future Enhancements

🔔 Alarm integration

📱 Mobile app alert system

☁ Cloud deployment

📡 IoT sensor integration

🎥 Live CCTV integration

📥 Installation

Clone the repository:

git clone https://github.com/sinchana1408/Indoor-fire-and-smoke-detection-.git

Create virtual environment:

python -m venv yolo_env

Activate environment:

yolo_env\Scripts\activate

Install dependencies:

pip install -r requirements.txt
🎯 Conclusion

This project demonstrates the application of deep learning for real-time indoor fire and smoke detection using YOLOv8. It can be extended into a complete fire emergency alert system with sensor integration and cloud monitoring.

👩‍💻 Author

Sinchana Shivanand


---

# ✅ After Creating README

Run:

```bash
git add README.md
git commit -m "Added project README"
git push
