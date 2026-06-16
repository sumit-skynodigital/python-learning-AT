# Scenario 11: Password Policy Validator
# Requirement

# Password must:

# Be at least 8 characters.
# Test Data
# Password	Expected
# admin	Invalid
# admin123	Valid
# pass12	Invalid
# password123	Valid
# Concepts Used
# len()
# If Else

password = input("Enter password: ")
if len(password) >= 8:
    print("Valid")
else:
    print("Invalid")
    
