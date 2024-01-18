#Prework question 1:
def hello_name(user_name):
    print("hello_" + user_name)

hello_name('Malachi')

#Prework question 2:
def first_odds():
    odd_number = 0
    while odd_number < 100:
        odd_number += 1
        if odd_number % 2 == 0:
            continue

        print(odd_number)

first_odds()

#Prework question 3:
def max_num_in_list(a_list):
    return max(a_list)

print(max_num_in_list(a_list=[5,34,1,78,92]))

#Prework question 4:
def is_leap_year(a_year):
    if a_year % 4 == 0:
        if int(a_year) % 100 != 0:
            print(True)
    else:
        print(False)

is_leap_year(2005)

#Prework question 5:
def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))

x = [1, 2, 3, 4, 5, 7]
print(is_consecutive(x))