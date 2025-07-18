import random, time

random.seed(time.time())

def main():
    print("Welcome to the Monty Hall Game!")
    monty_hall()


def monty_hall():
    red = "🔴"
    green = "🟢"
    blue = "🔵"

    doors = [red, green, blue]
    prize = random.choice(doors)
    
    while True:
        choice = input(f"Choode one of the following doors: {red}, {green}, {blue}: ").strip().lower()
        if choice not in [red, green, blue] and choice not in ["red", "green", "blue"]:
            print("Invalid choice. Please choose a valid door.")
            continue
        else:
            choice = red if choice in ["red", "🔴"] else green if choice in ["green", "🟢"] else blue

    


if __name__ == "__main__":
    main()