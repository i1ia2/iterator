#Задание 1
class FlatIterator:
    def __init__(self, n_l):
        self.my_list = n_l

    def __iter__(self):
        self.cursor = 0
        self.nest_cursor = -1
        self.full_list = []
        return self

    def __next__(self):
        self.nest_cursor += 1
        if len(self.my_list[self.cursor]) == self.nest_cursor:
            self.cursor += 1
            self.nest_cursor = 0
        if self.cursor == len(self.my_list):
            raise StopIteration
        self.full_list = self.my_list[self.cursor][self.nest_cursor]
        return self.full_list



def test():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test()
#Задание 2
import types


def flat_generator(list_of_lists):
    for spisok in list_of_lists:
        for spi in spisok:
            yield spi
            spisok_list.append(spi)

spisok_list = []

def test():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test()