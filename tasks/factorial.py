def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
print fact(5)



def fact(n):
    if n == 0:
       print("The factorial of 0 is 1")
    else:
       for i in range(1,n+1):
           f= f*i
print fact(7)






#tailrecursion
def tail_factorial(n, accumulator=1):
  if n == 0:
      print accumulator
  else:
      return tail_factorial(n-1, accumulator * n)
tail_factorial(5)
