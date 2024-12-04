# discuss the anatomy of a function


# this is a function definition
# it tells the cumputer the instructions
# on what we want it to do wiht data

# data = just means data types

# () curly bracket- these are for passing in
#data

# when the bracket are in a function
# definition, they are called parameters
# parameters= placeholder
#def customeNameFunction(name):
#    print('new nickname is : super'+ name)

# when we want to use a function
# we call it by writing its name
# whenw e pass dtaa inside of the brackets
# it is now called an argument
# argument = requires facts/ real data 
#customeNameFunction('James')

# lesson on conditional statements
# conditional statements invole the
#'IF' and 'ELSE' keywords.
# IF were looking for a condition we can
# run or code, otherwise or ELSE it will
# doing something else on defult

def verifyAge(age):
    if age> 17:
        print('congrats you can play GTA VI')
    else:
        print('Sorry, you need am adult to get this game.')   

verifyAge(18)  


# Activity

def hourssToMinutes(hour):
    print(hour* 60)

# argument- real data inside of the function call
hourssToMinutes(3)    

# conditional statemnt
# IF/ else