import pandas as pd
from jinja2 import Template
from weasyprint import HTML
import os
import base64

# Function to encode images to Base64
def encode_image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return f"data:image/png;base64,{base64.b64encode(img_file.read()).decode('utf-8')}"

# Function to read CSV file
def read_csv(file_path):
    return pd.read_csv(file_path)

# Updated A4-sized HTML template with smaller font size for placeholders
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Certificate</title>
    <style>
        @page {
            size: A4 landscape;
            margin: 0;
        }
        body {
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100%;
            height: 100%;
            background-color: #f5f5f5;
        }
        .border-container {
            position: absolute;
            width: 100%;
            height: 100%;
            border: 20px solid #444;
            box-sizing: border-box;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
        }
        .certificate {
            width: 100%;
            height: 100%;
            background-image: url('{{ background_image_base64 }}');
            background-size: cover;
            background-position: center;
            text-align: center;
            color: #fff;
            box-sizing: border-box;
            padding: 30px;
        }
        .header img { 
        margin-bottom: -10px; /* Adjust this value to move it upwards */ 
        }
        h1 {
            font-size: 2.5em;
            margin: 10px 0;
            color: #007BFF;
            text-shadow: 2px 2px 4px #000000; /* Subtle shadow for gold */
        }
        h3 {
            font-size: 1.5em;
            color: #C0C0C0;
            margin: 10px 0;
        }
        p {
            font-size: 1.2em;
            margin: 5px 0;
            color: #FFD57E;
        }
        .details {
            font-size: 1.5em;
            font-weight: bold;
            color: #FFD700;
        }
        .usn {
            color: #007ACC; /* Darker, professional blue for USN */
        }
        .footer {
            position: absolute;
            bottom: 40px;
            width: 90%;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .date {
            font-size: 1em;
            color: #C0C0C0; /* Silver */
            margin-left: 20px; /* Left margin for better alignment */
            border: 1px solid #C0C0C0; /* Subtle border for the signature box */
            padding: 5px;
            display: inline-block;
        }
        .signature {
            border: 1px solid #C0C0C0; /* Subtle border for the signature box */
            padding: 5px;
            display: inline-block;
        }
        .signature img {
            max-height: 55px;
        }
    </style>
</head>
<body>
    <div class="border-container">
        <div class="certificate">
            <div class="header">
                <img src="{{ org_logo_base64 }}" alt="Organization Logo" style="max-width: 250px;">
                <p style="color:#00BFFF; font-weight:bold;">www.mtdn.co.in</p>
            </div>
            <h1 style="color: #FFD700;">Certificate of Achievement</h1>
            <p>&nbsp;</p>
           
            <h3 style="color: #C0C0C0;">This certifies that</h3>
            <p class="details" style="color: #FFD700;">{{ name }} <span style="color: #007ACC;">({{ usn }})</span></p>

            <p>&nbsp;</p>
            <p style="font-size: 1.2em; color: #FFA500;">has successfully completed the training and workshop of 10 days held in December 2024.</p>

            <p style="font-size: 1.2em; color: #FFA500;">Focusing on the core principles and hands-on techniques in Python programming with databases.</p>
            <p>
            <div class="footer">
                <p class="date" style="font-size: 1em; color: #D3D3D3;">Date: 19th December 2024</p>
                <div class="signature">
                    <img src="{{ signature_image_base64 }}" alt="Signature">
                    <p style="color: #C0C0C0; font-size: 1em;">Nithin Neelakanta Rao<br><span style="font-size: smaller;">MTD Founder</span></p>                </div>
            </div>
        </div>
    </div>
</body>
</html>

"""

# Function to generate certificates
def generate_certificate(data, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    
    # Encode images to Base64
    background_image_base64 = encode_image_to_base64(r"C:\Users\Asus\Downloads\2KE23CS149\Certificate_Generation\assests\certificate_template.png")
    org_logo_base64 = encode_image_to_base64(r"C:\Users\Asus\Downloads\2KE23CS149\Certificate_Generation\assests\logo.png")
    signature_image_base64 = encode_image_to_base64(r"C:\Users\Asus\Downloads\2KE23CS149\Certificate_Generation\assests\sign.jpg")
    
    for index, row in data.iterrows():
        name = row['name']
        usn = row['usn']
        
        # Render HTML
        template = Template(html_template)
        rendered_html = template.render(
            name=name,
            usn=usn,
            background_image_base64=background_image_base64,
            org_logo_base64=org_logo_base64,
            signature_image_base64=signature_image_base64
        )
        
        # Save as PDF
        pdf_file_path = os.path.join(output_dir, f"{name}_{usn}.pdf")
        HTML(string=rendered_html, base_url=os.getcwd()).write_pdf(pdf_file_path)
        print(f"Generated: {pdf_file_path}")

# Main function
if __name__ == "__main__":
    input_csv = r"C:\Users\Asus\Downloads\2KE23CS149\Certificate_Generation\assests\data.csv" # Path to CSV file
    output_directory = "certificates"  # Output directory
    
    # Read data and generate certificates
    data = read_csv(input_csv)
    generate_certificate(data, output_directory)