#PRACTICAL 3
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