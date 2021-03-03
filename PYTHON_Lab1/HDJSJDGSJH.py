#Given the integer the number of min that passed since midnight - how many hours and min are displayed on the 24hr clock
#The program should print two numbers the number of hours ( between 0 and 23) and the number of minutes ( between 0 and 59).


N = int(input("enter the time past midnight:"))
hours = (N//60)
min = (N%60)
print(f"the hour is {hours}")
print(f"the min is {min}")
print(f"its {hours}:{min} now")
