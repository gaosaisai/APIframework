#coding:utf-8
# 处理数据依赖问题的文件
from util.operation_excel import OperationExcel

class DependdentData:
	def __init__(self,case_id):
		self.case_id = case_id
		self.opera_excel = OperationExcel()
	#通过case_id 去获取该case_id的整行数据
	def get_case_line_data(self.case_id):
		rows_data = self.opara_excel.get_rows_data(self.case_id)
		return rows_data
