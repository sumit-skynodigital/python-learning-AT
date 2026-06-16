# Scenario 1: Login Validation
# Business Requirement

# Users can log in only with valid credentials.

# Task

# Create a program that checks:

# Valid Username: admin
# Valid Password: Admin123
# Inputs to Test
# Username	Password	Expected Result
# admin	Admin123	Login Successful
# admin	wrongpass	Invalid Credentials
# wronguser	Admin123	Invalid Credentials
# empty	empty	Username Required
# admin	empty	Password Required
# Challenge

# Implement all validations.

# Concepts Used
# Variables
# Input
# If Else

username = input("Enter username: ")
password = input("Enter password: ")

valid_username = "admin"
valid_password = "Admin123"

if username == "" and password == "":
    print("Username Required")
elif username == "":
    print("Username Required")
elif password == "":
    print("Password Required")
elif username == valid_username and password == valid_password:
    print("Login Successful")
else:
    print("Invalid Credentials")

