import asyncio

async def func1():
    while True:
           print ("hello")
           await asyncio.sleep(1)


async def func2():
    while True:
        print ("goodby")
        await asyncio.sleep(5)

async def main():
    task1=asyncio.create_task(func1())
    task2=asyncio.create_task(func2())
    await task1
    await task2


asyncio.run(main())