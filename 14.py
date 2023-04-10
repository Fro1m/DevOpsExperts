#age = []
#for i in range(5):
#    age.append(int(input('enter your age: ')))
#print(max(age))


def until_moshe():
    list_of_names = []
    your_name = "stam harta"
    while your_name != 'moshe':
        your_name = input("what is your name?")
        list_of_names.append(your_name)
    return list_of_names


lets_check = until_moshe()
print(lets_check)

