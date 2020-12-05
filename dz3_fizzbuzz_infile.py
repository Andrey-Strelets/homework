with open("number.txt") as file, open("result.txt", "w") as r:

	for line in file:
		num1, num2, num3 = line.strip() and line.split()
		for num in range(1, int(num3) + 1):
			if num % int(num1) == 0:
				print("F", file=r, end='')
			if num % int(num2) == 0:
				print ("B", file=r, end='')
			if num % int(num1)  != 0 and num % int(num2) != 0:
				print(num, file=r, end='')
			print(" ", file=r, end='')
		print("\n", file=r, end='')
		print("Number in strind with file - ", num1, num2, num3, file=r, end='\n\n' )
