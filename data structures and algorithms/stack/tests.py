import unittest
from auto_check_tail import Stack
from brackets_func import check_brackets_balance
from postfix import calc_postfix_exp

class StackTest(unittest.TestCase):

	def test_len(self):
		stack = Stack()
		stack.stack = [1,2,3]
		self.assertEqual(stack.size(), 3)

	def test_push(self):
		stack = Stack()
		stack.stack = [1,2,3]
		stack.push(4)
		self.assertEqual(stack.stack, [1,2,3,4])

	def test_pop(self):
		stack = Stack()
		stack.stack = [1,2,3]
		self.assertEqual(stack.pop(), 3)
		self.assertEqual(stack.stack, [1,2])

	def test_pop_empty(self):
		stack = Stack()
		self.assertEqual(stack.pop(), None)
		self.assertEqual(stack.stack, [])

	def test_peek(self):
		stack = Stack()
		stack.stack = [1,2,3]
		self.assertEqual(stack.peek(), 3)
		self.assertEqual(stack.stack, [1,2,3])

	def test_peek_empty(self):
		stack = Stack()
		self.assertEqual(stack.peek(), None)
		self.assertEqual(stack.stack, [])

	def test_bracket_balance(self):
		self.assertTrue(check_brackets_balance('(()()())'))
		self.assertFalse(check_brackets_balance('(()()(()'))
		self.assertFalse(check_brackets_balance('())('))
		self.assertFalse(check_brackets_balance('))(('))

	def test_postfix_regression(self):
		self.assertEqual(calc_postfix_exp('8 2 + 5 * 9 + ='), 59)

	def test_postfix_incorrect_inputs(self):
		with self.assertRaises(ValueError):
			self.assertEqual(calc_postfix_exp('8 2 2 + 5 * 9 + ='), 59)
		with self.assertRaises(ValueError):
			self.assertEqual(calc_postfix_exp('8 + 5 * 9 + ='), 59)
		with self.assertRaises(ValueError):
			self.assertEqual(calc_postfix_exp('8 2 + * 9 + ='), 59)

if __name__ == '__main__':
	unittest.main()