'''
Real-World Example: Multithreading for I/O-bound Tasks
Scenario: Web Scraping 
Web scraping often involves making numerous 
network requests to fetch web pages. 
These tasks are I/O-bound because they spend a lot of time waiting 
for responses from servers. Multithreading can significantly improve
the performance by allowing multiple web pages to be fetched concurrently.
'''

'''
https://www.langchain.com/
https://docs.langchain.com/oss/python/langchain/overview?_gl=1*mp1jnt*_ga*MTAwNTEyNjA3My4xNzYxNzY3NzEz*_ga_47WX3HKKY2*czE3NjE3Njc3MTMkbzEkZzAkdDE3NjE3Njc3MTMkajYwJGwwJGgw
https://docs.langchain.com/oss/python/langchain/tools
https://docs.langchain.com/oss/python/langchain/agents
'''

import threading
import requests
from bs4 import BeautifulSoup
import re

urls=[
    'https://www.langchain.com/',
    'https://docs.langchain.com/oss/python/langchain/overview?_gl=1*mp1jnt*_ga*MTAwNTEyNjA3My4xNzYxNzY3NzEz*_ga_47WX3HKKY2*czE3NjE3Njc3MTMkbzEkZzAkdDE3NjE3Njc3MTMkajYwJGwwJGgw;',
    'https://docs.langchain.com/oss/python/langchain/tools',
    'https://docs.langchain.com/oss/python/langchain/agents'
]


def sanitize_filename(url):
    # Replace all characters that are NOT letters, numbers, _, or - with _
    return re.sub(r'[^a-zA-Z0-9_-]', '_', url)

def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f'Fetched {len(soup.get_text())} characters from {url}')

    filename = f"file_{sanitize_filename(url)}.txt"
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(url + "\n\n\n")
        file.write(soup.get_text())

threads = []

for url in urls:
    thread = threading.Thread(target=fetch_content,args = (url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("all the urls are fetched")
