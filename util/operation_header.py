# #coding:utf-8
# import requests
# url = "http://m.imooc.com/passport/user/login"
# data = {
# 	"username":"",
# 	"password":""
# }




# 统计字符串中每个字符出现的次数
aa="therjht sdhsjdh sdhsjdhjs 666fdfdf"
new_aa=[]

for i in aa:
	if i not in new_aa:
		new_aa.append(i)

dd={}
for i in new_aa:
	dd[i]=aa.count(i)
	# dd[i] =aa.count(i)
print (dd)


