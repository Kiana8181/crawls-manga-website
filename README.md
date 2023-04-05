# Image to PDF Converter

 This code is a Python script that crawls a website, downloads images from specific pages, converts them into PDF format, merges them into a single PDF document, and saves them to the local disk. Here is a breakdown of the code:

-***import statements***: The code imports various Python modules including os, requests, BeautifulSoup, PyPDF2, and PIL.

-***url variable***: The URL of the website to be crawled is stored in this variable.

-***Sending a request to the website***: The code uses the requests module to send a request to the website and retrieves its HTML content.

-***Parsing the HTML content***: The BeautifulSoup module is used to parse the HTML content and extract specific elements, in this case, all the li tags within the ul tag with the class "su-posts".

-***Looping through each li tag***: The code loops through each li tag and extracts the href and text of the a tag inside it.

-***Creating a new folder and downloading images***: If the href and text are not None, the code creates a new folder with the text as its name and downloads all the images from the page linked by the href into that folder.

-***Converting images to PDF format***: The code then converts all the downloaded images into PDF format using the PIL module.

-***Merging PDF files***: The code merges all the PDF files into a single document using the PyPDF2 module.

-***Cleaning up temporary files***: Finally, the code deletes all the temporary image and PDF files.

## Prerequisites

- Python 3.x
- Required Python modules:
  - beautifulsoup4
  - Pillow
  - PyPDF2
  - requests

You can install the required modules by running the following command:

`pip install -r requirements.txt`


## Usage

To use this script, follow these steps:

1. Clone this repository:

 `https://github.com/Kiana8181/crawls-manga-website.git`

2. Open the terminal in the cloned repository.

3. Run the following command to start the script:

 `python main.py`


The script will start crawling the website and downloading the images. Once it is done, it will convert the images to PDF format, merge them into a single PDF document, and save it to the local disk.

4. After the script is done, you will find the PDF document in the folder with the name of the page where the images were downloaded.



