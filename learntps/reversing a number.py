n= 12345
rev=0

while n>0:
    temp=n%10
    rev=rev*10+temp
    n=n/10
print rev





s='aaajjjdkkdd'
li=list(s)
di={}
for i in li:
    di[i]= li.count(i)
print di
    




a='jbjbnnnjb'
s='jb'
c=0
print a.count('jb')
for i in range(len(a)):
    if s in a:
       c=c+1
print c
