import asyncio

async def my_async_function():
    # Do something that takes a long time
    await asyncio.sleep(10)
    return "Hello, world!"

async def main():
    try:
        result = await asyncio.wait_for(my_async_function(), timeout=5)
        print(result)
    except asyncio.TimeoutError:
        print("The operation timed out.")

asyncio.run(main())
