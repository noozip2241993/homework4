import random
def generating_two_integers():
    """Generating randomly two positive one-digit integers and return values as a tuple"""
    digit1= random.randrange(10)
    digit2= random.randrange(10)
    return (digit1,digit2) #pack two integers'value into a tuple
num1, num2 = generating_two_integers()
def checking_answer(num1,num2):
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
checking_answer(num1,num2)
