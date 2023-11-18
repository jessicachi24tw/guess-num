import random
r = random.randint(1, 100)
count = 0
while True:
	count += 1 #count = count + 1
	x = input('請猜1-100任一整數：')
	x = int(x)
	if x == r:
		print('你猜對了')
		print('這是你猜的第', count, '次')
		break
	elif x > r:
		print('你猜錯了 你猜得比較大')
	else:
		print('你猜錯了 你猜得比較小')
	print('這是你猜的第', count, '次')