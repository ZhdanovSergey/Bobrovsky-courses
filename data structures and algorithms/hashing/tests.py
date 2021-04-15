import unittest
from auto_check import HashTable
import random
import string


class HashTableTasts(unittest.TestCase):

    def test_hash_fun(self):
        table = HashTable(17, 3)
        test_val = 'abc'
        index = table.hash_fun(test_val)
        self.assertTrue(isinstance(index, int))
        self.assertTrue(0 <= index < 17)

    def test_hash_fun_random(self):
        for _ in range(1000):
            step = random.choice([2, 3, 5, 7, 11])
            size = random.choice([13, 17, 19, 23, 29, 31, 37, 41, 43, 47])
            table = HashTable(size, step)
            test_val = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(0,100)))
            index = table.hash_fun(test_val)
            self.assertTrue(isinstance(index, int))
            self.assertTrue(0 <= index < size)

    def test_seek_slot(self):
        table = HashTable(17, 3)
        test_val = 'abc'
        index = table.seek_slot(test_val)
        self.assertTrue(isinstance(index, int))
        self.assertTrue(0 <= index < 17)
        self.assertEqual(table.slots[index], None)

    def test_seek_slot_random(self):
        for _ in range(100):
            step = random.choice([2, 3, 5, 7, 11])
            size = random.choice([13, 17, 19, 23, 29, 31, 37, 41, 43, 47])
            table = HashTable(size, step)
            for i in range(table.size * 2):
                test_val = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(0,100)))
                index = table.seek_slot(test_val)
                if i < table.size:
                    self.assertTrue(isinstance(index, int))
                    self.assertTrue(0 <= index < size)
                    self.assertEqual(table.slots[index], None)
                    table.slots[index] = test_val
                else:
                    self.assertEqual(index, None)

    def test_put(self):
        table = HashTable(17, 3)
        test_val = 'abc'
        index = table.put(test_val)
        if index is not None:
            self.assertEqual(table.slots[index], test_val)

    def test_put_random(self):
        for _ in range(100):
            step = random.choice([2, 3, 5, 7, 11])
            size = random.choice([13, 17, 19, 23, 29, 31, 37, 41, 43, 47])
            table = HashTable(size, step)
            for i in range(table.size * 2):
                test_val = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(0,100)))
                index = table.put(test_val)
                if i < table.size:
                    self.assertTrue(isinstance(index, int))
                    self.assertTrue(0 <= index < size)
                    self.assertEqual(table.slots[index], test_val)
                else:
                    self.assertEqual(index, None)

    def test_find(self):
        table = HashTable(17, 3)
        test_val = 'abc'
        index = table.put(test_val)
        self.assertEqual(table.find(test_val), index)

    def test_find_random(self):
        for _ in range(100):
            step = random.choice([2, 3, 5, 7, 11])
            size = random.choice([13, 17, 19, 23, 29, 31, 37, 41, 43, 47])
            table = HashTable(size, step)
            for i in range(table.size * 2):
                test_val = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(0,100)))
                table.put(test_val)
                if test_val in table.slots:
                    self.assertEqual(table.slots[table.find(test_val)], test_val)
                else:
                    self.assertEqual(table.find(test_val), None)


if __name__ == '__main__':
    unittest.main()