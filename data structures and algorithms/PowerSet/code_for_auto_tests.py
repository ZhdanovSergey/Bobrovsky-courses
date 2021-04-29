class PowerSet:

	def __init__(self):
		self.store = []

	def size(self):
		return len(self.store)

	def put(self, value):
		if not self.get(value):
			self.store.append(value)

	def get(self, value):
		return value in self.store

	def remove(self, value):
		if self.get(value):
			self.store.remove(value)
			return True
		else:
			return False

	def intersection(self, set2):
		new_set = PowerSet()
		for x in self.store:
			if set2.get(x):
				new_set.put(x)
		return new_set

	def union(self, set2):
		new_set = PowerSet()
		for x in self.store + set2.store:
			new_set.put(x)
		return new_set

	def difference(self, set2):
		new_set = PowerSet()
		for x in self.store:
			if not set2.get(x):
				new_set.put(x)
		return new_set

	def issubset(self, set2):
		for x in set2.store:
			if not self.get(x):
				return False
		return True
