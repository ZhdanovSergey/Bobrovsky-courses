from auto_check import Deque

def check_palindrome(string):
	deque = Deque()
	for x in string:
		deque.addFront(x)
	while deque.size() >= 2:
		if deque.removeFront() == deque.removeTail():
			continue
		else:
			return False
	return True