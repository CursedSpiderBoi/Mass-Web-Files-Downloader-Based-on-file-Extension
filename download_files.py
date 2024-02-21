import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

def download_files_with_extension(website_link, extension, output_directory):
    # Fetch the webpage content
    response = requests.get(website_link)
    if response.status_code != 200:
        print("Error: Unable to fetch webpage")
        return

    # Parse HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Get all <a> tags
    hrefs = soup.find_all('a')

    # Filter hrefs by extension
    filtered_hrefs = [href['href'] for href in hrefs if href.get('href') and href['href'].endswith(extension)]

    if not filtered_hrefs:
        print("No files found with the specified extension")
        return

    # Create a directory based on the website link if it doesn't exist
    website_name = urlparse(website_link).netloc
    output_folder = os.path.join(output_directory, website_name)
    os.makedirs(output_folder, exist_ok=True)

    # Download each file and save in the folder
    for href in filtered_hrefs:
        absolute_url = urljoin(website_link, href)
        filename = urlparse(absolute_url).path.split('/')[-1]
        file_path = os.path.join(output_folder, filename)
        try:
            response = requests.get(absolute_url)
            if response.status_code == 200:
                with open(file_path, 'wb') as file:
                    file.write(response.content)
                print(f"Downloaded: {filename}")
            else:
                print(f"Failed to download: {filename}")
        except Exception as e:
            print(f"Error downloading {filename}: {e}")

# Prompt user for website link, file extension, and output directory
website_link = input("Enter the website link: ")
extension = input("Enter the file extension (e.g., .pdf): ")
output_directory = input("Enter the output directory: ")

# Call the function
download_files_with_extension(website_link, extension, output_directory)
