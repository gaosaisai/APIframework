#coding:utf-8
class global_var:  
	#case_id
	Id='0'
	url='1'
	run='2'
	request_way='3'
	header='4'
	case_depend='5'
	data_depend='6'
	filed_depend='7'
	data='8'
	expect='9'
	result='10'
#获取caseid  且为字符串类型，用int在后续转化为整数型
def get_id():
	return global_var.Id
	# 把变量放在类里，保证调用时不会调用重名的数据 

#获取url
def get_url():
	return global_var.url

def get_run():
	return global_var.run

def get_run_way():
	return global_var.request_way

def get_header():
	return global_var.header

def get_case_sepend():
	return global_var.case_depend

def get_data_depend():
	return global_var.data_depend

def get_filed_depend():
	return global_var.filed_depend

def get_data():
	return global_var.data

def get_expect():
	return global_var.expect

def get_result():
	return global_var.result

#获取header的值，暂时写死了。也可以去读配置文件
def get_header_value():
	header={
	"header":"1234",
	"cookie":"Mushishi"
	}