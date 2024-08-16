from PIL import Image
from parser import PrescriptionParser
from surya.ocr import run_ocr
from surya.model.detection import segformer
from surya.model.recognition.model import load_model
from surya.model.recognition.processor import load_processor

def extract(file_path):
    image = Image.open(file_path)

    langs = ["en"] 
    det_processor, det_model = segformer.load_processor(), segformer.load_model()
    rec_model, rec_processor = load_model(), load_processor()

    predictions = run_ocr([image], [langs], det_model, det_processor, rec_model, rec_processor)

    text_lines = [line.text for line in predictions[0].text_lines]
    combined_text = "\n".join(text_lines)
    print(text_lines)
    print(combined_text)

    # parse
    extracted_data = PrescriptionParser(combined_text).parse()
    return extracted_data

if __name__ == "__main__":
    data = extract("backend/resources/metformin.png")
    for key, value in data.items():
        print(f"{key}: {value}")