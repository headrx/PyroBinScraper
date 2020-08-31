
#!/user/bin/python3.8

#############
#Downloads all PDF files from PyroBin 
#Written by HeadRx
#Aug 31, 2020
#############

from bs4 import BeautifulSoup
import requests
import os
import subprocess

def build_pdfs(url):
    headers = {'User Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 '}
    data = requests.get(url, headers = headers)
    data = data.content

    links = list()
    soup = BeautifulSoup(data)

    #Get pages
    for link in soup.findAll('a', href= True):
        if 'pdf' in link['href']:
            links.append(link['href'])
    return links

def build_pages(url):
    headers = {'User Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 '}
    data = requests.get(url, headers = headers)
    data = data.content

    pages = list()
    soup = BeautifulSoup(data)

    #Get pages
    for link in soup.findAll('a', href= True):
        if 'php' in link['href']:
            pages.append(link['href'])
    return pages

def download(url):
    filename = url.split('/')
    filename = filename[2]
    subprocess.call(f"wget --max-redirect 0 ‐O {filename} {url}", shell=True)

#Main loop
base = "http://pyrobin.com"
url = "http://pyrobin.com/files.php"
pages = build_pages(url)

for page in pages:
    print(f'Retrieving : {page}')
    links = build_pdfs(base+page)
    links = set(links)
    for link in links:
        if 'index' not in link and 'pdf' in link:
            download(base+link)
