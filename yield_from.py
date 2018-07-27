def first_generator():
    yield 1
    print('In the middle of first generator')
    yield 2


def second_generator():
    gen = first_generator()

    yield from gen
    print('In the middle of second generator')
    yield 3
