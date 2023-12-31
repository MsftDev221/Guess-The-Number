import random


def evaluate(check: int, against: int) -> tuple[str, bool]:
    """
    Compare a user-provided number with a generated number and provide feedback.

    Parameters:
    - check (int): The user-provided number for comparison.
    - against (int): The generated number to compare against.

    Returns:
    tuple[str, bool]: A tuple containing two elements:
        - A string providing feedback on the comparison result.
        - A boolean indicating the success of the comparison (True if numbers are equal, False otherwise).
    """
    if (check > against):
        return ("Your number is too high! Try again.", False)
    elif (check < against):
        return ("Your number is too low! Try again.", False)
    else:
        return (f"That's it! The generated number was {against}!", True)


def get_input(_: str) -> int:
    """
    Prompt the user for input and ensure the input is a valid integer.

    Parameters:
    - _msg (str): The message displayed to prompt the user for input.

    Returns:
    int: The valid integer entered by the user.

    Raises:
    ValueError: If the user enters a non-integer value.
    """
    num = input(_)

    try:
        int(num)
    except ValueError:
        return False

    return int(num)


def main():
    """
    Starting point of guess the computer-generated random number game.

    This script generates a random number between 1 and 100, then prompts the user to guess it.
    After each guess, the script provides feedback on whether the guess is too high, too low, or correct.

    Usage:
    1. Run the script.
    2. Enter your guess when prompted.
    3. Receive feedback until you correctly guess the generated number.

    Note: This script uses the `get_input` and `evaluate` functions.
    """
    computer_number: int = random.randint(1, 100)

    user_input = get_input(
        "The computer has generated a random number from 1-100. Try guessing it!\n")

    while (user_input == False):
        user_input = get_input("")

    result = evaluate(user_input, computer_number)
    print(result[0])

    while (result[1] == False):
        user_input = get_input("")

        result = evaluate(user_input, computer_number)
        print(result[0])


if __name__ == "__main__":
    main()
