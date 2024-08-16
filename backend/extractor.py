from PIL import Image
from parser import PrescriptionParser
from surya.ocr import run_ocr
from surya.model.detection import segformer
from surya.model.recognition.model import load_model
from surya.model.recognition.processor import load_processor

def initialize_ocr_models():
    det_processor, det_model = segformer.load_processor(), segformer.load_model()
    rec_model, rec_processor = load_model(), load_processor()
    return det_processor, det_model, rec_model, rec_processor

def extract(file_path, det_processor, det_model, rec_model, rec_processor):
    image = Image.open(file_path)

    predictions = run_ocr([image], [["en"]], det_model, det_processor, rec_model, rec_processor)

    text_lines = [line.text for line in predictions[0].text_lines]
    combined_text = "\n".join(text_lines)
    print(text_lines)
    print(combined_text)

    # Use the PrescriptionParser to extract fields as needed
    extracted_data = PrescriptionParser(combined_text).parse()
    return extracted_data

if __name__ == "__main__":
    det_processor, det_model, rec_model, rec_processor = initialize_ocr_models()
    data = extract("backend/resources/1_omeprazole.png", det_processor, det_model, rec_model, rec_processor)
    for key, value in data.items():
        print(f"{key}: {value}")