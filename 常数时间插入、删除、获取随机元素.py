import random
class RandomizedSet:

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		#该字典用来存val再列表中的下标
		self.d = {}
		#用来按插入顺序存入值
		self.l = []

	def insert(self, val: int) -> bool:
		"""
		Inserts a value to the set. Returns true if the set did not already contain the specified element.
		"""
		if val in self.d:
			return False
		else:
			#字典的键为val，值为下标
			self.d[val] = len(self.l)
			self.l.append(val)
			return True

	def remove(self, val: int) -> bool:
		"""
		Removes a value from the set. Returns true if the set contained the specified element.
		"""
		if val in self.d:
			#将字典最后插入的下标改为val的下标
			self.d[self.l[-1]] = self.d[val]
			#首先从字典中删除val这个键值对，其次将最后插入列表中的元素覆盖到val的下标下，
			self.l[self.d.pop(val)] = self.l[-1]
			#最后删除最后一个下标
			self.l.pop()
			return True
		else:
			return False

	def getRandom(self) -> int:
		"""
		Get a random element from the set.
		"""
		#随机返回一个值
		return self.l[random.randint(0, len(self.l) - 1)]
