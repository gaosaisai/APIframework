#coding:utf-8
import sys
sys.path.append("E:/saisaigithubfiles/APIframework")
sys.path.append("E:/saisaigithubfiles/APIframework/data")
from base.runmethod import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
from util.send_email import SendEmail
class RunTest:
	def __init__(self):
		self.run_method=RunMethod()
		self.data=GetData()
		self.com_util=CommonUtil()
		self.send_mai = SendEmail()

	#程序执行的主入口
	def go_on_run(self):
		res=None
		pass_count = []
		fail_count = []
		#10 0,1,2,3,4,5,6......  第一行不需要
		rows_count=self.data.get_case_lines()
		for i in range(1,rows_count):
			url =self.data.get_request_url(i)
			method=self.data.get_request_method(i)
			is_run=self.data.get_is_run(i)
			data=self.data.get_data_for_json(i)
			#不能调用get_request_data()方法
			expect=self.data.get_expect_data(i)
			header=self.data.is_header(i)
			depend_case = self.data.is_depend(i)
			# 有依赖后  需要把需要的数据组装起来  返回结果
			if depend_case != None:
				self.sepend_data = DependentData()
				#获取的依赖相应数据
				depend_response_data = self.depend_data.get_data_for_key(i)
				#获取依赖的key
				depend_key = self.data.get_depend_filed(i)
				request_data[depend_key] = depend_response_data
			res=self.run_method.run_main(method,url,data,header)

			if is_run:
			#method,url,data=None,header=None  run_main里边变量的顺序不能错
				res=self.run_method.run_main(method,url,data,header)
				# print (type(res))
				if self.com_util.is_contain(expect,res):
					# print ("测试通过")
					self.data.write_result(i,'pass')
					pass_count.append(i)
					print (pass_count)
					print (len(pass_count))
				else:
					# print ("测试失败")
					self.data.write_result(i,'fail')
					fail_count.append(i)
					# print (len(fail_count))
					print (fail_count)
			return res
			self.send_mai.send_main([1,2],[1])
		self.send_mai.send_main([1,2],[1])
if __name__ == '__main__':
	run = RunTest()
	# print (run.go_on_run())
	run.go_on_run()