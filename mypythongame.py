while True:
    print("(to run secret route: type 'go deeper in house', followed by 'keep going', 'keep going', 'keep going'.)")
    answer = input("You find yourself in a house filled with many cats. Which one do you pet? Options: Orange, Pink, and Muddy. ")

# beginning of orange route

    if answer == "Orange":
        print("He is orange, and he tells you his name is Eggs.")
        print("a) poke his nose")
        print("b) pick him up")
        answer = input("What do you do? ")

        # poke route
        if answer == "a":
            print("Nothing happened, but now Eggs thinks you're weird. Game over.")
            break

        # pick up route
        if answer == "b":
            print("Congratulations! He's yours. Go home a happy new parent, the end.")
            break

# beginning of pink route

    if answer == "Pink":
        print("You chose the magic cat! Well done. It's glowing now.")
        print("a) run")
        print("b) pet")
        answer = input("What do you do?")

        # if run chosen
        if answer == "a":
            print("Why would you do that? Should have pet the cat, loser. Game over")
            break

        # if pet chosen
        if answer == "b":
            print("He's purring and glittering now.")
            print("a) keep petting")
            print("b) leave")
            answer = input("What do you do? ")

            # keep petting route
            if answer == "a":
                print("Wow! You died in a flood of glitter, and then the cat ate you. You died in the coolest way possible.")
                break

            # leaving route
            if answer == "b":
                print("You left. Good choice! Leave that weird house behind you. You win, but you're boring.")
                break


# muddy route

    if answer == "Muddy":
        print("He's nice, but stinky. Game over!")
        break


# secret route

    if answer == "go deeper in house":
        answer = input("Oh! You didn't pet any cats. That's strange. Go back. (cd..) ")
        if answer == "keep going":
            answer = input("I told you to go back! Stop that! Go pet a cat! ")
            if answer == "keep going":
                answer = input("You'll regret this. Enter room draft is coming from? ")
                if answer == "keep going":
                    print("There's a really fat puppy in the room. He eats your toes! Game over.")
                    break
