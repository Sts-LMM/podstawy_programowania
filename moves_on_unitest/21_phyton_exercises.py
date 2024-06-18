import asyncio

async def print_after_delay():
    await asyncio.sleep(2)
    print("Python Exercises!")

loop = asyncio.get_event_loop()
loop.run_until_complete(print_after_delay())
loop.close()
