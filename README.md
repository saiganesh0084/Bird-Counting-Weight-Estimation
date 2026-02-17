# Bird Counting and Weight Estimation from Poultry CCTV Video
## 📌 Overview

This project implements a prototype system for bird counting and weight estimation using fixed-camera poultry CCTV footage.

The pipeline includes:

- Video Frame Extraction
- Data Labeling using Roboflow
- YOLOv8 Model Training
- Multi-Object Tracking (ByteTrack)
- Bird Counting Over Time
- Bounding Box-Based Weight Proxy
- Annotated Video & JSON Outputs

## 🎯 Approach
**1️⃣ Frame Extraction**

The input CCTV video was divided into frames to create a training dataset.

**2️⃣ Data Labeling (Roboflow)**

Frames were labeled using Roboflow.

- Single class: chicken
- Bounding box annotations
- Dataset exported in YOLO format

**3️⃣ Model Training**

A YOLOv8 detector was trained on the labeled dataset to improve domain-specific detection accuracy.

**4️⃣ Detection & Tracking**

- Bird detection via a trained YOLOv8 model
- Stable tracking IDs using ByteTrack

Tracking ensures:

✔ Reduced double-counting

✔ Identity persistence

✔ Occlusion tolerance

**5️⃣ Bird Counting**

Bird counts are computed per frame using active tracking IDs:
```
Count = Number of unique tracked IDs
```
**6️⃣ Weight Estimation (Proxy)**

True weight labels unavailable.

Weight estimation implemented using bounding box area:

```
Weight Proxy ∝ Box Width × Box Height
```

This serves as a ***relative weight index***.

### 📊 Outputs

✔ Annotated Video (Bounding Boxes + Tracking IDs + Counts)

✔ Structured JSON Results


### ⚠ Limitations

Conversion of weight proxy into grams requires:

- Camera calibration OR
- Labeled bird weight dataset

## 🔮 Ongoing Work

This project is under active development.

Future improvements include:

- Larger labeled dataset
- Improved detector accuracy
- Calibration-based weight estimation

Expanding the dataset and refining the model require significant labeling and training time.

## ✅ Summary

End-to-end ML pipeline:
```
Video → Frames → Labeling → Training → Detection → Tracking → Analytics
```