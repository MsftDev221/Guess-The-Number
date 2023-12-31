import random


def evaluate(check: int, against: int) -> tuple[str, bool]:
    if (check > against):
        return ("Your number is greater than the generated one. Try again", False)
    elif (check < against):
        return ("Your number is less than the generated one. Try again.", False)
    else:
        return (f"That's it! The generated number was {against}!", True)


def get_input(_msg: str) -> int:
    num = input(_msg)

    while (not num.isdecimal()):
        num = input("I can only accept whole numbers. Try again")

    return int(num)


def main():
    computer_number: int = random.randint(1, 100)

    user_input = get_input(
        "The computer has generated a random number from 1-100. Try guessing it!\n")

    result = evaluate(user_input, computer_number)
    print(result[0])

    while (result[1] == False):
        user_input = get_input("")

        result = evaluate(user_input, computer_number)
        print(result[0])

    return 0


if __name__ == "__main__":
    main()
