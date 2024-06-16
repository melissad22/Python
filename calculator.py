# Melissa Dunlap CS50 calculator


x = float(input("What is x? "))
y = float(input("What is y? "))

#rounded result
z = round(x / y, 2)

# print float rounded to 2 after decimal
print(f"{z:2f}")

# prints a comma for 1,000s
# print(f"{z:,}")
