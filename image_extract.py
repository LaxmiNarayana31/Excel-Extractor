import os
import pandas as pd
import requests
import re  # Import the regular expression module

# Step 1: Read the CSV File
file_path = 'New GB sheet.csv'
df = pd.read_csv(file_path)

# Step 2: Extract Image URLs and Item Names

df = df[df['item_image'].str.startswith('http')]
image_urls = df['item_image']
item_names = df['item_name']

# Function to sanitize file names
def sanitize_filename(filename):
    # Replace invalid characters with underscores
    return re.sub(r'[\\/*?:"<>|]', '_', filename)

# Step 3: Create a local directory to save images
local_dir = os.path.join(os.getcwd(), "New_sheet_images")
if not os.path.exists(local_dir):
    os.makedirs(local_dir)

# Function to download and save images
def download_image(url, local_path):
    response = requests.get(url)
    if response.status_code == 200: 
        with open(local_path, 'wb') as file:
            file.write(response.content)
        print(f"Image downloaded: {local_path}")
    else:
        print(f"Failed to download image from {url}")

# Step 4: Download and save images using sanitized item names 
for url, name in zip(image_urls, item_names):
    file_extension = url.split('.')[-1]  # Get the file extension from the URL
    sanitized_name = sanitize_filename(name)  # Sanitize the item name
    local_path = os.path.join(local_dir, f"{sanitized_name}.{file_extension}")
    download_image(url, local_path)
