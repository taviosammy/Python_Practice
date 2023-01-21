#simple code to practice nested if statements

# This is how you work out whether if a particular year is a leap year.

# on every year that is evenly divisible by 4 

# **except** every year that is evenly divisible by 100 

# **unless** the year is also evenly divisible by 400



# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

leap= "Leap year."
not_leap = "Not leap year."

if year % 4 == 0 :
    if year % 100 == 0:
        if year % 400 == 0:
            print(leap)
        else:
            print(not_leap)
    else:
        print(leap)
else:
    print(not_leap)