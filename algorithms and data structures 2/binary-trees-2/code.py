class aBST:

	def __init__(self, depth):
		# правильно рассчитайте размер массива для дерева глубины depth:
		tree_size = 2 ** (depth + 1) - 1
		self.Tree = [None] * tree_size # массив ключей
	
	def FindKeyIndex(self, key):
		# ищем в массиве индекс ключа
		def findKeyRecursive(key, current_index):
			if self.Tree[current_index] == None:
				return -current_index
			if self.Tree[current_index] == key:
				return current_index

			leftChildIndex = current_index * 2 + 1
			rightChildIndex = current_index * 2 + 2

			if key < self.Tree[current_index] and leftChildIndex < len(self.Tree):
				return findKeyRecursive(key, leftChildIndex)
			if key > self.Tree[current_index] and rightChildIndex < len(self.Tree):
				return findKeyRecursive(key, rightChildIndex)

			return None

		if len(self.Tree) > 0:
			return findKeyRecursive(key, 0)
		return None
	
	def AddKey(self, key):
		# добавляем ключ в массив
		findResult = self.FindKeyIndex(key)

		if findResult is None:
			return -1

		if findResult < 0 or (findResult == 0 and self.Tree[0] is None):
			self.Tree[abs(findResult)] = key
			
		return abs(findResult)
		# индекс добавленного/существующего ключа или -1 если не удалось