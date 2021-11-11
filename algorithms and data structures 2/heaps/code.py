class Heap:

	def __init__(self):
		self.HeapArray = [] # хранит неотрицательные числа-ключи

	def _siftingDownRecursively(self, current_index):
		max_child_index = self._getMaxChildIndex(current_index)
		if max_child_index is not None and self.HeapArray[current_index] < self.HeapArray[max_child_index]:
			self._swapKeys(current_index, max_child_index)
			self._siftingDownRecursively(max_child_index)

	def _siftingUpRecursively(self, current_index):
		if (current_index > 0):
			parent_index = ((current_index + current_index % 2) - 2) // 2

			if self.HeapArray[current_index] > self.HeapArray[parent_index]:
				self._swapKeys(current_index, parent_index)
				self._siftingUpRecursively(parent_index)

	def _swapKeys(self, index1, index2):
		(self.HeapArray[index1], self.HeapArray[index2]) = (self.HeapArray[index2], self.HeapArray[index1])

	def _getMaxChildIndex(self, parent_index):
		if parent_index * 2 + 2 >= len(self.HeapArray):
			return None

		left_child_index = parent_index * 2 + 1
		right_child_index = parent_index * 2 + 2
		left_child_key = self.HeapArray[left_child_index]
		right_child_key = self.HeapArray[right_child_index]

		if left_child_key is None and right_child_key is None:
			return None
		if left_child_key is None:
			return right_child_index
		if right_child_key is None:
			return left_child_index
		if left_child_key >= right_child_key:
			return left_child_index
		return right_child_index
		
	def MakeHeap(self, a, depth):
		# создаём массив кучи HeapArray из заданного
		# размер массива выбираем на основе глубины depth
		tree_size = 2 ** (depth + 1) - 1
		self.HeapArray = [None] * tree_size

		for key in a:
			self.Add(key)

	def GetMax(self):
		# вернуть значение корня и перестроить кучу
		if (self.HeapArray[0] is None):
			return -1 # если куча пуста

		max_key = self.HeapArray[0]
		self.HeapArray[0] = None
		# last_key_index = next((index for index, key in reversed(enumerate(self.HeapArray)) if key is not None), None)
		last_key_index = next((index for index, key in reversed(list(enumerate(self.HeapArray))) if key is not None), None)

		if (last_key_index is not None):
			self.HeapArray[0] = self.HeapArray[last_key_index]
			self.HeapArray[last_key_index] = None
			self._siftingDownRecursively(0)

		return max_key


	def Add(self, key):
		# добавляем новый элемент key в кучу и перестраиваем её
		target_index = next((index for index, key in enumerate(self.HeapArray) if key is None), None)

		if target_index is None:
			return False # если куча вся заполнена

		self.HeapArray[target_index] = key
		self._siftingUpRecursively(target_index)

		return True