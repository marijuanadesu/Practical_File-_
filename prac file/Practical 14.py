#PRACTICAL 14
'''Write a function to count'A' or'E 
individually from text file story. txt'''
def countword():
    obj=open("story.txt","r")
    data=obj.read()
    word=data.split()
    c=0
    for i in word:
        if i =='a':
           c+=1
    print(c)
countword()
