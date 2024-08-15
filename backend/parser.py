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
            "medicine_name": {"pattern": r"([A-Z\-]+ [0-9]+(?:MG|G))", "flags": re.IGNORECASE},
            "quantity": {"pattern": r"(\d+ )\s*(TABLETS|CAPSULES)", "flags": re.IGNORECASE},
            "dosage": {"pattern": r"TAKE (\d+ [A-Z]+)\s", "flags": re.IGNORECASE},
            "frequency": {"pattern": r"(\d+ TIMES DAILY|1 TIME DAILY)", "flags": re.IGNORECASE},
            "taken_with": {"pattern": r"To take with (.*?)(?:\.|$)", "flags": re.IGNORECASE},
            "not_taken_with": {"pattern": r"(?:Do not take|avoid) (?:with|if) (.*?)(?:\.|$)", "flags": re.IGNORECASE},
            "food": {"pattern": r"May be (.*?food)", "flags": re.IGNORECASE},
            "reason": {"pattern": r"For (.*?)(?:\.|$)", "flags": re.IGNORECASE},
            "side_effects": {"pattern": r"May cause (.*?)(?:\.|$)", "flags": re.IGNORECASE},
            "prescription_date": {"pattern": r"(\d{2}/\d{2}/\d{4})", "flags": re.IGNORECASE},
        }

        pattern_object = pattern_dict.get(field_name)
        if pattern_object:
            matches = re.findall(pattern_object["pattern"], self.text, flags=pattern_object["flags"])
            if matches:
                return ''.join(matches[0]).strip()
        return "Nil"

if __name__ == "__main__":
    document_text = """
    CO-AMOXICLAV 1G                                         14 TABLETS
TAKE 1 TABLET 2 TIMES DAILY
May be taken with or after food.
For bacterial infections.



18/07/2024


    """

    pp = PrescriptionParser(document_text)
    for key, value in pp.parse().items():
        print(f"{key}: {value}")
