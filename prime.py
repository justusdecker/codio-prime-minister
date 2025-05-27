from math import sqrt

def is_divisible_by(number, by):
	return number % by == 0

def is_prime(number):
    #Only divisible by 1 and itself

    for i in range(2,int(sqrt(number)) + 1):
        if is_divisible_by(number,i):
            return False
    return True

def primes_in_range(start,end):
    for i in range(start,end):
        if is_prime(i):
            print(f"The number {i} is prime")
def main():
    start = int(input("Enter start range: "))
    end = int(input("Enter end range: "))
    primes_in_range(start, end)

if __name__ == "__main__":
    main()