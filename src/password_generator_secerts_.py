import string
import secrets
import random


def analyze_password(password):
    """Count how many of each type of character the password has."""
    return {
        "length": len(password),
        "uppercase": sum(1 for c in password if c.isupper()),
        "lowercase": sum(1 for c in password if c.islower()),
        "numbers": sum(1 for c in password if c.isdigit()),
        "special": sum(1 for c in password if c in string.punctuation),
    }


def check_strength(stats):
    score = 0

    if stats["length"] >= 8:
        score += 1
    if stats["length"] >= 12:
        score += 1
    if stats["uppercase"] > 0:
        score += 1
    if stats["lowercase"] > 0:
        score += 1
    if stats["numbers"] > 0:
        score += 1
    if stats["special"] > 0:
        score += 1

    if score <= 3:
        return "Weak"
    elif score <= 5:
        return "Medium"
    else:
        return "Strong"


def generate_password(length):
    """Generate a random password using the secrets module.

    It always includes at least one uppercase letter, one lowercase letter,
    one number and one special character, so the user is never asked y/n.
    """
    # One guaranteed character from each type
    password_chars = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation),
    ]

    # Fill the rest with random characters from all types
    all_characters = (
        string.ascii_uppercase
        + string.ascii_lowercase
        + string.digits
        + string.punctuation
    )
    for _ in range(length - len(password_chars)):
        password_chars.append(secrets.choice(all_characters))

    # Shuffle so the guaranteed characters are not always at the start
    random.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)


def show_analysis(password):
    stats = analyze_password(password)

    print("\nPassword Analysis:")
    print(f"  Total characters  : {stats['length']}")
    print(f"  Uppercase letters : {stats['uppercase']}")
    print(f"  Lowercase letters : {stats['lowercase']}")
    print(f"  Numbers           : {stats['numbers']}")
    print(f"  Special characters: {stats['special']}")

    print("\nPassword Strength:")
    print(check_strength(stats))


def get_length():
    while True:
        try:
            length = int(input("\nPassword length (8-64): "))

            if 8 <= length <= 64:
                return length

            print("Please enter a number between 8 and 64.")

        except ValueError:
            print("Please enter a valid number (digits only).")


def main():
    print("=" * 45)
    print("        PASSWORD GENERATOR & CHECKER")
    print("=" * 45)

    while True:
        print("\n1. Generate a strong password")
        print("2. Check my own password")
        print("3. Quit")

        choice = input("\nChoose an option (1/2/3): ").strip()

        if choice == "1":
            length = get_length()
            password = generate_password(length)

            print("\nGenerated Password:")
            print(password)
            show_analysis(password)

        elif choice == "2":
            password = input("\nEnter the password to check: ")

            if not password:
                print("Password cannot be empty.")
                continue

            show_analysis(password)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Please choose 1, 2 or 3.")


if __name__ == "__main__":
    main()