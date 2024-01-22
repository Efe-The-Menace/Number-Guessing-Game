try:
    from random import randint

    guess = int(input("Pick a number from 1 to 100.\n"))
    answer = randint(1, 10)


    while guess != answer:

        if guess < 1 or guess > 100:
            print("Common!! A number from 1 to 100.\n")
            guess = int(input("Pick again\n."))

        elif guess < answer:
            print("Too low.")
            guess = int(input("Pick again.\n"))

        else:
            print("Too high.")
            guess = int(input("Pick again.\n"))

        

    print("CORRECT!!")


except Exception as e:
    print(e)