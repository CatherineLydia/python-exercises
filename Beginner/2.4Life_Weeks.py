age = input("What is your current age?")

total_months = (90*12)
total_weeks = (90*52)
total_days = (90*365)

my_months = (int(age)*12)
my_weeks = (int(age)*52)
my_days = (int(age)*365)

rem_months = total_months-my_months
rem_weeks = total_weeks-my_weeks
rem_days = total_days-my_days

print(
    f"You have {rem_days} days, {rem_weeks} weeks, and {rem_months} months left.")
