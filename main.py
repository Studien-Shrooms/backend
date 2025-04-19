from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os, shutil

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200", 
                   "https://thankful-desert-06810b503.6.azurestaticapps.net",
                   "https://thankful-desert-06810b503.6.azurestaticapps.net/"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def translation(filepath: str, language: str) -> str:
    #hier dann azure oder so?
    return f"Dies ist eine automatische Übersetzung von {os.path.basename(filepath)} für Sprache '{language}'."

@app.post("/upload")
async def upload_video(file: UploadFile = File(...), language: str = Form(...)):
    filepath = os.path.join(UPLOAD_DIR, file.filename)

    try:
        with open(filepath, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        translation_result = translation(filepath, language)
        os.remove(filepath)
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

    return JSONResponse(content={
        "message": "Upload erfolgreich",
        "filename": file.filename,
        "language": language,
        "translation": translation_result
    })
