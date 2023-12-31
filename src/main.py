import random


def main():
    computer_number: int = random.randint(1, 100)

    user_input = input(
        "The computer has generated a random number. Try guessing it!\n")


if __name__ == "__main__":
    main()
