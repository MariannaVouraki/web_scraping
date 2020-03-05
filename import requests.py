import requests
from bs4 import beautifulSoup
import re

file_name = './queue.txt'
def run(url):
        sourse_code = request.get(url)
        soup = Beautifulsoup(page.content,'html.parser')
        linkregex = re.compile(r"\L<symbols>", symbols = ['#','-','_','?','='])
        if linkregex.search(url):
            pass
        for link in links:
            try:
                if 'wikipedia.org' in link['href']:
                    add_to_file(file_name,f"https://www.wikipedia.org{link['href']}")
            except:
                pass

 def getlink(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.readline()
    return data       
def add_to_file(path, data):
    with open(path,'a', encoding='utf-8') as file:
        file.write(data + '\n')

if __name__ == "__main__":
    run(getlink(file_name))       