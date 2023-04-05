import requests
from bs4 import BeautifulSoup

# Send a request to the website and get the HTML content
url = "https://w2.kumodesugananika.com/" # Replace with the URL of the website you want to crawl
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
    text = a_tag.text.strip() if a_tag else None

    # Print the href and text for each li tag
    print("Href: ", href)
    print("Text: ", text)
    print("-----------")
