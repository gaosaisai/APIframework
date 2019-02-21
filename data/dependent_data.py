#coding:utf-8
# 处理数据依赖问题的文件
from util.operation_excel import OperationExcel
from base.runmethod import RunMethod
from data.get_data import GetData
class DependdentData:
	def __init__(self,case_id):
		self.case_id = case_id
		self.opera_excel = OperationExcel()
		self.data = GetData()
	#通过case_id 去获取该case_id的整行数据
	def get_case_line_data(self):
		rows_data = self.opara_excel.get_rows_data(self.case_id)
		return rows_data

	#执行依赖测试，获取结果
	def run_dependent(self):
		run_method = RunMethod()
		row_num = self.opera_excel.get_row_num(self.case_id)
		request_data = self.get_data_for_json(row_num)
		header = self.data.is_header(row_num)
		method = self.data.get_request_method(row_num)
		url = self.data.get_request_url(row_num)
		res = run_method.run_main(method,url,request_data,header)
		return res




