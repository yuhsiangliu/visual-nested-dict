import json

class VisualNestedDict:
	def __init__(self, d=None, name=None):
		self.name = name
		self.root = Node(name)
		if d:
			self.root.input(d)
		self.arrow = ['├── ', '└── ']
		self.v_line = ['│   ', '    ']
		self.h_line = '─'
		self.space = []
		self.result = []

	def load(self, d, name=None):
		self.root = Node(name or self.name)
		self.root.input(d)

	def read_json(self, file, name=None):
		with open(file) as f:
			d = json.load(f)
		self.load(d, name=name)

	def load_json(self, code, name=None):
		d = json.loads(code)
		self.load(d, name=name)

	def text(self, node=None, end=False):
		node = node or self.root
		pre = ''.join(self.space)
		if self.space:
			pre += self.arrow[end]
			self.space.append(self.v_line[end])
		else:
			self.space.append('')
		if type(node).__name__!='Node':
			raise TypeError()
		if node.dtype=='dict':
			self.result.append(f'{pre}{node.key} <{node.dtype}>')
			for i, child in enumerate(node.sub,1):
				self.text(node=child, end=i==len(node.sub))
		elif node.dtype=='list':
			left, child, right = self.expand_list(node)
			left = ''.join(left)
			right = ''.join(right[::-1])
			self.space.append(' '*(len(left)+len(node.key)+1))
			if child==None:
				self.result.append(f'{pre}{node.key} {left}{right}')
			elif child.dtype!='dict':
				self.result.append(f'{pre}{node.key} {left}{child.dtype}{right}')
			else:
				self.result.append(f'{pre}{node.key} {left}{child.dtype}{right}')
				for i, gr in enumerate(child.sub,1):
					self.text(node=gr, end=i==len(child.sub))
			self.space.pop()
		else:
			self.result.append(f'{pre}{node.key} <{node.dtype}>')
		self.space.pop()

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

class Node:
	def __init__(self, key='', dtype=None, sub=None):
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

if __name__ == '__main__':
	course = { 'id': 'MATH 101',
	           'name': 'Differential Calculus',
	           'section': 100,
	           'term': 'Spring 2021',
	           'instructor': 'John Doe',
	           'schedule': [{'day': 'Monday', 'time': [840, 930], 'room': 'Remote'},
	                   {'day': 'Wednesday', 'time': [510, 600], 'room': 'Remote'}],
	           'student': [{'name': 'Adam Lee',
	                        'major': 'mathematics',
	                        'grade': {'homework': [10, 9, 10, 10, 8],
	                                  'midterm': 9,
	                                  'final': 9}},
	                       {'first_name': 'Dana McKay',
	                        'major': 'business',
	                        'grade': {'homework': [8, 9, 10, 7, 8],
	                                  'midterm': 8,
	                                  'final': 10}}]
	           }

	VND = VisualNestedDict(name='course')
	VND.load(course)
	VND.text()