import os
import requests
from bs4 import BeautifulSoup
from PIL import Image
from PyPDF2 import PdfReader, PdfMerger

# Send a request to the website and get the HTML content
url = "https://w2.kumodesugananika.com/"
response = requests.get(url)
html_content = response.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all li tags in the HTML
second_soup = soup.select("ul.su-posts")[0]
li_tags = second_soup.find_all('li')

# Loop through each li tag and extract the href and text of the a tag inside it
for li_tag in li_tags:
    # Extract href and text of the a tag
    a_tag = li_tag.find('a')
    href = a_tag['href'] if a_tag and 'href' in a_tag.attrs else None
    text = a_tag.text.strip().replace("?", "").replace(":", "") if a_tag else None

    new_folder_path = f"Kumo Desu ga, Nani ka\\{text}"
    os.makedirs(new_folder_path)

    # Set the URL of the website to crawl
    url = href

    # Use requests to fetch the webpage content
    response = requests.get(url)

    # Use BeautifulSoup to parse the HTML content and find all images in the div with class "separator"
    soup = BeautifulSoup(response.content, "html.parser")
    images = soup.select('div.separator img')

    if len(images)==0:
        images = soup.select('figure.aligncenter img')

    # Download each image and save it to disk
    for i, image in enumerate(images):
        image_url = image['src']
        image_data = requests.get(image_url).content
        with open(os.path.join(new_folder_path, f"image{i}.jpg"), "wb") as f:
            f.write(image_data)

    # Convert the images to PDF format
    pdfs = []
    for i in range(len(images)):
        image_file = f"image{i}.jpg"
        with Image.open(os.path.join(new_folder_path, image_file)) as img:
            pdf_file = f"{new_folder_path}\\image{i}.pdf"
            img.save(pdf_file, "PDF")
            pdfs.append(pdf_file)

    # Merge the PDF files into a single document
    # create a PdfMerger object
    merger = PdfMerger()

    # add PDF files to the merger
    with open(os.path.join(new_folder_path, 'merged.pdf'), 'wb') as output:
        merger.write(output)
    for pdf in pdfs:
        with open(pdf, 'rb') as open_pdf:
            merger.append(PdfReader(open_pdf))
    merged_pdf = f"{text}.pdf"
    with open(os.path.join(new_folder_path, merged_pdf), "wb") as f:
        merger.write(f)

    # Clean up the temporary image and PDF files
    for i in range(len(images)):
        os.remove(f"{new_folder_path}//image{i}.jpg")
        os.remove(f"{new_folder_path}//image{i}.pdf")

    os.remove(f"{new_folder_path}//merged.pdf")