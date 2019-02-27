#coding:utf-8
# 处理数据依赖问题的文件
from util.operation_excel import OperationExcel
from base.runmethod import RunMethod
from data.get_data import GetData
from jsonpath_rw import jsonpath,parse
class DependdentData:
	def __init__(self,case_id):
		self.case_id = case_id
		self.opera_excel = OperationExcel()
		self.data = GetData()

	#通过case_id 去获取该case_id的整行数据
	def get_case_line_data(self):
		rows_data = self.opara_excel.get_rows_data(self.case_id)
		return rows_data

	#执行*依赖测试，获取结果
	def run_dependent(self):
		run_method = RunMethod()
		#找到对应的行号，后续获取其他数据需要用到
		row_num = self.opera_excel.get_row_num(self.case_id)
		request_data = self.get_data_for_json(row_num)
		header = self.data.is_header(row_num)
		method = self.data.get_request_method(row_num)
		url = self.data.get_request_url(row_num)
		# 获取这些数据以便后续run_main 方法使用
		res = run_method.run_main(method,url,request_data,header)
		return res


	# 根据依赖的key获取执行依赖case的响应数据，然后返回 ***
	def get_data_for_key(self,row):
		depend_data = self.data.get_depent_key(row)
		# 依赖的返回数据一般都是给出来，去运行case里边解析拿到对应的需要的数据
		response_data = self.run_dependent()
		json_exe = parse(depend_data)
		madle = json_exe.find(response_data)
		# for i in madle:
		# 	i.value
		return [math.value for math in madle][0]  # ???增强的for 循环 
