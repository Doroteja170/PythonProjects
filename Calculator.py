def calculator(a,b,operator):
    if(operator=='+'):
        output=a+b
        return output
    elif(operator=='-'):
        output = a - b
        return output
    elif (operator == '*'):
        output = a * b
        return output
    elif (operator == '/'):
        output = a / b
        return output
    else:
        return f"Wrong input"

def calc():
    should_continue=True
    num1 = float(input("What's the first number?: "))
    while should_continue:
        print('+')
        print('-')
        print('*')
        print('/')
        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        output = calculator(num1, num2, operation)
        print(f'{num1}{operation}{num2}={output}')

        cont = input(f"Type 'y' to continue calculating with {output}, or 'n' if you want new calculation: ").lower()
        if cont == 'y':
            num1 = output
        else:
            print('\n'*100)
            should_continue = False
            calc()

calc()