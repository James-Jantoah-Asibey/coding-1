# Loops - is a onstruct that repeats a set of 
# instructions under specific conditions.


# while - so long as a condition is true,
# keep repeating the loop.
x = 3
y = 'ian'
#while x == 2:
#while y == 'ian':
while 10 < 1:
    
    print('this text will repeat forever')


#expiration= input('what is todays date?:')    
#while expiration == '1/23/2025':
 #    print('this product has expired') 


def tripSavings():
     accountBalance = 0 
     tripGoal = 8000
     while accountBalance < tripGoal:
          depositAmount =  int (input('How much you want to despoit ?'))
          accountBalance = depositAmount + accountBalance 
          print('your new balance is '+ str(accountBalance))

tripSavings() 

def damageCounter():
    player1 = 100
    while player1 > 0:
        damage = input("How much damage is this attack doing? :")
        player1 -= damage
        print('Player1 health is now 'str(player1) +'healthpoints')

damageCounter()


def verifyPassword(password):


