from bs4 import BeautifulSoup
from docx import Document
import requests
import pyperclip  # To copy text to clipboard
import os

# URL of the webpage
path = ".\\SLR"
os.makedirs(path, exist_ok=True)

for i in range(180, 308):
    url = f"https://www.fortuneeternal.com/novel/solo-leveling-ragnarok-raw-novel/chapter-{i}/"

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
        text = [line for line in page if line != ""][728:-382]
        # for j, line in enumerate(text):
        #     print(j, line)
        output = f"{path}\\{i-1}.docx"
        document = Document()
        for line in text:
            document.add_paragraph(line)
        document.save(output)
        print(f"[*] Copied [Chapter {i-1}] successfully.")

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
