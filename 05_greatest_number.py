a1=int(input("enter num 1 : "))
a2=int(input("enter num 2 : "))
a3=int(input("enter num 3 : "))
a4=int(input("enter num 4 : "))

if(a1>a2 and a1>a3 and a1>a4):
    print(f"{a1} is greatest1")
elif(a2>a1 and  a2>a3 and a2>a4):
    print(f"{a2} is greatest2")
elif(a3>a2 and a3>a1 and a3>a4):
    print(f"{a3} is greatest3")
elif(a4>a2 and a4>a3 and a4>a1):
    print(f"{a4} is greatest4")

print("done")