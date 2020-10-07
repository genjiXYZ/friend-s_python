#coding=utf-8
while True:
	try:
		x = input('输入您的时薪(单位:$ 格式:数字): ')
		type(float(x)) is float 
		break
	except ValueError:
		print ('格式错误,请输入 数字')

while True:
	try:
		y = input('输入您的工作时长(单位:h 格式:数字): ')
		type(float(y)) is float 
		break
	except ValueError:
		print ('格式错误,请输入 数字')

def isRight( num ):
	a = float(num)
	if a >=0 :
		return True
	else:
		return False	

if isRight( x ) & isRight( y ):
	c = ( float(x) * float(y))
	print('你的工资是:'+str(c)+'美金')
else:
	print('对不起你的数据有误,或者有旷工记录,请联系客服')		

