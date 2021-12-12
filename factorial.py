def factorial(n):
  ret = 1
  for i in range(2,n+1):
    ret *= i
  return ret

def sum(n):
  s = str(n)
  ret = 0
  for x in s: 
    ret += int(x)
  return ret

a = factorial(10)
b = sum(a)
print(f"fac:{a}\nsum:{b}")

a = factorial(100)
b = sum(a)
print(f"fac:{a}\nsum:{b}")