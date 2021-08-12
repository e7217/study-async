import asyncio
import time


async def func_one():
    print("hello")


async def sub_one():
    # while 1:
    for i in range(1, 10):
        try:
            await asyncio.sleep(2)
            await func_one()
        except KeyboardInterrupt:
            break


async def func_two():
    print("world!")


async def sub_two():
    for i in range(1, 10):
        try:
            await asyncio.sleep(3)
            await func_two()
        except KeyboardInterrupt:
            break


async def main():
    # futures = [asyncio.ensure_future(sub_one()), asyncio.ensure_future(sub_two())]
    # await asyncio.gather(*futures)
    futures = [asyncio.create_task(sub_one()), asyncio.create_task(sub_two())]
    await asyncio.gather(*futures)


asyncio.run(main())
