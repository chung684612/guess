import random

s = input('請輸入起始數字: ')
e = input('請輸入結束數字: ')
s = int(s)
e = int(e)
time = 0
r = random.randint(s, e)
while True:
	num = input('請猜數字: ')
	num = int(num)
	time += 1
	if num == r:
		print('恭喜您答對了!', '共猜了', time, '次')
		break
	elif num > r:
		print('答錯了', num, '比較大')
	elif num < r:
		print('答錯了', num, '比較小')