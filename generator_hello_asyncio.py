import asyncio


@asyncio.coroutine
def hello_world_coroutine(delay):
    print('Hello')
    yield from asyncio.sleep(delay)
    print(f'World, with delay: {delay}')


loop = asyncio.get_event_loop()

loop.create_task(hello_world_coroutine(1))
loop.create_task(hello_world_coroutine(2))

loop.run_forever()
