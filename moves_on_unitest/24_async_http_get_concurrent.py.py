import asyncio
import aiohttp

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    url1 = "https://example.com"
    url2 = "https://example.org"
    task1 = asyncio.create_task(fetch(url1))
    task2 = asyncio.create_task(fetch(url2))
    responses = await asyncio.gather(task1, task2)
    for response in responses:
        print(response)

asyncio.run(main())
