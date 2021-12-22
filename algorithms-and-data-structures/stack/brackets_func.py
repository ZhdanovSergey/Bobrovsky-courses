from auto_check_tail import Stack

def check_brackets_balance(string):
	stack = Stack()
	for x in string:
		if x == '(':
			stack.push(1)
		elif x == ')' and stack.pop() is None:
			return False
	return stack.size() == 0