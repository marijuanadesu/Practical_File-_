#PRACTICAL 5
'''Read a text file line by line and
display each word separated by "a#".'''

f= open("story.txt","r")
data= f.readline().split()
for i in data:
    print(i,end="a# ")
