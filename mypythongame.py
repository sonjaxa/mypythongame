while True:
    answer = input("You find yourself in a house filled with many cats. Which one do you pet? Options: Orange, Pink, and Muddy. Secret route: go deeper in house, keep going, keep going, keep going. ")

# beginning of orange route

    if answer == "Orange":
        answer = input("He is orange, and he tells you his name is Eggs. What do you do? Options: PokeNose, PickUp ")
        if answer == "PokeNose":
            print("Nothing happened, but now Eggs thinks you're weird. Game over.")
            break
        if answer == "PickUp":
            print("Congratulations! He's yours. Go home a happy new parent, the end.")
            break

# beginning of pink route

    if answer == "Pink":
        answer = input("You chose the magic cat! Well done. It's glowing now. What do you do? Your options: Run, Pet ")
        if answer == "Run":
            print("Why would you do that? Should have pet the cat, loser. Game over")
            break
        if answer == "Pet":
            answer = input("He's purring and glittering now. What do you do? Options: KeepPetting, Leave ")
            if answer == "KeepPetting":
                print("Wow! You died in a flood of glitter, and then the cat ate you. You died in the coolest way possible.")
                break
            if answer == "Leave":
                print("You left. Good choice! Leave that weird house behind you. You win, but you're boring.")
                break

# muddy route

    if answer == "Muddy":
        print("He's nice, but stinky. Game over!")
        break

# secret route

    if answer == "go deeper in house":
        answer = input("Oh! You didn't pet any cats. That's strange. Go back. (cd..)")
        if answer == "keep going":
            answer = input("I told you to go back! Stop that! Go pet a cat! ")
            if answer == "keep going":
                answer = input("You'll regret this. Enter room draft is coming from? ")
                if answer == "keep going":
                    print("There's a really fat puppy in the room. He eats your toes! Game over.")
                    break
