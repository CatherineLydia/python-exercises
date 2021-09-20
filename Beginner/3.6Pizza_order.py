print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

if(size == 'S'):
  if(add_pepperoni == 'Y'):
    bill_amt = 17
  else:
    bill_amt = 15
elif(size == 'M'):
  if(add_pepperoni == 'Y'):
    bill_amt = 23
  else:
    bill_amt = 20
elif(size == 'L'):
  if(add_pepperoni == 'Y'):
    bill_amt = 28
  else:
    bill_amt = 25
if(extra_cheese == 'Y'):
  bill_amt += 1
print(f"Your final bill is:${bill_amt}")
