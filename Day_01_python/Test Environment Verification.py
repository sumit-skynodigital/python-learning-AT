# Scenario 7: Test Environment Verification
# Business Requirement

# Different URLs for environments.

# Data
# environment = "UAT"
# Expected
# Environment	URL
# DEV	dev.company.com
# QA	qa.company.com
# UAT	uat.company.com
# PROD	company.com
# Challenge

# Display correct URL.

# Concepts Used
# Variables
# If Else

environment = input("Enter environment (DEV, QA, UAT, PROD): ").upper()
if environment == "DEV":
    print("URL: dev.company.com")
elif environment == "QA":
    print("URL: qa.company.com")
elif environment == "UAT":
    print("URL: uat.company.com")
elif environment == "PROD":
    print("URL: company.com")
else:
    print("Invalid environment")
    
