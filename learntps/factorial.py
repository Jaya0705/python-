def factr(n):
    if n>=1:
        return n*factr(n-1)
    else:
        return 1


   
def facti(n):
    f=1
    if n>=1:
        for i in range(1,n+1):
            f=f*i
        return f
    else:
        return 1
    
print facti(7)
print factr(8)




#tailrecursion
def tail_factorial(n, accumulator=1):
  if n == 0:
      print accumulator
  else:
      return tail_factorial(n-1, accumulator * n)
tail_factorial(5)




