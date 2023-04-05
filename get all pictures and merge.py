import os
import requests
from bs4 import BeautifulSoup
from PIL import Image
from PyPDF2 import PdfReader, PdfMerger

# Set the URL of the website to crawl
url = "https://w2.kumodesugananika.com/manga/kumo-desu-ga-nani-ka-chapter-0/"

# Use requests to fetch the webpage content
response = requests.get(url)

# Use BeautifulSoup to parse the HTML content and find all images in the div with class "separator"
soup = BeautifulSoup(response.content, "html.parser")
images = soup.select('div.separator img')

# Download each image and save it to disk
for i, image in enumerate(images):
    image_url = image['src']
    image_data = requests.get(image_url).content
    with open(f"image{i}.jpg", "wb") as f:
        f.write(image_data)

# Convert the images to PDF format
pdfs = []
for i in range(len(images)):
    image_file = f"image{i}.jpg"
    with Image.open(image_file) as img:
        pdf_file = f"image{i}.pdf"
        img.save(pdf_file, "PDF")
        pdfs.append(pdf_file)

# Merge the PDF files into a single document
# create a PdfMerger object
merger = PdfMerger()

# add PDF files to the merger
with open('merged.pdf', 'wb') as output:
    merger.write(output)
for pdf in pdfs:
    with open(pdf, 'rb') as open_pdf:
        merger.append(PdfReader(open_pdf))
merged_pdf = "output.pdf"
with open(merged_pdf, "wb") as f:
    merger.write(f)


# Clean up the temporary image and PDF files
for i in range(len(images)):
    os.remove(f"image{i}.jpg")
    os.remove(f"image{i}.pdf")


os.remove("merged.pdf")
