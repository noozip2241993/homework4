import random

for i in range(6):
    num = random.randrange(1,101)
    def prime():
        """Checking whether num is a prime or not"""
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
    prime()
   
