import asyncio
import requests
import time
import httpx
from bs4 import BeautifulSoup



async def download(url_queue,data_queue):
    while True:
        url = await url_queue.get()
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            log_file_name = url.split("/")[-1]
            to_save = {
                "log_file_name":log_file_name,
                "data":response.text
            }
            data_queue.put_nowait(to_save)
        url_queue.task_done()


async def save(data_queue):
    while True:
        data_to_save = await data_queue.get()
        log_file_name = data_to_save['log_file_name']
        data = data_to_save['data']

        with open(log_file_name,'w') as f:
            f.write(data)
        data_queue.task_done()


async def main():
    start = time.perf_counter()
    url = "http://localhost:8000"
    url_q = asyncio.Queue()
    url_d = asyncio.Queue()
    nb_workers_dl = 5
    nb_workers_save= 3
    download_tasks = []
    save_tasks = []
    
    for i in range(nb_workers_dl):
        task = asyncio.create_task(download(url_q,url_d))
        download_tasks.append(task)

    for i in range(nb_workers_save):
        task = asyncio.create_task(save(url_d))
        save_tasks.append(task)
    
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    urls = [f"{url}/{a['href']}" for a in soup.find_all('a')]
    
    for url in urls:
        url_q.put_nowait(url)


    await url_q.join()
    await url_d.join()

    [t.cancel() for t in download_tasks]
    [t.cancel() for t in save_tasks]


    end = time.perf_counter()
    print(end-start,"s")




if __name__ == '__main__':
    asyncio.run(main())
