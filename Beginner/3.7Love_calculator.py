print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name = name1.lower()+name2.lower()
t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")
l = name.count("l")
o = name.count("o")
v = name.count("v")
first_num = t+r+u+e
sec_num = l+o+v+e
love_percentage = int(str(first_num)+str(sec_num))
if(love_percentage < 10 or love_percentage > 90):
  print(
      f"Your score is {love_percentage}, you go together like coke and mentos.")
elif(love_percentage > 40 and love_percentage < 50):
  print(f"Your score is {love_percentage}, you are alright together.")
else:
  print(f"Your score is {love_percentage}.")
