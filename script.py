# Script to display and save prime numbers between 1 and 250

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


primes = []

# Find prime numbers
for number in range(1, 251):
    if is_prime(number):
        primes.append(number)

# Display primes
print("Prime numbers between 1 and 250:")
for p in primes:
    print(p)

# Save results to file
with open("results.txt", "w") as file:
    file.write("Prime numbers between 1 and 250:\n")
    for p in primes:
        file.write(str(p) + "\n")

print("\nResults have been saved to results.txt")