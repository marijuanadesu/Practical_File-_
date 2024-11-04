#PRACTICAL 3
#Define a function to add even and odd 
#elements of list separately and print the sum.
def add():
    sume=sumo=0
    list=[0,1,2,3,4,5,6,7,8,9]
    for i in list:
        if list[i]%2==0:
           sume+=list[i]
        else:
            sumo+=list[i]
    print("Sum of even elements:",sume )
    print("Sum of odd elements:",sumo )
add()
