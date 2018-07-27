def generator_send():
    print('Going to yield a value')
    received = yield 42
    print(f'Received {received}')
