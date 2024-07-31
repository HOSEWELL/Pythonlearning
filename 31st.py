#31st assignment

# Get the number from the user
number = int(input("Enter a number: "))

# Get the number of multiples from the user
multiples = int(input("Enter the number of multiples: "))

# Loop through and print the multiplication table
print(f"Multiplication table for {number} up to {multiples} multiples:")
for i in range(1, multiples + 1):
    print(f"{number} x {i} = {number * i}")


#(2)
# Get the number from the user
number = int(input("Enter a number: "))

# A flag variable to indicate if the number is prime
is_prime = True

# Check if the number is less than 2 (since 2 is the smallest prime number)
if number < 2:
    is_prime = False
else:
    # Initialize a divisor to 2
    divisor = 2

    # Use a while loop to check for factors of the number
    while divisor <= number // 2:
        if number % divisor == 0:
            is_prime = False
            break
        divisor += 1

# Print the result
if is_prime:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")


#(3)
# Get the number of rows for the triangle from the user
rows = int(input("Enter the number of rows: "))

# Use a for loop to print each row of the triangle
for i in range(1, rows + 1):
    # Print 'i' stars on the 'i'th row
    for j in range(i):
        print("*", end="")
    # Move to the next line after printing stars in the current row
    print()