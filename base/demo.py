import requests
import json

class RunMain:
	# def __init__(self,url,method,data=None):
	# 	self.res=self.run_main(url,method,data)

	def send_get(self,url,data):
		res=requests.get(url=url,data=data).json()
		# return json.dumps(res,indent=2,sort_keys=True)
		return res

	def send_post(self,url,data):
		res=requests.post(url=url,data=data).json()
		# return json.dumps(res,indent=2,sort_keys=True)
		return res

	def run_main(self,url,method,data=None):
		res= None
		if method =='GET':
			res= self.send_get(url,data)
		else:
			res= self.send_post(url,data)
		return res

if __name__ =='__main__':
	url = 'http://v.juhe.cn/laohuangli/d?date=2014-09-09&key=2e42c2614ebe84c6f225ea00b7095242'
	# data={
	# 	'key':'2e42c2614ebe84c6f225ea00b7095242',
	# 	'date':'2014-09-09'
	# }
	run = RunMain(url,'GET')
	print (run.res)