import os
os.system('cls')
user_input = 0

def default_list():
    list_numbers_str = str([0,1,2,3,4,5,6,7,8,9])
    return list_numbers_str

def get_input():
    input_user = input('Enter Your number: ')
    input_user = input_user.split()
    list_for_appending = []
    for s in input_user:
        for i in s:
            if i in default_list():
                list_for_appending.append(i)
    return list_for_appending
    
def changer_type(list_for_appending):
    list_change_type = []
    for s in list_for_appending:
        if s in default_list():
            list_change_type.append(int(s)) 
    return list_change_type

print(sum(changer_type(get_input())))



