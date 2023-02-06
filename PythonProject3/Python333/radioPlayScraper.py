# 2021-03-03 ebb: I adapted a script for downloading videos from GeeksforGeeks.org: https://www.geeksforgeeks.org/downloading-files-web-using-python/
# Before beginning, you will need to do some pip installs at the command line:
# go out to your shell (Git Bash or Terminal) and enter:
# pip install BeautifulSoup4

import requests
import os
from bs4 import BeautifulSoup

url = 'http://textfiles.com/food/'
folder = 'recipes'

if not os.path.exists(folder):
    os.makedirs(folder)

def scrape_paragraphs(url):
    response = requests.get(url, stream=True)
    soup = BeautifulSoup(response.text, 'html.parser')

    subfolder = url.split("//")[1].replace("/", "_").replace(".", "_")
    subfolder_path = os.path.join(folder, subfolder)

    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)

    for i, p in enumerate(soup.find_all('p')):
        with open(os.path.join(subfolder_path, f'paragraph_{i}.txt'), 'w') as f:
            f.write(p.text)

scrape_paragraphs(url)

for link in BeautifulSoup(requests.get(url).text, 'html.parser').find_all('a'):
    link_url = link.get('href')
    if link_url.startswith('http'):
        scrape_paragraphs(link_url)
        scrape_paragraphs(link_url)








