# Scenario 6: API Status Code Validation
# Business Requirement

# Validate API responses.

# Rules
# Status Code	Meaning
# 200	Success
# 201	Created
# 400	Bad Request
# 401	Unauthorized
# 404	Not Found
# 500	Server Error
# Task

# Take status code input.

# Display appropriate message.

# Concepts Used
# If Else

status_code = int(input("Enter API status code: "))
if status_code == 200:
    print("Success")    
elif status_code == 201:
    print("Created")
elif status_code == 400:
    print("Bad Request")
elif status_code == 401:
    print("Unauthorized")
elif status_code == 404:
    print("Not Found")
elif status_code == 500:
    print("Server Error")
else:
    print("Invalid Status Code") 