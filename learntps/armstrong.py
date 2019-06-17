#armstrong number

n = input("enter a number")
tot = 0
temp=n
while temp>0:
    digit = temp%10
    tot = tot+(digit**3)
    temp = temp//10
if tot == n:
    print "armstrong no"
else:
    print "not an armstrong no"
