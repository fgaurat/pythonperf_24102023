import asyncio
import requests
import time
import httpx
from bs4 import BeautifulSoup

sem = asyncio.Semaphore(10)


async def download_and_write_requests(url):
    loop = asyncio.get_event_loop()
    response =await loop.run_in_executor(None, requests.get, url)
    log_file_name = url.split("/")[-1]
    with open(log_file_name,'w') as f:
        f.write(response.text)
        
async def download_and_write(url):
    async with sem:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            log_file_name = url.split("/")[-1]
            with open(log_file_name,'w') as f:
                f.write(response.text)


async def main():
    start = time.perf_counter()
    url = "http://localhost:8000"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    urls = [download_and_write(f"{url}/{a['href']}") for a in soup.find_all('a')]
    result = await asyncio.gather(*urls)    

    end = time.perf_counter()
    print(end-start,"s")




if __name__ == '__main__':
    asyncio.run(main())
