# function definition  

# create a function that will determine what level of edcation 
# a college student is in, based on the number of years 
# they've been in school.

# function definition 
def titleBySchoolYear(year):
    if year == 1:
        print('Im a freshman')
    elif year == 2: 
        print('im a sophmore')
    elif year == 3:
        print('ima a junior')
    elif year == 4:
        print('ima a senior')
    elif year == 5 or year ==6:
        print('Youre in gradg school getting your masters degree') 
    elif year == 7 or year == 8:
        print('youre in grade school getting your doctorate.')    
    else: 
        print(' error: didnt recognize input') 

titleBySchoolYear(7)                       