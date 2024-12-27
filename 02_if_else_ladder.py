# Age of consent

n=int(input("enter your age : ") )

if(n>=18):
    print(f"You're {n} i.e. above age of consent.")
     
elif(n<=0):
    print("0 and negative age is not valid")

else:
    print(f"You're {n} i.e. below age of consent")