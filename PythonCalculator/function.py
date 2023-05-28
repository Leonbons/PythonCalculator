def addition(num1, num2): #här defineras operationerna
    result = num1 + num2
    print("{0} + {1} = {2}". format(num1, num2, result))
def subtraction(num1, num2):
    result = num1 - num2
    print("{0} - {1} = {2}". format(num1, num2, result))
def multiplication(num1, num2):
    result = num1 * num2
    print("{0} * {1} = {2}". format(num1, num2, result))
def division(num1, num2): #Om num2 är 0 så bryts det annars går det
    if num2 == 0.0:
        print("Det går inte att dividera med 0")
    else: 
        result = num1 / num2
        print("{0} / {1} = {2}". format(num1, num2, result))
def squared(num1, num2):
    result = num1 ** num2
    print("{0} ** {1} = {2}". format(num1, num2, result))

