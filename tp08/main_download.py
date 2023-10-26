import requests
from bs4 import BeautifulSoup
from pprint import pprint

def download_and_write(url):
    response = requests.get(url)
    log_file_name = url.split("/")[-1]
    with open(log_file_name,'w') as f:
        f.write(response.text)
        

def main():
    url = "http://localhost:8000"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for a in soup.find_all('a'):
        url_file = f"{url}/{a['href']}"
        print(url_file)
        download_and_write(url_file)







if __name__ == '__main__':
    main()
