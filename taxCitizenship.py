type_of_citizen = input("Enter type of citizen (individual/senior/super senior): ")
income = int(input("Enter annual income: "))

if type_of_citizen == 'individual':
    if income < 250000:
        tax = 0
    elif income <= 500000:
        tax = income * 0.05
    elif income <= 1000000:
        tax = 12500 + income * 0.2
    else:
        tax = 112500 + income * 0.3

elif type_of_citizen == "senior":
    if income < 300000:
        tax = 0
    elif income <= 500000:
        tax = income * 0.3
    elif income < 1000000:
        tax = 10000 + income * 0.2
    else:
        tax = 110000 + income * 0.3

elif type_of_citizen == "super senior":
    if income < 500000:
        tax = 0
    elif income <= 1000000:
        tax = income * 0.2
    else:
        tax = 100000 + income * 0.3

else:
    tax = -1  # Invalid type_of_citizen input

print("Tax:", tax)
