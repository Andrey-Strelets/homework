with open("number.txt") as file:

	for line in file:
		num1, num2, num3 = line.strip() and line.split()
		for num in range(1, int(num3) + 1):
			if num % int(num1) == 0:
				print("F",end='')
			if num % int(num2) == 0:
				print ("B", end='')
			if num % int(num1)  != 0 and num % int(num2) != 0:
				print(num, end='')
			print(" ", end='')
		print("\n", end='')
		print("Number in strind with file - ", num1, num2, num3, end='\n\n' )
