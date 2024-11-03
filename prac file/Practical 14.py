def countword():
    obj=open("story.txt","r")
    data=obj.read()
    word=data.split()
    c=0
    for i in data:
        if i =='A':
           c+=1
    print(c)
countword()
