# Mass-Web-Files-Downloader-Based-on-file-Extension

This is a Python script that allows users to download files with a specific extension from a given website. The script fetches the webpage content, parses the HTML, filters the links by the specified file extension, and saves the files in a folder named after the website link.

## How to Use

### Requirements
- Python 3.x
- Requests library (`pip install requests`)
- BeautifulSoup library (`pip install beautifulsoup4`)

### Usage
1. Clone the repository to your local machine:

       git clone https://github.com/your_username/web-file-downloader.git

2. Navigate to the directory containing the Python script:

       cd Mass-Web-Files-Downloader-Based-on-file-Extension

3. Run the Python script using the following command:

       python download_files.py

4. Follow the prompts to input the website link, file extension, and output directory.

## Example Use Case

Suppose you want to download all PDF files from a website containing research papers. Here's how you can use the Web File Downloader script:

1. Enter the website link: `https://example.com/research-papers`
2. Enter the file extension: `.pdf`
3. Choose the output directory where the downloaded files will be saved.

The script will fetch the webpage content, filter the links to PDF files, and save them in a folder named `example.com` (or the domain name of the website) within the specified output directory. You can then access and view the downloaded PDF files conveniently.

also raise a PR in case you improve or smth
