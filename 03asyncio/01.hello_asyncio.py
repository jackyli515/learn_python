"""
"""

import asyncio

import time


async def work(i):
    await asyncio.sleep(2)
    print(f"{time.time()}运行协程任务{i}...")


# 协程对象阻塞运行
for i in range(3):
    asyncio.run(work(i))


# 并发运行方式一
print("-并发运行方式1")


async def test_task():
    # 协程任务并发运行
    task = [asyncio.create_task(work(i)) for i in range(3)]
    await asyncio.wait(task)


asyncio.run(test_task())


# 并发运行方式二
print("-并发运行方式2")


async def test_task2():
    # 协程任务并发运行
    task = [asyncio.create_task(work(i)) for i in range(3)]
    await asyncio.gather(*task)


asyncio.run(test_task2())
