class MyIterator:
    def __init__(self):
        self.counter = 1

    def __iter__(self):
        print('Iter called')
        return self

    def __next__(self):
        print('Next called')
        counter = self.counter

        if counter > 3:
            raise StopIteration

        self.counter += 1

        return counter
