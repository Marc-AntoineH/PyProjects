def collatz(number):
    if number % 2 == 0: # The number is even.
        print(number // 2)
        return number // 2
    else:
        result = 3 * number + 1 # The number is odd.
        print (result)
        return result

try:
    n = int(input("Choose any number: "))
    while n != 1:
        n = collatz(n)
except ValueError:
    print("Only positive number are allowed")
