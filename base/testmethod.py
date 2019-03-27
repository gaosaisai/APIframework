import unittest
from demo import RunMain
import json
import HTMLTestRunner
from mock import mock
from mock_demo import mock_test

class TestMethod(unittest.TestCase):

	def setUp(self):
		self.run=RunMain()
		

	def test_03(self):
		url = 'http://coding.imooc.com/api/cate'
		data = {
			'timestamp':'1507034803124',
			'uid':'5249191',
			'uuid':'5ae7d1a22c82fb89c78f603420870ad7',
			'secrect':'078474b41dd37ddd5efeb04aa591ec12',
			'token':'7d6f14f21ec96d755de41e6c076758dd',
			'cid':'0',
			'errorCode':1001
			}
		# run=RunMain()   # 调用的demo中的类，赋值为 run
		res= mock_test(self.run.run_main,data,url,'POST',data)
		# mock_data = mock.Mock(return_value=data)  #把data作为一个mock的返回值
		# print (mock_data)
		# self.run.run_main=mock_data
		res =self.run.run_main(url,'POST',data)   # 调用demo 中的run_main()方法
		print (res)
	# @unittest.skip('test_02')
	def test_02(self):
		url = 'http://coding.imooc.com/api/cate'
		data = {
			'timestamp':'1507034803124',
			'uid':'5249191',
			'uuid':'5ae7d1a22c82fb89c78f603420870ad7',
			'secrect':'078474b41dd37ddd5efeb04aa591ec12',
			'token':'7d6f14f21ec96d755de41e6c076758dd',
			'cid':'0',
			'errorCode':1001		}
		res=self.run.run_main(url,'POST',data)
		# print (res)  #不能使用loads，因为在demo中已经进行loads了
		res=eval(res)
		self.assertNotEqual(res['errorCode'],1001,'测试失败')
		print ("这是第二个case")

if __name__ == '__main__':
	# filepath="../report/htmlreport.html"
	# fp=open(filepath,'wb')
	unittest.main()
	# suite= unittest.TestSuite()
	# suite.addTest(TestMethod('test_02'))
	# suite.addTest(TestMethod('test_03'))
	# runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='this is first report')
	# runner.run(suite)

	# unittest.TextTestRunner().run(suite)
