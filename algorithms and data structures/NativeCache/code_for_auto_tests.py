class NativeCache:

	def __init__(self, sz):
		self.size = sz
		self.slots = [None] * self.size
		self.values = [None] * self.size
		self.hits = [0] * self.size
		self.step = 3

	def hash_fun(self, key):
		return sum([ord(x) for x in key]) % self.size

	def is_key(self, key):
		return key in self.slots

	def put(self, key, value):
		init_index = self.hash_fun(key)
		index = init_index
		while True:
			if self.slots[index] is None:
				self.slots[index] = key
				self.values[index] = value
				break
			elif self.slots[index] == key:
				self.values[index] = value
				break
			index = (index + self.step) % self.size
			if index == init_index:
				min_hits_index = self.hits.index(min(self.hits))
				self.slots[min_hits_index] = key
				self.values[min_hits_index] = value
				self.hits[min_hits_index] = 0
				break

	def get(self, key):
		if self.is_key(key):
			index = self.slots.index(key)
			self.hits[index] += 1
			return self.values[index]
		else:
			return None