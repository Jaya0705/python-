li=['1','2','3','a','4','5','b','0','0']
l1=[]
l2=[]
for i in li:
    try:
        r=1/int(i)
        l1.append(i)
    except (ZeroDivisionError):
        l1.append(i)
    except (ValueError):
        l2.append(i)
   
print l1
print l2





try:
     file = open('functions python.txt', 'r')
     for i in file: 
         Print i 
         if i <= 0:
             raise ValueError("That is not a positive number!")
except ValueError as ve:
     print ve

except NameError as ne:
    print ne

except SyntaxError as se:
    print se
    
except Exception:
    print 'file not found error'








#exception handling
import sys
randomList = [0, 2]
for i in randomList:
    try:
        print("The entry is", i)
        r = 1/float(i)
        break
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()
print("The reciprocal of",i,"is",r)









#**kwargs 
def myFun(arg1, **kwargs):  
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 
myFun("Hi", first ='Geeks', mid ='for', last='Geeks') 
