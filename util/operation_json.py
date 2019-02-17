#coding:utf-8
import json
# fp=open("../dataconfig/login.json")
# data=json.load(fp)
# print (data['addcart'])
 
class OperationJson:
	# 构造函数
	def __init__(self):
		self.data=self.read_data()
		#将两个方法关联起来
	# 读取json文件  用完了会自动关闭	
	def read_data(self):
		# fp = open('../dataconfig/login.json')
		# fp.close()
		# 你需要获取一个文件句柄，从文件中读取数据，然后关闭文件句柄。
		# 虽然这段代码运行良好，但是太冗长了。这时候就是with一展身手的时候了
		with open('../dataconfig/login.json') as fp:
			data=json.load(fp)
			return data
		# with open as 用完文件后会自动关闭
		# json load 方法

	# 根据关键字获取数据
	def get_data(self,id):
		return self.data[id]

if __name__ == '__main__':
	opjson=OperationJson()
	print (opjson.get_data('login'))
