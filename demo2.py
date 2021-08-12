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


def func_two():
    print("world!")


def sub_two():
    for i in range(1, 10):
        try:
            time.sleep(3)
            func_two()
        except KeyboardInterrupt:
            break


async def async_sub_two():
    await loop.run_in_executor(None, sub_two)


async def main():
    futures = [asyncio.create_task(func_one()), asyncio.create_task(async_sub_two())]
    await asyncio.gather(*futures)


loop = asyncio.get_event_loop()
result = loop.run_until_complete(main())
loop.close()

asyncio.run(main())
