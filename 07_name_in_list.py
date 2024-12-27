# Name in list

l = ["harry","soham","soumya","pritam"]

name= input("enter your name: ")

if(name.lower() in l):
    print(f"Congratulations {name}, you are selected")
else:
    print(f"Sorry {name}, you are not selected")