import random

time = 0
r = random.randint(1, 100)
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