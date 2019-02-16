#coding:utf-8
import sys
sys.path.append("C:/Users/saga270448/Pycharmwww/imooc")
from base.runmethod import RunMethod
from data.get_data import GetData
class RunTest:
	def __init__(self):
		self.run_method=RunMethod()
		self.data=GetData()

	#程序执行的主入口
	def go_on_run(self):
		res=None
		#10 0,1,2,3,4,5,6......  第一行不需要
		rows_count=self.data.get_case_lines()
		for i in range(1,rows_count):
			url =self.data.get_request_url(i)
			method=self.data.get_request_method(i)
			is_run=self.data.get_is_run(i)
			data=self.data.get_data_for_json(i)
			header=self.data.is_header(i)
			if is_run:
				#method,url,data=None,header=None
				res=self.run_method.run_main(method,url,data,header)
			return res
if __name__ == '__main__':
	run = RunTest()
	print (run.go_on_run())


