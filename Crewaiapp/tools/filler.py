from PIL import Image, ImageDraw, ImageFont
import os

class FormFiller:
    def __init__(self, form_path):
        self.form_path = form_path

    def fill_form_with_data(self, data):
        # Load the ITR form image
        img = Image.open(self.form_path)
        draw = ImageDraw.Draw(img)

        # Load a font (make sure arial.ttf is available in your system)
        font = ImageFont.truetype("arial.ttf", 16)

        # Define positions for each field on the form
        positions = {
            'PAN': (100, 150),
            'First Name': (200, 150),
            'Middle Name': (200, 180),
            'Last Name': (200, 210),
            'Date of Birth': (400, 150),
            'Aadhaar Number': (600, 150),
            'Mobile Number': (100, 300),
            'Email Address': (100, 330),
        }

        # Overlay the text into the form
        draw.text(positions['PAN'], data['PAN'], font=font, fill="black")
        draw.text(positions['First Name'], data['First Name'], font=font, fill="black")
        draw.text(positions['Middle Name'], data['Middle Name'], font=font, fill="black")
        draw.text(positions['Last Name'], data['Last Name'], font=font, fill="black")
        draw.text(positions['Date of Birth'], data['Date of Birth'], font=font, fill="black")
        draw.text(positions['Aadhaar Number'], data['Aadhaar Number'], font=font, fill="black")
        draw.text(positions['Mobile Number'], data['Mobile Number'], font=font, fill="black")
        draw.text(positions['Email Address'], data['Email Address'], font=font, fill="black")

        # Save the modified image
        output_path = './data/filled/filled_ITR_form.png'
        img.save(output_path)
        return output_path
