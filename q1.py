import string


def check_password_strength(password):
    """
    Checks the strength of a password and provides feedback.

    Args:
        password (str): The password to check.

    Returns:
        str: A message indicating the password's strength.
    """
    feedback = []
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    # --- Character type checks ---
    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in string.punctuation:  # Checks for common special characters
            has_special = True

    # --- Build feedback messages ---
    if not has_lower:
        feedback.append("Password must contain at least one lowercase letter.")
    if not has_upper:
        feedback.append("Password must contain at least one uppercase letter.")
    if not has_digit:
        feedback.append("Password must contain at least one digit.")
    if not has_special:
        feedback.append("Password must contain at least one special character (!@#$%^&*() etc.).")

    # --- Evaluate password strength based on criteria and length ---
    if len(feedback) == 0:  # All character types are present
        if len(password) >= 8:
            return "Strong: Your password meets all criteria and is long enough."
        else:
            return "Weak: Your password meets character requirements but is too short. Make it longer."
    else:
        # Handle cases where character types are missing
        if len(password) < 8:
            feedback.append("Password is too short. Aim for at least 8 characters.")
        return f"Weak: " + "\n".join(feedback)


# --- User Input and Feedback ---
input_password = input("Enter your password: ")
result = check_password_strength(input_password)
print(result)
