import requests
from bs4 import BeautifulSoup
from pprint import pprint
import time
import threading

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
    threads = []
    for a in soup.find_all('a'):
        url_file = f"{url}/{a['href']}"
        print(url_file)
        th = threading.Thread(target=download_and_write,args=[url_file])
        
        th.start()
        threads.append(th)

    for th in threads:
        th.join()
    end = time.perf_counter()
    print(end-start,"s")





if __name__ == '__main__':
    main()
