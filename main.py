'''
05/03/2021

Review

Recursion

def Function(parameter):
  if(): # Base Condition
    return something
  else:
    return something + Function(Parameter +/-/* 1)
'''

# 2. Fibonacci Sequence with Recursive function

def fibonacci(n):
  if(n <= 1):
    return n
  else: 
    return (fibonacci(n - 1) + fibonacci(n - 2))

nterm = int(input("How many terms do you want?: ")) 

if(nterm <= 0):
  print("Please enter a positive integer.")
else:
  print("Fibonacci Sequence: ")
  for i in range(nterm):
    print(fibonacci(i))

# 3. Fibonacci Sequence with a Loop

terms = int(input("How many Terms do you want?: "))
num1 = 0
num2 = 1
count = 0

if(nterm <= 0):
  print("Please enter a positive integer.")
else:
  print("Fibonacci Sequence: ")

  while(count < nterm):
    print(num1)
    nth = num1 + num2

    num1 = num2
    num2 = nth
    count += 1
