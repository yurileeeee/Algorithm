# BOJ 10872 팩토리얼

n = int(input())

def factorial(num):
  if num == 0 or num == 1:
    return 1
  else: 
    return num*factorial(num-1)

print(factorial(n))