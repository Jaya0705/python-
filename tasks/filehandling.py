file = open('functions python.txt', 'r')  
for i in file: 
    print i 

    
    
    
file = open("functions python.txt", "r")  
print file.read(10)




with open('functions python.txt','w') as f: 
    f.write("This is the write command") 
    f.write("It allows us to write in a particular file")
with open('functions python.txt','a') as fi:
    fi.write("This will add this line")


with open('functions python.txt','r') as f1:
    #print f1.read()
    print f1.readlines()
    #print f1.readline()


fil= open('functions python.txt', 'r')  
for i in fil: 
    print i.strip 



#Python code to illustrate split() function 
with open("functions python.txt", "r") as file: 
    f = file.readlines()
    for line in f: 
        word = line.split(',') 
        print word

        
        
with open('functions python.txt','r') as f:
    f.flush()
    print f.read()
    print f.tell()
    print f.seek(5)
    print f.read()
    print f.tell()
    print f.fileno()
    print f.isatty()


#This,is,the,write,command,It,allows,us,to,write,in,a,particular,file,This,will,add,this,line
#next()
f = open('functions python.txt', 'r')  
for i in range(5):
   line = f.next()
   print "Line No %d - %s" %(i, line)
f.close()




#truncate()
'''truncate([size]): Truncate the file’s size. If the optional size argument is present, the file is truncated to (at most) that size. The size defaults to the current position. The current file position is not changed. Note that if a specified size exceeds the file’s current size, the result is platform-dependent: possibilities include that the file may remain unchanged, increase to the specified size as if zero-filled, or increase to the specified size with undefined new content.'''
f = open('functions python.txt', 'w') 
f.truncate(10) 
f.close() 




f = open('functions python.txt', 'a+') 
print(f.closed) 
print(f.encoding) 
print(f.mode) 
print(f.newlines) 
print(f.softspace) 


