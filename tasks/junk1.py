#readafilen print no of occurence of wordsinit
search_word=input('enter the word')
file=open('functions python.txt','r')
c=0
for line in file:
    words = line.split()
    print words
    for i in words:
        if i==search_word:
            c=c+1
print c
file.close()



#printing a pattern
for row in range(0,5):
    print '*'
    for col in range(0,row+1):
        print '*'

