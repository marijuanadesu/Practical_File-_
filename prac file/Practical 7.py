def remove_lines_with_a():
    f= open('input.txt', 'r') 
    lines = f.readlines()
    
    f= open('output.txt', 'w') 
    for line in lines:
        if 'a' not in line:
            f.write(line)
          

remove_lines_with_a()
