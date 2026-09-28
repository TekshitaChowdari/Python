numbers = list(range(1, 51))
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
primes = list(filter(is_prime, numbers))
print("Prime numbers:", primes)


words = ["madam", "hello", "level", "world", "radar", "python"]
def is_palindrome(word):
    return word == word[::-1]
palindromes = list(filter(is_palindrome, words))
print("Palindromes:", palindromes)
#output:-
#Prime numbers: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
#Palindromes: ['madam', 'level', 'radar']

