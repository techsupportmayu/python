import pdfkit

# URL of the webpage you want to convert to PDF
url = "https://example.com"

# Path to the wkhtmltopdf executable
# Make sure to provide the correct path to the executable
path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'

# Configure pdfkit options
options = {
    'page-size': 'A4',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
}

# Convert URL to PDF
pdfkit.from_url(url, 'output.pdf', configuration=pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf), options=options)

print("PDF created successfully!")
