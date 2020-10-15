import random
def create_question():
    num1= random.randrange(10)
    num2= random.randrange(10)
    return two_integers(num1,num2)

def two_integers(num1,num2):
    answer = num1*num2 
    while True:
        guess = int(input(f'How much is {num1} times {num2}? '))
        if guess == answer:
            print("This is a correct answer. Done!")
            break
        else:
            print(f"{num1} times {num2} is not {guess}, please try again!")
create_question()