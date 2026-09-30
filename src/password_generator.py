import secrets
import string
#password function 
def generate_password(length, use_uppercase, use_lowercase,
                      use_numbers, use_symbols):

    characters = ""

    if use_uppercase:
        characters += string.ascii_uppercase

    if use_lowercase:
        characters += string.ascii_lowercase

    if use_numbers:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type must be selected.")

    password = "".join(
        secrets.choice(characters)
        for _ in range(length)
    )

    return password
# password strength checker 
def check_strength(password):

    score = 0

    if len(password) >= 8:
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(char in string.punctuation for char in password):
        score += 1

    if score <= 2:
        return "Weak"

    elif score <= 4:
        return "Moderate"

    else:
        return "Strong"


#Get user input 
def get_yes_no(question):

    while True:

        answer = input(question + " (y/n): ").strip().lower()

        if answer in ["y", "yes"]:
            return True

        if answer in ["n", "no"]:
            return False

        print("Please enter y or n.")

#main function 
def main():

    print("=" * 45)
    print("        PASSWORD GENERATOR")
    print("=" * 45)

    while True:

        try:
            length = int(input("\nPassword length: "))

            if length < 4:
                print("Password length should be at least 4.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    use_uppercase = get_yes_no("Include uppercase letters?")
    use_lowercase = get_yes_no("Include lowercase letters?")
    use_numbers = get_yes_no("Include numbers?")
    use_symbols = get_yes_no("Include special characters?")

    try:

        password = generate_password(
            length,
            use_uppercase,
            use_lowercase,
            use_numbers,
            use_symbols
        )

        print("\nGenerated Password:")
        print(password)

        print("\nPassword Strength:")
        print(check_strength(password))

    except ValueError as error:

        print("\nError:", error)

if __name__ == "__main__":
    main()