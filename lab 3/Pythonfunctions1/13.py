import random
def guess_number():
    x=random.randint(1,20)
    name=input("Hello! What is your name? ")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    cnt=0
    while True:
        guess=int(input("Take a guess"))
        if guess>x:
            print("Your guess is too high.")
            cnt+=1
        elif guess<x:
            print("Your guess is too low")
            cnt+=1
        else:
            break
    print(f"Good job, {name}! You guessed my number in {cnt} guesses!")
guess_number()