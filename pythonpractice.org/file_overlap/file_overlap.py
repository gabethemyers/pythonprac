with open('happy_numbers.txt', 'r') as file:
   happys = file.readlines() 
   happys = [int(line.rstrip()) for line in happys]

with open('prime_number.txt', 'r') as file:
    primes = file.readlines() 
    primes = [int(line.rstrip()) for line in primes]


result = [elem for elem in primes if elem in happys]
print(result)