from fastapi import APIRouter, UploadFile, File
import shutil
import os

router = APIRouter()

ULOAD_DIR = "uploads"
os.makedirs(ULOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    file_location = os.path.join(ULOAD_DIR, file.filename)
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename, "status": "uploaded"}
