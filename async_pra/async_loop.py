import asyncio


async def work(x):
    for _ in range(3):
        print('Work {} is running ..'.format(x))
    return "Work {} is finished".format(x)


async def study(x):
    for _ in range(3):
        print('Study {} is running ..'.format(x))
    return "Study {} is finished".format(x)


def call_back(future):
    print("Callback: {}".format(future.result()))


if __name__ == '__main__':  
    coroutine = work(1)
    coroutine_study = study(1)

    loop = asyncio.get_event_loop()

    task = asyncio.ensure_future(coroutine)
    task1 = asyncio.ensure_future(coroutine_study)
    task.add_done_callback(call_back)
    task1.add_done_callback(call_back)

    loop.run_until_complete(task)  # 返回任务的结果
    loop.run_until_complete(task1)
