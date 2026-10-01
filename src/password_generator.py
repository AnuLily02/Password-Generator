import string


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

    # Length
    if stats["length"] >= 8:
        score += 1
    if stats["length"] >= 12:
        score += 1

    # Character types
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


def give_suggestions(stats):
    tips = []

    if stats["length"] < 12:
        tips.append("Use at least 12 characters.")
    if stats["uppercase"] == 0:
        tips.append("Add uppercase letters (A-Z).")
    if stats["lowercase"] == 0:
        tips.append("Add lowercase letters (a-z).")
    if stats["numbers"] == 0:
        tips.append("Add numbers (0-9).")
    if stats["special"] == 0:
        tips.append("Add special characters (!@#$%).")

    return tips


print("=" * 45)
print("        PASSWORD STRENGTH CHECKER")
print("=" * 45)

while True:
    password = input("\nEnter a password (or type 'quit' to exit): ")

    if password.lower() == "quit":
        print("Goodbye!")
        break

    if not password:
        print("Password cannot be empty.")
        continue

    stats = analyze_password(password)

    print("\nPassword Analysis:")
    print(f"  Total characters  : {stats['length']}")
    print(f"  Uppercase letters : {stats['uppercase']}")
    print(f"  Lowercase letters : {stats['lowercase']}")
    print(f"  Numbers           : {stats['numbers']}")
    print(f"  Special characters: {stats['special']}")

    print("\nPassword Strength:")
    print(check_strength(stats))

    tips = give_suggestions(stats)
    if tips:
        print("\nHow to make it stronger:")
        for tip in tips:
            print(f"  - {tip}")