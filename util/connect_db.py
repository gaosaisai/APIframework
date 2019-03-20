# #coding:utf-8
import MySQLdb
import json
conn = MySQLdb.connect(
			host='localhost',
			port=336,
			user='root',
			passwd='123456',
			db='le_study',
			charset='utf8'
			)

cur = conn.cusor()
cur.execute("select * from web_user where Name='mushishi'")
print (cur.fetchone())

class OperationMysql:
	# 定义全局变量
	def __init__(self):
		self.conn = MySQLdb.connect(
			host='localhost',
			port=336,
			user='root',
			passwd='123456',
			db='le_study',
			charset='utf8',
			cursorclass=MySQLdb.cursors.DictCursor
			)
		self.cur = self.conn.cusor()

	#查询一条数据
	def search_one(self,sql):
		result = self.cur.excute(sql)
		result = json.dumps(result)
		return result

if __name__ == '__main__':
	op_mysql = OperationMysql()
	res = op_mysql.search_one("select * from web_user whers Name='mushishi")
	print (type(res))
