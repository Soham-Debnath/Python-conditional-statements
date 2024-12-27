# A student passes if 3 subjects' marks each > 33 % and total percentage > 40%
marks1 = int(input('enter marks 1 : '))
marks2 = int(input('enter marks 2 : '))
marks3 = int(input('enter marks 3 : '))
              
total_percentage = ((marks1 + marks2 + marks3)*100)/300

if(total_percentage>=40 and marks1,marks2,marks3 > 33):
    print(f"Your marks are {marks1,marks2,marks3} and total is {total_percentage} hence youre are passed.")
else:
    print(f"Your marks are {marks1,marks2,marks3} and total is {total_percentage} hence youre are failed.")
print("\n")
print("Good luck.")

