import requests
from bs4 import BeautifulSoup
from pprint import pprint
import time
import concurrent.futures


def download_and_write(url):
    response = requests.get(url)
    log_file_name = url.split("/")[-1]
    with open(log_file_name,'w') as f:
        f.write(response.text)
        

def main():
    start = time.perf_counter()
    url = "http://localhost:8000"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    urls = [f"{url}/{a['href']}" for a in soup.find_all('a')]

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(download_and_write,urls)

    end = time.perf_counter()
    print(end-start,"s")





if __name__ == '__main__':
    main()
