# what is this question asking me to do
# we need to make a discount software

# we need the membership tier
# the item name and prrice

def shoppingDiscount(membership,itemName, itemPrice):
    if membership== 'superShopper':
        print('you will get 10 percent off your item')
        discountAmount = itemPrice * 0.1
        finalAmout = itemPrice -discountAmount
        print('congrats supershopper! you will get 10 percent off your item')
        print(finalAmount)
    elif membership== 'megaShopper':
        print('you will get 15 percent off your item')
        discountAmount = itemPrice * 0.15
        finalAmout = itemPrice -discountAmount
        print(finalAmount)
    elif membership== 'ultraShopper':
        print('you will get 20 percent off our item')
        discountAmount = itemPrice * 0.2
        finalAmout = itemPrice -discountAmount
        print(finalAmount)
    else:
        print('you do not have any membership benefits')

shoppingDiscount('superShopper',100)            