#coding:utf-8
import xlrd
# data=xlrd.open_workbook('../dataconfig/case1.xls')
# tables=data.sheets()[0]
# print (tables.nrows)
# print (tables.cell_value(2,3))

class OperationExcel:
	# 构造函数
	def __init__(self,file_name=None,sheet_id=None):
		#打开指定路径的Excel文件
		if file_name:
			self.file_name=file_name
			self.sheet_id=sheet_id
		
		else:
			self.file_name='../dataconfig/case1.xls'
			self.sheet_id=0
		# 给定一个默认的file_name 和sheet_id的值，算是一种容错处理
		self.data=self.get_data()   
		#self.data=后边可以是一个具体的值/公式/函数
	#获取sheets的内容
	def get_data(self):
		data=xlrd.open_workbook(self.file_name)
		# 得到Excel文件对象
		tables=data.sheets()[self.sheet_id]
		#通过index：下标 获取指定索引的sheet
		# tables=data.sheet_name()[]
		#通过sheet的名字获取指定的sheet
		return tables

	#获取单元格的行数
	def get_lines(self):
		table=self.data
		# table=self.get_data()  也可以用这行代码
		return table.nrows
		# nrows 获取sheet表格行总数
		# ncols 获取sheet表格列总数
	#获取某一个单元格的内容
	def get_cell_value(self,row,col):
		return self.data.cell_value(row,col)
		# cell_value 通过行列坐标读取表格中的数据
if __name__ == '__main__':
	opers = OperationExcel()
	print (opers.get_cell_value(1,2))
	# 1,2 Excel读取行列的时候都是从0开始 
	# 1代表Excel表中的第二行 2代表Excel中的第三行

	# 不需要关闭文件对象，workfile文件对象没有close()方法