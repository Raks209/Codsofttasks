# Firstly take inputs from the user
x = int(input("Enter the first number"))
y = int(input("Enter the second number"))

ch= 0
# Provide menu to the  user that what operation they want to perform 
while ch<6 :
    print('1. Percentage')
    print('2. Multiply')
    print('3. Divide')
    print('4.Addition')
    print('5.Subtraction')
    print('6.Exit')
    ch=int(input('enter the choice of operation you want to perform :'))
    
    # Use the if else loop to take choices from the user 

    if ch==1:
        z=x%y    
        print('The percentage between these number is :',z)

    elif ch==2:
        z=x*y
        print('The product of these number is :',z)

    elif ch==3:
        z=x/y
        print('The quotient of these number is:',z)

    elif ch==4:
        z=x+y
        print('The sum of these number is:',z)

    elif ch==5:
        z=x-y
        print('The difference of these number is:',z)

    elif ch==6:
        break

    else :
        print('The operation choosen do not exist')
