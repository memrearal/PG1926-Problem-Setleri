#
# FizzBuzz Problemi çözümü
# @memrearal
#
baslangic = 1
bitis = 100
for i in range(baslangic, bitis):
	if i%3 == 0 and i%5 == 0:
		print("FizzBuzz,")
	else:
		if i%3 == 0:
			print("Fizz,")
		elif i%5 == 0:
			print("Buzz,")
		else:
			print('{},'.format(i))
