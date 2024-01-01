import requests 
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import os

url = 'https://www.espn.com/nba/story/_/id/33297498/the-nba-75th-anniversary-team-ranked-where-76-basketball-legends-check-our-list'

max_width = 500
response = requests.get(url)
html = response.text
print(html)
soup = BeautifulSoup(html, 'html.parser')
img_tags = soup.find_all('img')
print(img_tags)
image_dir = "images"
if not os.path.exists(image_dir):
    os.makedirs(image_dir)

for index, img in enumerate(img_tags):
    img_url = img['src']
    img_response = requests.get(img_url)
    img_data = BytesIO(img_response.content)
    aspect_ratio = image.width / image.height
    new_height = int(max_width / aspect_ratio)

    image = image.resize((max_width, new_height))
    img_name = f"{index}.png"
    save_path = os.path.join(image_dir, img_name)
    
    image.save(f"resized_image_{img_tags.index(img)}.png")