import re

def password_strength(password):
    # Criteria checks
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r"[A-Z]", password) is not None
    lowercase_criteria = re.search(r"[a-z]", password) is not None
    number_criteria = re.search(r"\d", password) is not None
    special_char_criteria = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None

    # Calculate score based on criteria met
    score = sum([
        length_criteria,
        uppercase_criteria,
        lowercase_criteria,
        number_criteria,
        special_char_criteria
    ])

    # Determine password strength
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    # Feedback for user
    feedback = []
    if not length_criteria:
        feedback.append("- Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("- Include at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("- Include at least one lowercase letter.")
    if not number_criteria:
        feedback.append("- Include at least one number.")
    if not special_char_criteria:
        feedback.append("- Include at least one special character (e.g., !@#$%^&*).")

    return strength, feedback

def main():
    print("Password Strength Checker")
    password = input("Enter a password to check its strength: ")

    strength, feedback = password_strength(password)

    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("Feedback to improve your password:")
        for item in feedback:
            print(item)
    else:
        print("Your password is very strong. Good job!")

if __name__ == "__main__":
    main()
