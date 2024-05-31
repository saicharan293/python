import math
# for optimized performance
def prime_check(n):
    is_prime=True
    if n==1:
        is_prime=False
    for i in range(2,math.ceil(n/2)+1):
        if n%i==0:
            is_prime=False
        else:
            is_prime=True
    if is_prime:
        print(n,"is prime")
    else:
        print(n,"is not prime")

# using square root method: remarks=>error
# def prime_check(n):
#     is_prime=True
#     if n==1:
#         is_prime=False
#     print(math.ceil(math.sqrt(n)))
#     for i in range(2,math.ceil(math.sqrt(n))+1):
#         if n%i==0:
#             is_prime=False
#         else:
#             is_prime=True
#         # break
#     if is_prime:
#         print(n,'is prime number')
#     else:
#         print(n,'is not a prime number')

n=int(input('enter a number '))
prime_check(n)
