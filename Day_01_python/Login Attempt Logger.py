# Scenario 12: Login Attempt Logger
# Requirement

# Track login attempts.

# Input:

# attempts = 5
# Expected
# Attempts Remaining: 0

# Account Locked

# if attempts ≥ 5.

# Else:

# Attempts Remaining: X

attempts = int(input("Enter number of login attempts: "))
if attempts >= 5:
    print("Account Locked")
else:
    remaining_attempts = 5 - attempts
    print(f"Attempts Remaining: {remaining_attempts}")