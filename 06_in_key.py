#IN key
#  detect spam
a1= "make money online"
a2= "buy this"
a3= "click this"
a4= "subscribe it"

statement = input("enter your comment: ")
 
if((a1 in statement.lower()) or (a2 in statement.lower()) or (a3 in statement.lower()) or (a4 in statement.lower())):
    print("spam")

else:
    print('not spam')