#Program to find a given number is prime or not.

#Funtion to check a number is prime or not
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        nn = n%i
        if nn ==0:
            return False
    return True

print("Starting program...\n")
num = int(input("Enter a number:"))
if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
