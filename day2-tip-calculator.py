#if bill was $150, split between 5 people with 12% tip (150.00 / 5) * 1.12
#round result to 2 decimal places

print("Welcome to the tip calculator! :)")
bill = float(input("What was the total bill? $"))
tip = int(input("How much percentage of the total bill do you want to pay? 10, 12 or 15 "))
people = int(input("How many people to split bill between? "))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")