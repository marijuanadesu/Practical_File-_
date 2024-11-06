#PRACTICAL 11
'''Write a Python program to implement
a stack using list.'''
stack=[]
def push(stack, item): 
    stack.append(item)

def pop(stack):
    if len(stack)!=0:
         return stack.pop() 
    else: 
        return "Stack is empty"

def peek(stack):
    if len(stack)!=0:
        return stack[-1] 
    else: 
        return "Stack is empty"

def size(stack):
    return len(stack) 

def display(stack):
    return stack

push(stack, 1) 
push(stack, 2) 
push(stack, 3) 

print("Stack:", display(stack)) 
print("Popped item:", pop(stack)) 
print("Stack after pop:", display(stack)) 
print("Top item:", peek(stack)) 
# Display stack size 
print("Stack size:",size(stack))
