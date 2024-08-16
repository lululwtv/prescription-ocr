import re

class PrescriptionParser:
    def __init__(self, text):
        self.text = text
        
    def parse(self):
        return {
            "medicine_name": self.get_field("medicine_name"),
            "quantity": self.get_field("quantity"),
            "dosage": self.get_field("dosage"),
            "frequency": self.get_field("frequency"),
            "taken_with": self.get_field("taken_with"),
            "not_taken_with": self.get_field("not_taken_with"),
            "food": self.get_field("food"),
            "reason": self.get_field("reason"),
            "side_effects": self.get_field("side_effects"),
            "prescription_date": self.get_field("prescription_date"),
        }

    def get_field(self, field_name):
        pattern_dict = {
            "medicine_name": {"pattern": r"([A-Z\s]+[0-9]+(?:MG|G))", "flags": re.IGNORECASE},
            "quantity": {"pattern": r"(\d+\s+\w+)", "flags": re.IGNORECASE},
            "dosage": {"pattern": r"TAKE\s+(\d+\s+\w+)", "flags": re.IGNORECASE},
            "frequency": {"pattern": r"(\d+\s+TIMES\s+DAILY|1\s+TIME\s+DAILY)", "flags": re.IGNORECASE},
            "taken_with": {"pattern": r"To\s+take\s+with\s+(.*?)(?:\n|$)", "flags": re.IGNORECASE},
            "not_taken_with": {"pattern": r"(?:Do\s+not\s+take|avoid)\s+(?:with|if)\s+(.*?)(?:\n|$)", "flags": re.IGNORECASE},
            "food": {"pattern": r"May\s+be\s+taken\s+(.*?)(?:\n|$)", "flags": re.IGNORECASE},
            "reason": {"pattern": r"For\s+(.*?)(?:\n|$)", "flags": re.IGNORECASE},
            "side_effects": {"pattern": r"May\s+cause\s+(.*?)(?:\n|$)", "flags": re.IGNORECASE},
            "prescription_date": {"pattern": r"(\d{2}/\d{2}/\d{4})", "flags": re.IGNORECASE},
        }

        pattern_object = pattern_dict.get(field_name)
        if pattern_object:
            matches = re.findall(pattern_object["pattern"], self.text, flags=pattern_object["flags"])
            if matches:
                result = ' '.join(matches[0]).strip().title() if isinstance(matches[0], tuple) else matches[0].strip().title()

                # Add a space between the number and "MG" in the medicine name
                if field_name == "medicine_name":
                    result = re.sub(r"(\d+)(mg|g)", r"\1 \2", result, flags=re.IGNORECASE)

                return result
        return "Nil"

if __name__ == "__main__":
    document_text = """
METFORMIN 850MG					      
280 TABLETS
TAKE 1 TABLET 2 TIMES DAILY
To take with Diclofenac
May be taken after food
Do not take with alcohol
For Type 2 Diabetes
18/07/2024
"""

    pp = PrescriptionParser(document_text)
    for key, value in pp.parse().items():
        print(f"{key}: {value}")
