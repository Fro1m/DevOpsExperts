a = int(input('enter number: '))
b = int(input('enter one more: '))

try:
    result = a / b
except BaseException as e:
    print("something went wrong")
    print(e.args)
    