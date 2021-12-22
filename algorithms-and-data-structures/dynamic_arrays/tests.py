import unittest
from random import choice, randint
from auto_checked import DynArray

class DynArrayTests(unittest.TestCase):

    def create_dyn_arr(self, arr):
        dyn_arr = DynArray()
        for x in arr:
            dyn_arr.append(x)
        return dyn_arr

    def get_correct_capacity_after_increase(self, capacity, current_len):
        if current_len > capacity:
            capacity *= 2
        return capacity

    def get_correct_capacity_after_reduce(self, capacity, current_len):
        min_capacity = 16
        if current_len < capacity/2 and capacity > min_capacity:
            capacity = int(capacity/1.5)
        return max(capacity, min_capacity)

    def test_insert_simple(self):
        dyn_arr = self.create_dyn_arr([1,2,3])
        dyn_arr.insert(1,5)
        self.assertEqual([x for x in dyn_arr], [1,5,2,3])
        self.assertEqual(dyn_arr.capacity, 16)

    def test_insert_first_elem(self):
        dyn_arr = self.create_dyn_arr([1,2,3])
        dyn_arr.insert(0,5)
        self.assertEqual([x for x in dyn_arr], [5,1,2,3])
        self.assertEqual(dyn_arr.capacity, 16)

    def test_insert_last_elem(self):
        dyn_arr = self.create_dyn_arr([1,2,3])
        dyn_arr.insert(2,5)
        self.assertEqual([x for x in dyn_arr], [1,2,5,3])
        self.assertEqual(dyn_arr.capacity, 16)

    def test_insert_in_empty_arr(self):
        dyn_arr = self.create_dyn_arr([])
        dyn_arr.insert(0,5)
        self.assertEqual([x for x in dyn_arr], [5])
        self.assertEqual(dyn_arr.capacity, 16)

    def test_insert_incorrect_position(self):
        dyn_arr = self.create_dyn_arr([1,2,3])
        with self.assertRaises(IndexError):
            dyn_arr.insert(5,5)

    def test_insert_with_increase_capacity(self):
        dyn_arr = self.create_dyn_arr([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
        dyn_arr.insert(1,5)
        self.assertEqual([x for x in dyn_arr], [1,5,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
        self.assertEqual(dyn_arr.capacity, 32)

    def test_insert_random(self):
        for i in range(20):
            arr = [randint(-10,+10) for j in range(randint(0,100))]
            arr_orig_len = len(arr)
            dyn_arr = self.create_dyn_arr(arr)
            test_val = 100
            while len(arr) < arr_orig_len*2:
                test_index = randint(0,len(arr)+1)
                if test_index <= len(arr):
                    capacity_before = dyn_arr.capacity
                    arr.insert(test_index, test_val)
                    dyn_arr.insert(test_index,test_val)
                    self.assertEqual([x for x in dyn_arr], arr)
                    self.assertEqual(dyn_arr.capacity, self.get_correct_capacity_after_increase(capacity_before, len(arr)))
                else:
                    with self.assertRaises(IndexError):
                        dyn_arr.insert(test_index,test_val)

    def test_delete_simple(self):
        dyn_arr = self.create_dyn_arr([1,2,3])
        dyn_arr.delete(1)
        self.assertEqual([x for x in dyn_arr], [1,3])
        self.assertEqual(dyn_arr.capacity, 16)

    def test_delete_first_elem(self):
        dyn_arr = self.create_dyn_arr([1,2,3])
        dyn_arr.delete(0)
        self.assertEqual([x for x in dyn_arr], [2,3])
        self.assertEqual(dyn_arr.capacity, 16)

    def test_delete_last_elem(self):
        dyn_arr = self.create_dyn_arr([1,2,3])
        dyn_arr.delete(2)
        self.assertEqual([x for x in dyn_arr], [1,2])
        self.assertEqual(dyn_arr.capacity, 16)

    def test_delete_from_empty_arr(self):
        dyn_arr = self.create_dyn_arr([])
        with self.assertRaises(IndexError):
            dyn_arr.delete(0)

    def test_delete_incorrect_position(self):
        dyn_arr = self.create_dyn_arr([1,2,3])
        with self.assertRaises(IndexError):
            dyn_arr.delete(5)

    def test_delete_with_increase_capacity(self):
        dyn_arr = self.create_dyn_arr([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])
        dyn_arr.delete(0)
        dyn_arr.delete(0)
        self.assertEqual([x for x in dyn_arr], [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])
        self.assertEqual(dyn_arr.capacity, int(32/1.5))

    def test_delete_random(self):
        for i in range(20):
            arr = [randint(-10,+10) for j in range(randint(0,100))]
            arr_orig_len = len(arr)
            dyn_arr = self.create_dyn_arr(arr)
            while len(arr) > arr_orig_len/2:
                test_index = randint(0,len(arr))
                if test_index < len(arr):
                    capacity_before = dyn_arr.capacity
                    arr.pop(test_index)
                    dyn_arr.delete(test_index)
                    self.assertEqual([x for x in dyn_arr], arr)
                    self.assertEqual(dyn_arr.capacity, self.get_correct_capacity_after_reduce(capacity_before, len(arr)))
                else:
                    with self.assertRaises(IndexError):
                        dyn_arr.delete(test_index)

if __name__ == '__main__':
    unittest.main()