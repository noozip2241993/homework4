import random
def generating_defining_prime_number():
    """Checking whether the argument is a prime number or not"""
    for j in range(6): #generating six random numbers
        num = random.randrange(1,101)
        if num > 1: #prime numbers are greater than 1
            for i in range(2,num): #check for factors
                if(num%i)== 0:
                    print(num,"is not a prime number")
                    break
            else:
                    print(num,"is a prime number")
        else:
            print(num,"is not a prime number")
            #if input is less than or equal to 1, it is not a prime number
generating_defining_prime_number()
