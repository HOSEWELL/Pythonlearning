#31st assignment

# (1)
number = int(input("Enter a number: "))
multiples = int(input("Enter the second number: "))

print(f"Multiplication table for {number} up to {multiples} multiples:")
for i in range(1, multiples + 1):
    print(f"{number} x {i} = {number * i}")


#(2)
# Get the number from the user
number = int(input("Enter a number: "))

# A flag variable to indicate if the number is prime
is_prime = True
if number < 2:
    is_prime = False
else:
    # Initialize a divisor to 2
    divisor = 2
    while divisor <= number // 2:
        if number % divisor == 0:
            is_prime = False
            break
        divisor += 1
if is_prime:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")


#(3)
# Get the number of rows for the triangle from the user
rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()