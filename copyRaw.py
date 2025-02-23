from bs4 import BeautifulSoup
from docx import Document
import requests
import pyperclip  # To copy text to clipboard
import os

# URL of the webpage
page_url = input("Enter URL: ")
print("What is your starting chapter number?")
chap_lower = int(float(input("\tEnter integer: ")))
print("What is your ending chapter number?")
chap_upper = int(float(input("\tEnter integer: ")))
print("How many lines from the top of the page do you want to exclude? ")
page_lower = int(float(input("\tEnter integer: ")))
print("How many lines from the bottom of the page do you want to exclude? ")
page_upper = int(float(input("\tEnter integer: "))) * -1
print("What name you want your output folder to have? ")
path = input("\tEnter string: ")
print()

# url = f"https://www.fortuneeternal.com/novel/solo-leveling-ragnarok-raw-novel/chapter-"
# chap_lower = 169
# chap_upper = 308
# page_lower = 728
# page_upper = -382
# path = ".\\SLR"

os.makedirs(path, exist_ok=True)
for i in range(chap_lower, chap_upper + 1):
    # edit this part for specifi websites
    chap_url = f"{page_url}{i}/"

    # Fetch the page content
    response = requests.get(chap_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        # Extract all text from the page
        page = soup.get_text()
        page = page.split("\n")
        text = [line for line in page if line != ""][page_lower:page_upper]
        output = f"{path}\\{i-1}.docx"
        document = Document()
        for line in text:
            document.add_paragraph(line)
        document.save(output)
        print(f"[*] Copied [Chapter {i-1}] successfully.")

    else:
        print(f"[*]Failed to retrieve the page. Status code: {response.status_code}")
        print(f"[*]You might want to modify the script or the URL is invalid.")
