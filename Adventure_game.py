def start_adventure():
    print("You wake up in a dark forest. The air is thick with mystery. Which way do you go?")
    choice = input("Enter 'left' or 'right': ")

    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("Invalid choice. Try again.")
        start_adventure()

def left_path():
    print("You enter a dense thicket. You hear a rustling sound...")
    choice = input("Do you 'investigate' or 'run'? ")

    if choice == "investigate":
        encounter_wild_animal()
    elif choice == "run":
        print("You run away, but the animal chases you. Game Over!")
    else:
        print("Invalid choice. Try again.")
        left_path()

def encounter_wild_animal():
    print("A wild animal appears! It looks injured and scared.")
    choice = input("Do you 'help' the animal or 'attack'? ")

    if choice == "help":
        print("The animal calms down and transforms into a magical creature! It grants you a wish. You win!")
    elif choice == "attack":
        print("You attack the animal, but it fights back fiercely. Game Over!")
    else:
        print("Invalid choice. Try again.")
        encounter_wild_animal()

def right_path():
    print("You come across a mysterious cave. Do you 'enter' or 'go back'?")
    choice = input("Enter 'enter' or 'back': ")

    if choice == "enter":
        cave_exploration()
    elif choice == "back":
        print("You decide to return to the forest. Game Over!")
    else:
        print("Invalid choice. Try again.")
        right_path()

def cave_exploration():
    print("Inside the cave, you find ancient drawings on the walls and a strange glowing stone.")
    choice = input("Do you 'examine' the drawings or 'take' the stone? ")

    if choice == "examine":
        print("The drawings tell the story of a lost civilization. You gain knowledge and wisdom. You win!")
    elif choice == "take":
        print("As you take the stone, the cave begins to collapse! You barely escape. Game Over!")
    else:
        print("Invalid choice. Try again.")
        cave_exploration()

def character_development():
    print("As you journey through the forest, you meet a wise old man.")
    choice = input("Do you 'talk' to him or 'ignore' him? ")

    if choice == "talk":
        print("The old man shares valuable advice about the forest. You gain a new skill: 'Survival'.")
        # This skill could affect future choices
    elif choice == "ignore":
        print("You miss out on valuable information. The forest becomes more dangerous. Game Over!")
    else:
        print("Invalid choice. Try again.")
        character_development()

print("Welcome to the Adventure Game!")
character_development()  # Introduce character development before starting the adventure
start_adventure()