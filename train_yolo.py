# train_yolo.py
from ultralytics import YOLO

# 1️⃣ Load a pre-trained YOLOv8 base model (Nano versPython: Select Interpreterion)
model = YOLO("yolov8n.pt")   # or yolov8s.pt for slightly bigger model

# 2️⃣ Train on your dataset
model.train(
    data="data/data.yaml",  # path to your YAML file
    epochs=50,                      # number of training epochs
    imgsz=640,                      # input image size
    batch=16,                       # batch size (adjust based on GPU)
    name="fire_yolo_v8_train",      # folder name for saved run
    workers=4                       # number of workers for data loading
)
