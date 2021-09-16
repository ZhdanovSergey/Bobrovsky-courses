from auto_check_tail import Stack

def calc_postfix_exp(string):
	arr = string.split()
	stack1, stack2 = Stack(), Stack()
	for x in arr[::-1]:
		stack1.push(x)
	while stack1.size() > 0:
		if stack1.peek().isdigit():
			stack2.push(int(stack1.pop()))
			if stack2.size() > 2:
				raise ValueError('input has more than 2 digits in a row')
			continue
		elif stack1.peek() == '+':
			stack1.pop()
			if stack2.size() != 2:
				raise ValueError('stack2 must contain 2 elements before operation')
			stack2.push(stack2.pop() + stack2.pop())
			continue
		elif stack1.peek() == '*':
			stack1.pop()
			if stack2.size() != 2:
				raise ValueError('stack2 must contain 2 elements before operation')
			stack2.push(stack2.pop() * stack2.pop())
			continue
		elif stack1.peek() == '=':
			return stack2.pop()