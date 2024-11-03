#PRACTICAL 1
def countdata():
    f=open("story.txt","r")
    ca=cd=cad=0
    data=f.read()
    for i in data:
        if i.isalpha():
           ca+=1
        elif i.isdigit():
            cd+=1
        elif i.isalnum():
            cad+=1

    print("No. of alphabets are",ca )
    print("No. of digits are",cd )
    print("No. of alphanumeric characters are",cad )
countdata()


