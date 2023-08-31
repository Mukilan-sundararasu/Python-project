#my first python project

A = float(input('enter the first number: '))
B = float(input('enter the second number: '))

operator = input('enter an operator (+ - * / ): ')

if operator == '+':
	result = A+B
	print(result)
	
elif operator == '-':
	result = A-B
	print(result)
	
elif operator == '*':
	result = A*B
	print(result)
	
elif operator == '/':
	result = A/B
	print(result)
	
else:
	print(f'{operator} is not a valid operator')