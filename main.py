# Day 8 of 100 for the Udemy Python Bootcamp

# A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

# Write your code below this line 👇
def prime_checker(number):
    prime_number = True
    for i in range(2, number):
        if number % i == 0:
            prime_number = False
    if prime_number == True:
        print("This is a prime number.")
    else:
        print("This isn\'t a prime number")
# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
