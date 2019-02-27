#coding:utf-8
import sys
sys.path.append("E:/saisaigithubfiles/APIframework")
#没加上边两居话之前一直报错，说没有这个模块
from util.operation_excel import OperationExcel
import data_config
from util.operation_json import OperationJson
class GetData:
	# 构造函数把 OperationExcel 拿进来
	def __init__(self):
		self.opera_excel=OperationExcel()   
		#添加以后才能操作OperationExcel里边的数据，
		#因为后边的数据基本都需要从这里边调用，所以先进行初始化。

	# 去获取Excel行数，就是我们的case个数  跟Excel里边的方法没有任何区别，
	# 但是老师还封装了一遍  555~~~
	def get_case_lines(self):
		return self.opera_excel.get_lines()

	#获取是否执行  返回True 和 False
	def get_is_run(self,row):
		flag = None
		col=int(data_config.get_run())
		run_model=self.opera_excel.get_cell_value(row,col)
		if run_model=='yes':
			flag=True
		else:
			flag=False
		return flag

	#是否携带header
	def is_header(self,row):
		col=int(data_config.get_header()) #转换字符串为整数型
		header=self.opera_excel.get_cell_value(row,col)
		if header=='yes':
			return data_config.get_header_value()  #读取真实的header
		else:
			return None

	#获取请求方式
	def get_request_method(self,row):
		col=int(data_config.get_run_way())
		request_method =self.opera_excel.get_cell_value(row,col)
		return request_method

	#获取URL
	def get_request_url(self,row):
		col=int(data_config.get_url())
		url=self.opera_excel.get_cell_value(row,col)
		return url

	#获取请求数据
	def get_request_data(self,row):
		col=int(data_config.get_data())
		data=self.opera_excel.get_cell_value(row,col)
		if data=='':
			return None
		return data

	#通过获取关键字拿到data数据,需要跟上边的data结合起来
	#调用上边返回的data  后续调用这个方法即可，
	#上边的方法算是到json文件的一个过渡
	def get_data_for_json(self,row):
		opera_json=OperationJson()  #也可以在构造函数里边实例化
		request_data=opera_json.get_data(self.get_request_data(row))
		return request_data

	#获取预期结果
	def get_expect_data(self,row):
		col=int(data_config.get_expect())
		expect=self.opera_excel.get_cell_value(row,col)
		if expect == '':
			return None
		return expect

	# 写入数据  所有列相关的数据都在这里边，行相关的数据是不固定的，需要在主函数中确定
	def write_result(self,row,value):
		col = int(data_config.get_result())
		self.opera_excel.write_value(row,col,value)


	#获取依赖数据的key
	def get_depend_key(self,row):
		col = int(data.config.get_data_depend())
		depent_key = self.opera_excel.get_cell_value(row,col)
		if depent_key == "":
			return None
		else:
			return depent_key

