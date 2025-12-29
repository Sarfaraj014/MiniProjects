import random
alphabets=["a","b","c","d","e","f","g","h","i","j","k","l","l"]
numbers=["9","8","7","6","5","4","3","2","1"]
symboles=["@","#","*","-","$"]

# tkaing input by the user
alphaCount=input("how many alphabets you need")
numCount=input("how many number you need")
symbolcount=input("how many symbol do you need")

password=[]
# add random numbers and alphabets and symboles in a empty list
for i in range(0,int(alphaCount)):
   password.append(random.choice(alphabets))
for i in range(0,int(numCount)):
   password.append(random.choice(numbers))
for i in range(0,int(symbolcount)):
   password.append(random.choice(symboles))
# mixed the list password using random shuffle
random.shuffle(password)
# convert list to string --------
Password=''
for i in password:
   Password=Password+i
# printing
print(f"your password = {Password}")
