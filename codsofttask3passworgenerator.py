#----program to generate password for user according to the length they want

import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGH1234567890@#$%^&*"

while 1:
    password_len = int(input("Enter the length of the password you want : "))
    #---- we will ask user what length of password they want
    password_num = int(input("Number of passwords you want to genrate : "))
    #---- we will ask user how much passwords they want

    for x in range(0,password_num):
        password = ""
        for x in range(0,password_len):
            password_char = random.choice(chars)
            password = password + password_char
        print("Your password generated is : ", password)

