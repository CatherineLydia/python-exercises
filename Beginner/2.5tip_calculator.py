print("Welcome to the tip calculator.")
bill_amt = input("What was the total bill? $")
tip_percentage = input(
    "What percentage tip would you like to give? 10,12 or 15?")
num_persons = input("How many people to split the bill?")
tip_amt = (float(bill_amt)*int(tip_percentage))/100
total_amt = float(bill_amt)+tip_amt
each_pay = total_amt/int(num_persons)
result = "{:.2f}".format(each_pay)
print(f"Each person should pay: ${result}")
