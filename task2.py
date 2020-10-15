import random
def generating_two_integers():
    """Generating randomly two positive one-digit integers and return values as a tuple"""
    num1= random.randrange(10)
    num2= random.randrange(10)
    return two_integers(num1,num2) #pack two integers'value into a tuple

def two_integers(num1,num2):
    """Checking guess with the answer"""
    answer = num1*num2 
    while True:
        guess = int(input(f'How much is {num1} times {num2}? '))
        if guess == answer:
            print("This is a correct answer. Done!")
            break
        else:
            print(f"{num1} times {num2} is not {guess}, please try again!")
generating_two_integers()
