class PrimeFilter:
    def __init__(self, numbers):
        self.numbers = numbers

    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_primes(self):
        return list(filter(lambda x: self.is_prime(x), self.numbers))

numbers = [1, 2, 3, 4, 5, 6, 7, 11, 7, 13, 8, 8, 15, 17, 19, 20, 23, 29]
pf = PrimeFilter(numbers)
print(pf.get_primes())