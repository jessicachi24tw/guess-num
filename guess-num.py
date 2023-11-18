import random
r = random.randint(1, 100)
while True:
	x = input('請猜1-100任一整數：')
	x = int(x)
	if x == r:
		print('你猜對了')
		break
	elif x > r:
		print('你猜錯了 你猜得比較大')
	else:
		print('你猜錯了 你猜得比較小')