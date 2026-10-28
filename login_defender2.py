# Automated Brute-Force Defender
# A simple login terminal that protects an account from repeated incorrect password attempts.

master_password = "Charles@1234567"
failed_attempts = 0
maximum_attempts = 5
# Keep asking for a password until access is granted or the
# maximum number of failed attempts has been reached.
while failed_attempts < maximum_attempts:

    entered_password = input("Enter your password: ")

    # An empty response may be an accidental Enter key press.
    # Give the user another chance without counting it as a failure.
    if entered_password == "":
        print("[WARNING] Password cannot be empty. Try again.")
        continue

    # Check the supplied password against the stored password.
    if entered_password == master_password:
        print("[ACCESS GRANTED] WELCOME_CHARLES!")
        break

    else:
        failed_attempts = failed_attempts + 1
        remaining_attempts = maximum_attempts - failed_attempts

        print("[ACCESS DENIED] Incorrect password.")

        # It Locks the account immediately after the fifth failed attempt.
        if failed_attempts == maximum_attempts:
            print("[ALERT] Excessive failed logins. Account locked!")
            break

        print("Attempts remaining:", remaining_attempts)
print("Login session ended.")