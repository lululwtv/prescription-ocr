import cv2
import numpy as np
from PIL import Image
from parser import PrescriptionParser
from surya.ocr import run_ocr
from surya.model.detection import segformer
from surya.model.recognition.model import load_model
from surya.model.recognition.processor import load_processor

def extract(file_path):
    # Open the image file
    image = Image.open(file_path)

    # Preprocess the image
    # processed_image = preprocess_image(image)

    langs = ["en"] # Replace with your languages
    det_processor, det_model = segformer.load_processor(), segformer.load_model()
    rec_model, rec_processor = load_model(), load_processor()

    predictions = run_ocr([image], [langs], det_model, det_processor, rec_model, rec_processor)

    text_lines = [line.text for line in predictions[0].text_lines]
    combined_text = "\n".join(text_lines)
    print(text_lines)
    print(combined_text)

    # Use the PrescriptionParser to extract fields as needed
    extracted_data = PrescriptionParser(combined_text).parse()
    return extracted_data

# def preprocess_image(img):
#     gray = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
#     resized = cv2.resize(gray, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
#     # processed_image = cv2.adaptiveThreshold(
#     #     resized,
#     #     255,
#     #     cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#     #     cv2.THRESH_BINARY,
#     #     65, # block size 
#     #     13  # constant
#     # )
#     return resized

if __name__ == "__main__":
    # Example usage with a sample PNG file
    data = extract("backend/resources/1_omeprazole.png")
    for key, value in data.items():
        print(f"{key}: {value}")