#PRACTICAL 1
#Define a function to count number of alphabets, digits,
# alphanumeric characters from the text file story.txt
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


