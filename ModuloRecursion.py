def factorial(n):
    if n/10<=1:
        return n
    else:
        return n%10+factorial(int(n/10))
      
print(factorial(351))
