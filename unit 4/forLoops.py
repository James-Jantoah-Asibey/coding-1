# FOR Loop is type loop that goes through a 
# a list and filters the value

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == 'banana':
        fruits.remove(x)
    print(x)

grades =[80,90,70,70,100,60]
for x in grades:
    if x <= 70:
        grades.remove(x)
    print(x)    
