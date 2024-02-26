import art
print(art.logo)

def addition(numberOne, numberTwo):
    return(numberOne + numberTwo)

def subtraction(numberOne, numberTwo):
    return(numberOne - numberTwo)

def multiplication(numberOne,numberTwo):
    return(numberOne * numberTwo)

def division(numberOne, numberTwo):
    return(numberOne / numberTwo)

numberOne = float(input("Enter your first number: "))
operand = input("+\n-\n*\n/\nPick your operand: ")
numberTwo = float(input("Enter your second number: "))
userChoice = ''

def calculating():
    if operand == '+':
        final = addition(numberOne, numberTwo)
        return(final)

    if operand == '-':
        final = subtraction(numberOne, numberTwo)
        return(final)

    if operand == '*':
        final = multiplication(numberOne, numberTwo)
        return(final)

    if operand == '/':
        final = division(numberOne, numberTwo)
        return(final)
    else:
        print("Invalid input! Start Over.")
        return

while userChoice != 'no':
    userNum = calculating()
    print(userNum)
    userChoice = input('Would you like to continue with this number? yes or no: ').lower()
    numberOne = userNum
    operand = input("+\n-\n*\n/\nPick your operand: ")
    numberTwo = float(input("Enter your second number: "))
