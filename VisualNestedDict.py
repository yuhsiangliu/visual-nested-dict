class Node:
	def __init__(self, key=None, dtype=None, sub=None):
		self.key = key
		self.dtype = dtype
		self.sub = sub or []

	def input(self, data):
		self.dtype = type(data).__name__
		if self.dtype=='dict':
			for key in data:
				self.sub.append(Node(key=key))
				self.sub[-1].input(data[key])
		elif self.dtype=='list':
			if data:
				self.sub.append(Node())
				self.sub[-1].input(data[0])

class VisualNestedDict:
	def __init__(self, name=None, d=[]):
		self.name = name
		self.root = Node(name)
		if d:
			self.root.input(d)
		self.draw = ['├─']

	def write(self, d):
		self.root = Node(self.name)
		self.root.input(d)

	def read_json(self, path):
		pass

	def text(self, pre=0, start=-1, node=None):
		node = node or self.root
		if type(node).__name__!='Node':
			raise TypeError()
		if node.dtype=='dict':
			print(f'{"-"*pre}{node.key} <{node.dtype}>')
			for child in node.sub:
				if type(child).__name__=='Node':
					self.text(pre=pre+1, node=child)
		elif node.dtype=='list':
			left, child, right = self.expand_list(node)
			left = ''.join(left)
			right = ''.join(right[::-1])
			if child==None:
				print(f'{"-"*pre}{node.key} {left}{right}')
			elif child.dtype!='dict':
				print(f'{"-"*pre}{node.key} {left}{child.dtype}{right}')
			else:
				print(f'{"-"*pre}{node.key} {left}{child.dtype}{right}')
				for gr in child.sub:
					if type(gr).__name__=='Node':
						self.text(pre=pre+len(node.key)+len(left)+1, node=gr)
		else:
			print(f'{"-"*pre}{node.key} <{node.dtype}>')

	def expand_list(self, node):
		if type(node).__name__!='Node' or node.dtype!='list':
			raise TypeError()
		left, right = ['<'], ['>']
		while node.dtype=='list':
			left.append('list[')
			right.append(']')
			if not node.sub:
				node = None
				break
			node = node.sub[0]
		return left, node, right






#d = {'1':'2'}
d = {'1': ['2','3'], '4':{'5':'6', '7':'8'}, '9': '10', '11':[['12','13']], '14':[{'15': ['16','17'], '18': ('19','20')}]}
x = VisualNestedDict('HELLO', d)
x.text()

#for a in ['┢', '├', '┝', '├', '─', '└', '│', ' │', '││', '─│']:
#	print(a)