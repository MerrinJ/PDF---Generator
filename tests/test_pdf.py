import unittest
import os
from app.pdf import generate_pdf, SAVE_DIR

class TestGeneratePDF(unittest.TestCase):
    def setUp(self):
         if not os.path.exists(SAVE_DIR):
            os.makedirs(SAVE_DIR)
    
    def tearDown(self):
        for filename in os.listdir(SAVE_DIR):
            file_path = os.path.join(SAVE_DIR, filename)
            if os.path.isfile(file_path):
                os.unlink(file_path)
    
    def test_generate_pdf_success(self):
        heading = "Test Heading"
        subheading = "Test Subheading"
        table_data = [["Header1", "Header2"], ["Row1Col1", "Row1Col2"]]
        base_url = "http://localhost"
        
        pdf_url = generate_pdf(heading, subheading, table_data, base_url)
        
        self.assertTrue(os.path.isfile(os.path.join(SAVE_DIR, "test_heading_report.pdf")))
        self.assertEqual(pdf_url, f"{base_url}/generated_pdfs/test_heading_report.pdf")
    
    def test_generate_pdf_invalid_heading(self):
        with self.assertRaises(ValueError) as context:
            generate_pdf("", "Test Subheading", [["Header1"]], "http://localhost")
        self.assertTrue("Heading must be a non-empty string" in str(context.exception))

    def test_generate_pdf_invalid_table_data(self):
        with self.assertRaises(ValueError) as context:
            generate_pdf("Valid Heading", "Valid Subheading", "Invalid Table Data", "http://localhost")
        self.assertTrue("Table data must be a list of lists" in str(context.exception))

if __name__ == '__main__':
    unittest.main()
