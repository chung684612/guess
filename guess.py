import random

r = random.randint(1, 100)
while True:
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('恭喜您答對了!')
		break
	elif num > r:
		print('答錯了', num, '比較大')
	elif num < r:
		print('答錯了', num, '比較小')