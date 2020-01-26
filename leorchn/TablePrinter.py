# 创建时间：2019-6-22 4:30
# 完成时间：2019-6-22 5:45
class TablePrint(object):
	head = {}
	data = {}
	def inputHead(self, *args): # 写入表格标题数据
		self.head = {}
		for s in args[0] if isinstance(args[0], list) else args: # 判断适配类型
			self.head[self.head.__len__()] = str(s)
		return self
	def input(self, *args): # 写入表格内容数据
		line = {}
		for s in args[0] if isinstance(args[0], list) else args: # 判断适配类型
			line[line.__len__()] = str(s)
		self.data[self.data.__len__()] = line # 插入新行
		return self
	def clear(self): # 清空表格内容
		self.data = {}
		return self
	def print(self): # 打印表格
		char_space = {} # 定义每列最大占位量
		for k in self.head: # 输入表格标题占位量
			char_space[char_space.__len__()] = getCharSpace(self.head[k])
		for row in self.data: # 输入表格内容占位量
			for col in self.data[row]:
				char_space[col] = max(char_space[col], getCharSpace(self.data[row][col]))
		# 以上计算空间 以下开始打印
		for k in self.head: # 打印标题。所调用的spaces函数内计算的是该单元格内容与最大占位量的差值。多+1个空格用来表示分隔符
			s = self.head[k] # 左对齐：s + spaces( x + 1 )
			print(s+spaces(char_space[k] - getCharSpace(self.head[k]) + 1), end='')
		print('')
		for row in self.data:
			for col in self.data[row]:
				s = self.data[row][col] # 右对齐：spaces( x ) + s + spaces( 1 )
				print(spaces(char_space[col] - getCharSpace(self.data[row][col]))+s+' ', end='')
			print('')
def getCharSpace(str): # 得到文本占位量。单个字符char值大于255的算两个占位，比如中文。否则算一个占位
	total = 0
	for chr in str: total += 2 if ord(chr) > 255 else 1
	return total
def spaces(count): # 得到指定数量的空格
	s = ''
	for i in range(count): s += ' '
	return s
