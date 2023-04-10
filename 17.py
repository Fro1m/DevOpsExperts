# my_file = open("my_file.txt", "")
# for line in my_file.readlines():
#     print(line, end='')

def get_name_from_user():
    user_name = input('Please enter a name: ')
    my_file = open('names.txt', 'a')
    my_file.write(f"{user_name}\n")
    my_file.close()

def print_hello_and_user_name():
    my_file = open('names.txt', 'r')
    for line in my_file.readlines():
        print(f"Hello {line}", end='')

get_name_from_user()
print_hello_and_user_name()