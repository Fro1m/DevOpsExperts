# # First challenge assignment
# for i in range(1, 6):
#     for j in range(i):
#         print("*", end="")
#     print()

# # Second challenge assignment
# size = 81
# for i in range(size):
#     for j in range(size):
#         if i == j or i == size - j - 1:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()


# # Third challenge assignment
# def get_number_from_user():
#     user_input = input('Enter a number: ')
#     return int(user_input)


# def compute_sum_of_digits():
#     user_input = get_number_from_user()
#     length_of_input = len(str(user_input))
#     total_sum = 0
#     for i in range(length_of_input):
#         number_to_divide = int('1' + (length_of_input - 1) * '0')
#         meanwhile_sum = int(user_input / number_to_divide)
#         total_sum += meanwhile_sum
#         length_of_input -= 1
#         user_input -= number_to_divide * meanwhile_sum
#     print(total_sum)
#
#
# compute_sum_of_digits()
