import asyncio

async def print_after_delay(name, delay):
    await asyncio.sleep(delay)
    print(f"Hello from {name}!")

async def main():
    task1 = asyncio.create_task(print_after_delay("Task 1", 1))
    task2 = asyncio.create_task(print_after_delay("Task 2", 2))
    task3 = asyncio.create_task(print_after_delay("Task 3", 3))
    await asyncio.gather(task1, task2, task3)

asyncio.run(main())
