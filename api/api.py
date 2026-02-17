from fastapi import FastAPI, UploadFile, File
import shutil
import json

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "OK"}

@app.post("/analyze_video")
async def analyze_video(file: UploadFile = File(...)):
    video_path = f"temp_{file.filename}"

    with open(video_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    with open("results.json") as f:
        results = json.load(f)

    return results
