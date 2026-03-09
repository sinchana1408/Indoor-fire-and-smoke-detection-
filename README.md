
# Indoor Fire and Smoke Detection using YOLOv8

## Project Overview

This project implements a real-time Indoor Fire and Smoke Detection System using YOLOv8 (You Only Look Once version 8). The model is trained to detect fire and smoke in indoor environments using computer vision and deep learning.

The system can be used for:
- Early fire detection
- CCTV monitoring systems
- Smart building safety systems
- Automated fire alert systems

---

## Features

- Detects Fire
- Detects Smoke
- Real-time object detection
- Bounding box prediction with confidence score
- Deep learning model (YOLOv8)
- High accuracy with optimized dataset

---

## Technologies Used

- Python
- YOLOv8 (Ultralytics)
- OpenCV
- PyTorch
- Roboflow / Custom Dataset
- VS Code

---

##  Project Structure


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

## Model Training

The model is trained using YOLOv8:

```python
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="data.yaml",
    epochs=50,
    imgsz=640
)
 Detection
results = model("test.jpg")
results.show()


Run:

```bash
git add README.md
git commit -m "Added project README"
git push
