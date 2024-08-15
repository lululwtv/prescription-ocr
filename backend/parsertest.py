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
            "medicine_name": "Omeprazole 20Mg",
            "quantity": "7 Capsules",
            "dosage": "1 Capsule",
            "frequency": "4 Times Daily",
            "taken_with": "Diclofenac",
            "not_taken_with": "Nil",
            "food": "Taken With Or After Food",
            "reason": "Gastritis",
            "side_effects": "Drowsiness",
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
            "medicine_name": "Metformin 850Mg",
            "quantity": "280 Tablets",
            "dosage": "1 Tablet",
            "frequency": "2 Times Daily",
            "taken_with": "Diclofenac",
            "not_taken_with": "Alcohol",
            "food": "Taken After Food",
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
            "medicine_name": "Glipizide 5Mg",
            "quantity": "120 Tablets",
            "dosage": "1 Tablet",
            "frequency": "2 Times Daily",
            "taken_with": "Sugary Foods If Giddy",
            "not_taken_with": "Alcohol",
            "food": "Taken Before Food",
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
            "medicine_name": "Atorvastatin 20Mg",
            "quantity": "90 Tablets",
            "dosage": "1 Tablet",
            "frequency": "1 Time Daily",
            "taken_with": "Nil",
            "not_taken_with": "Pregnant",
            "food": "Taken With Or Without Food",
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
        For Pain Relief.

        18/07/2024
        """
        expected_output = {
            "medicine_name": "Nifedipine 60Mg",
            "quantity": "230 Tablets",
            "dosage": "1 Tablet",
            "frequency": "2 Times Daily",
            "taken_with": "Nil",
            "not_taken_with": "Pregnant Or Breastfeeding",
            "food": "Taken With Or Without Food",
            "reason": "Pain Relief",
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
        For Bacterial Infections.

        18/07/2024
        """
        expected_output = {
            "medicine_name": "Co-Amoxiclav 1G",
            "quantity": "14 Tablets",
            "dosage": "1 Tablet",
            "frequency": "2 Times Daily",
            "taken_with": "Nil",
            "not_taken_with": "Nil",
            "food": "Taken With Or After Food",
            "reason": "Bacterial Infections",
            "side_effects": "Nil",
            "prescription_date": "18/07/2024"
        }
        pp = self.parser(text)
        self.assertEqual(pp.parse(), expected_output)


if __name__ == "__main__":
    unittest.main()
