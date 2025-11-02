def is_prime(n):
    if n <= 1:
        return False
    print(int(n**0.5)+1)
    for i in range(2, int(n**0.5)+1):
        print(i)
        nn = n%i
        print(f"{n} % {i} = {nn}")
        if nn ==0:
            return False
    return True

print("Starting program...\n")
num = int(input("Enter a number:"))
if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
