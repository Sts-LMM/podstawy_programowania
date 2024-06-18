import asyncio

async def task(name):
    print(f"Starting task {name}")
    try:
        await asyncio.sleep(3)
    except asyncio.CancelledError:
        print(f"Task {name} cancelled")
    else:
        print(f"Task {name} finished")

async def main():
    task1 = asyncio.create_task(task("A"))
    task2 = asyncio.create_task(task("B"))

    await asyncio.sleep(1)
    task2.cancel()

    await task1

asyncio.run(main())
