from fastapi import FastAPI, UploadFile, File
import uvicorn
from extractor import extract, initialize_ocr_models
import uuid
import os

det_processor, det_model, rec_model, rec_processor = initialize_ocr_models()

app = FastAPI()

@app.post("/extract_from_doc")
def extract_from_doc(file: UploadFile = File(...)):
    content = file.file.read()

    # Save the uploaded file
    FILE_PATH = "./uploads/" + str(uuid.uuid4()) + ".png"
    with open(FILE_PATH, "wb") as f:
        f.write(content)

    # Extract data from the uploaded file
    try:
        data = extract(FILE_PATH, det_processor, det_model, rec_model, rec_processor)
    except Exception as e:
        data = {
            'error': str(e)
        }

    # Remove the uploaded file
    if os.path.exists(FILE_PATH):
        os.remove(FILE_PATH)

    return data


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8501)
