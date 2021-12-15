ticket = int(input("Please input amount of tickets:"))
price = []
for i in range(1, ticket+1): # For i in a range from 1 to 999+, cause the tickets have to be more than 0
    age = int(input(f"Input the age {i} of customer: "))
    if age in range(0, 18):
        price.append(0)
    elif age in range(18, 25):
        price.append(990)
    elif age in range(25, 110):
        price.append(1390)
    else:
        print("Invalid value")
    if ticket > 3: # Discount in 10% if amount of tickets > 3 .
        print("Amount to pay with a 10% discount", sum(price) - ((sum(price) / 100) * 10), "rubles")
    else:
        print("Amount to pay:", sum(price), "rubles")
