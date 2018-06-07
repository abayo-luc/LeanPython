# objects = [2,5,6,7,8]
# for x in objects:
# 	print(x)

# numbers = range(5,155,5)
# for number in numbers:
# 	if number == 120:
# 		break
# 	print(number)

numbers = range(-50,51)
for number in numbers:
	if number % 3 == 0 and number % 5 == 0:
		print('BingBang')
	elif number % 5 == 0:
		print('Bang')
	elif number % 3 == 0:
		print('Bing')
	else :
		print(number)
else:
	print('I am done')