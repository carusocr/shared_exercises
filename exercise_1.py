import sys

def max(num1, num2):
  if num1 > num2:
    return num1
  else:
    return num2

num1 = sys.argv[1]
num2 = sys.argv[2]
print(max(num1, num2))
