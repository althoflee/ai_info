#%%
from ultralytics import YOLO

# Load a pretrained YOLO11n model
model = YOLO("yolo11x.pt")

# Run inference on 'bus.jpg' with arguments
model.predict("ive.jpg", save=True, imgsz=320, conf=0.5)
# %%
