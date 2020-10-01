#create a Fulty Calculator
#note that the calculations must be right except the following:
#45*3=555
#56+9=77
#56/6=4
######################################################################################
#FAULTY CALCULATOR
print("Enter the numbers for the calculation")
num_1=int(input())
num_2 = int(input())
print("Numbers entered for calculation:",num_1,num_2)
print("enter the operator for which you want to perform operation")
op=str(input())
print("Entered operator:",op)
if op == '+' or op == '-' or op == '*' or op == '/' or op == '%':
    if op == '*':
        if num_1 == 45 and num_2 == 3:
            print(555)
        else:
            print(num_1 * num_2)

    if op == '+':
        if num_1 == 46 and num_2 == 9:
            print(77)
        else:
            print(num_1 + num_2)

    if op == '/':
        if num_1 == 46 and num_2 == 6:
            print(4)
        else:
            print(num_1 / num_2)

    if op == '-':
        print(num_1 - num_2)

    if op == '%':
        print(num_1 % num_2)


else:
    print("Invalid Entry")
