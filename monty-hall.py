import random, time

random.seed(time.time())

def main():
    print("Welcome to the Monty Hall Game!\n")
    if monty_hall():
        print("Congratulations! You won the prize!")
    else:
        print("Unfortunately, you didn't win this time. Play again!")


def monty_hall():
    # initialize colors
    red = "🔴"
    green = "🟢"
    blue = "🔵"

    # make a list to be able to use random.choice
    colors = [red, green, blue]

    # randomly choose a color for the prize
    prize = random.choice(colors)
    
    # get user's choice and validate it
    while True:
        choice = input(f"Choode one of the following colors:\n{red} || {green} || {blue}\n\n").strip().lower()
        if choice not in colors and choice not in ["red", "green", "blue"]:
            print("Invalid choice. Please choose a valid door.")
            continue
        else:
            choice = red if choice in ["red", "🔴"] else green if choice in ["green", "🟢"] else blue
            break

    # populate a list of empty colors
    busts = [color for color in colors if color != prize]

    # choose a color to reveal a bust
    while True:
        reveal = random.choice(busts)
        if reveal != choice:
            break

    # ask the user if they want to switch their choice + validate
    while True:
        decision = input(f"{reveal} was an empty color. Would you like to switch your choice? (yes/no)\n").strip().lower()

        # remove the revealed color from the options
        busts.remove(reveal)
        colors.remove(reveal)

        if decision in ["yes", "y"]:
            for color in colors:
                if color != choice:
                    choice = color
                    break
            break
        elif decision in ["no", "n"]:
            break
        else:
            print("Invalid input. Please answer with 'yes' or 'no'.")

    # check if the user's choice is the prize
    return choice == prize


if __name__ == "__main__":
    main()