import random


def evaluate(check: int, against: int) -> tuple[str, bool]:
    if (check > against):
        return ("Your number is greater than the generated one. Try again", False)
    elif (check < against):
        return ("Your number is less than the generated one. Try again.", False)
    else:
        return (f"That's it! The generated number was {against}!", True)


def main():
    computer_number: int = random.randint(1, 100)

    user_input = input(
        "The computer has generated a random number. Try guessing it!\n")

    while (not user_input.isdecimal()):
        user_input = input(
            "The computer has generated a random number. Try guessing it!\n")

    user_input = int(user_input)


if __name__ == "__main__":
    main()
