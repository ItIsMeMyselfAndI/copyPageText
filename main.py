import requests
from bs4 import BeautifulSoup
import pyperclip  # To copy text to clipboard

# URL of the webpage
i = 2
url = f"https://www.fortuneeternal.com/novel/solo-leveling-ragnarok-raw-novel/chapter-18{i}/"

# Fetch the page content
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract all text from the page
    page = soup.get_text()

    # Copy text to clipboard
    # pyperclip.copy(text)
    # print("Webpage text copied to clipboard!")
    page = page.split("\n")
    text = []
    for line in page:
        if line != "":
            text.append(line)
    text = text[728:-383]
    for i, line in enumerate(text):
        print(i, line)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
