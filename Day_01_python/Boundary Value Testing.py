# Scenario 4: Boundary Value Testing
# Business Requirement

# Age field accepts:

# 18–60 years
# Task

# Validate age.

# Test Data
# Input	Expected
# 17	Invalid
# 18	Valid
# 19	Valid
# 59	Valid
# 60	Valid
# 61	Invalid
# Challenge

# Print:

# Boundary Value Pass

# or

# Boundary Value Fail

age= int(input("Enter age: "))
if age < 18 or age > 60:
    print("Boundary Value Fail")
else:
    print("Boundary Value Pass")
