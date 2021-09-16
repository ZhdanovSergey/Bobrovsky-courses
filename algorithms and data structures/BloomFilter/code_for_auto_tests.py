class BloomFilter:

	def __init__(self, f_len):
		self.filter_len = f_len
		self.store = 0

	def calc_hash(self, string, number):
		hash_ = 0
		for letter in string:
			code = ord(letter)
			hash_ = (hash_ * number + code) % self.filter_len
		return 1 << hash_

	def hash1(self, str1):
		return self.calc_hash(str1, 17)

	def hash2(self, str1):
		return self.calc_hash(str1, 223)

	def add(self, str1):
		self.store = self.store | self.hash1(str1)
		self.store = self.store | self.hash2(str1)

	def is_value(self, str1):
		return self.store & self.hash1(str1) != 0 \
			and self.store & self.hash2(str1) != 0