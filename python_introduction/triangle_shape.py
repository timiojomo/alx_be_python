rows = 5

while rows > 0:
    columns = 10
    i = columns//2
    j = 1
    while j < columns:
        print(" "*i, "*"*j, end=" ")  
        print()
        j+=2
        i-=1
    break