#PRACTICAL 2
#Define a function to count words from the 
#text file poem.txt.
def red1():
    obj=open("poem.txt","r")
    data=obj.read()
    word=data.split()
    c=0
    for i in word:
        c+=1
    print(c)
red1()
