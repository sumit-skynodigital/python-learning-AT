# Scenario 9: OTP Verification
# Business Requirement

# OTP is:

# 123456

# User gets 3 attempts.

# Expected

# Correct OTP:

# Access Granted

# Wrong OTP:

# Try Again

# After 3 failures:

# Account Locked
# Stretch Goal

# Implement attempt counter.

# Concepts Used
# Variables
# If Else

correct_otp = "123456"
attempts = 0
max_attempts = 3
while attempts < max_attempts:
    user_otp = input("Enter OTP: ")
    if user_otp == correct_otp:
        print("Access Granted")
        break
    else:
        attempts += 1
        if attempts < max_attempts:
            print("Try Again")
        else:
            print("Account Locked")

