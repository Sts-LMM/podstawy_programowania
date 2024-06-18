import asyncio
import time

async def task(name):
    print(f"Starting task {name}")
    await asyncio.sleep(1)
    print(f"Task {name} finished")

async def main():
    start = time.time()
    await asyncio.gather(
        task("A"),
        task("B"),
        task("C"),
        task("D"),
        task("E"),
    )
    end = time.time()
    print(f"Tasks completed in {end - start:.2f} seconds")

asyncio.run(main())
