import unittest
from parser import PrescriptionParser

class TestPrescriptionParser(unittest.TestCase):

    def setUp(self):
        self.parser = PrescriptionParser

    def test_label_1(self):
        text = """
        OMEPRAZOLE 20MG					       7 CAPSULES
        TAKE 1 CAPSULE 4 TIMES DAILY
        To take with Diclofenac.
        May be taken with or after food.
        For Gastritis.
        May cause drowsiness.

        26/12/2023
        """
        expected_output = {
            "medicine_name": "OMEPRAZOLE 20MG",
            "quantity": "7 CAPSULES",
            "dosage": "1 CAPSULE",
            "frequency": "4 TIMES DAILY",
            "taken_with": "Diclofenac",
            "not_taken_with": "Nil",
            "food": "taken with or after food",
            "reason": "Gastritis",
            "side_effects": "drowsiness",
            "prescription_date": "26/12/2023"
        }
        pp = self.parser(text)
        self.assertEqual(pp.parse(), expected_output)

    def test_label_2(self):
        text = """
        METFORMIN 850MG					      280 TABLETS
        TAKE 1 TABLET 2 TIMES DAILY
        To take with Diclofenac.
        May be taken after food.
        Do not take with alcohol.
        For Type 2 Diabetes.

        18/07/2024
        """
        expected_output = {
            "medicine_name": "METFORMIN 850MG",
            "quantity": "280 TABLETS",
            "dosage": "1 TABLET",
            "frequency": "2 TIMES DAILY",
            "taken_with": "Diclofenac",
            "not_taken_with": "alcohol",
            "food": "taken after food",
            "reason": "Type 2 Diabetes",
            "side_effects": "Nil",
            "prescription_date": "18/07/2024"
        }
        pp = self.parser(text)
        self.assertEqual(pp.parse(), expected_output)

    def test_label_3(self):
        text = """
        GLIPIZIDE 5MG					               120 TABLETS
        TAKE 1 TABLET 2 TIMES DAILY
        To take with sugary foods if giddy.
        Do not take with alcohol.
        May be taken before food.
        For Diabetes Mellitus.

        18/07/2024
        """
        expected_output = {
            "medicine_name": "GLIPIZIDE 5MG",
            "quantity": "120 TABLETS",
            "dosage": "1 TABLET",
            "frequency": "2 TIMES DAILY",
            "taken_with": "sugary foods if giddy",
            "not_taken_with": "alcohol",
            "food": "taken before food",
            "reason": "Diabetes Mellitus",
            "side_effects": "Nil",
            "prescription_date": "18/07/2024"
        }
        pp = self.parser(text)
        self.assertEqual(pp.parse(), expected_output)

    def test_label_4(self):
        text = """
        ATORVASTATIN 20MG				        90 TABLETS
        TAKE 1 TABLET 1 TIME DAILY
        Avoid if pregnant.
        May be taken with or without food.
        For High Cholesterol.

        18/07/2024
        """
        expected_output = {
            "medicine_name": "ATORVASTATIN 20MG",
            "quantity": "90 TABLETS",
            "dosage": "1 TABLET",
            "frequency": "1 TIME DAILY",
            "taken_with": "Nil",
            "not_taken_with": "pregnant",
            "food": "taken with or without food",
            "reason": "High Cholesterol",
            "side_effects": "Nil",
            "prescription_date": "18/07/2024"
        }
        pp = self.parser(text)
        self.assertEqual(pp.parse(), expected_output)

    def test_label_5(self):
        text = """
        NIFEDIPINE 60MG				               230 TABLETS
        TAKE 1 TABLET 2 TIMES DAILY
        Avoid if pregnant or breastfeeding.
        May be taken with or without food.
        For pain relief.

        18/07/2024
        """
        expected_output = {
            "medicine_name": "NIFEDIPINE 60MG",
            "quantity": "230 TABLETS",
            "dosage": "1 TABLET",
            "frequency": "2 TIMES DAILY",
            "taken_with": "Nil",
            "not_taken_with": "pregnant or breastfeeding",
            "food": "taken with or without food",
            "reason": "pain relief",
            "side_effects": "Nil",
            "prescription_date": "18/07/2024"
        }
        pp = self.parser(text)
        self.assertEqual(pp.parse(), expected_output)

    def test_label_6(self):
        text = """
        CO-AMOXICLAV 1G                                                 14 TABLETS
        TAKE 1 TABLET 2 TIMES DAILY
        May be taken with or after food.
        For bacterial infections.

        18/07/2024
        """
        expected_output = {
            "medicine_name": "CO-AMOXICLAV 1G",
            "quantity": "14 TABLETS",
            "dosage": "1 TABLET",
            "frequency": "2 TIMES DAILY",
            "taken_with": "Nil",
            "not_taken_with": "Nil",
            "food": "taken with or after food",
            "reason": "bacterial infections",
            "side_effects": "Nil",
            "prescription_date": "18/07/2024"
        }
        pp = self.parser(text)
        self.assertEqual(pp.parse(), expected_output)


if __name__ == "__main__":
    unittest.main()
