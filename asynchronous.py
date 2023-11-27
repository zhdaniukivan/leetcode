import asyncio
import time


async def func_1(x):
    print(x ** 2)
    await asyncio.sleep(3)
    print('func_1 finished')


async def func_2(x):
    print(x * 0.5)
    await asyncio.sleep(3)
    print('func_2 finished')


async def main():
    task1 = asyncio.create_task(func_1(4))
    task2 = asyncio.create_task(func_2(4))

    await task1
    await task2


print(time.strftime('%X'))
asyncio.run(main())
print(time.strftime('%X'))
