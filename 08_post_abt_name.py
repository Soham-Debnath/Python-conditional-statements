# Detect the post whethe it is talking about your name
your_name=input("enter your name: ")

post=input("enter your post: ")

if(your_name.lower() in post.lower()):
    print(f"Yes this post is taking about {your_name}")
else:
    print(f"No this post is not taking about {your_name}")
print("done")
      
