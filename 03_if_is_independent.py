# if statements are independent but else and elif are dependent to corresponding if.

a = int(input("enter number: "))

# If statement 1
if(a%2==0):
    print(f"{a} is even")
# No else nor elif is used under this if statement

# If statement 2
if(a>+18):
    print("You're an adult.")

else:
    print("You're a minor.")