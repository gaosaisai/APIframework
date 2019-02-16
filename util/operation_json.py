#coding:utf-8
import json
# fp=open("../dataconfig/login.json")
# data=json.load(fp)
# print (data['addcart'])
 
class OperationJson:
	def __init__(self):
		self.data=self.read_data()
	# 读取json文件  用完了会自动关闭	
	def read_data(self):
		# fp = open('../dataconfig/login.json')
		# fp.close()
		with open('../dataconfig/login.json') as fp:
			data=json.load(fp)
			return data

	# 根据关键字获取数据
	def get_data(self,id):
		return self.data[id]

if __name__ == '__main__':
	opjson=OperationJson()
	print (opjson.get_data('login'))
