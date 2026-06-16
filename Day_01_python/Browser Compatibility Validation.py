# Scenario 5: Browser Compatibility Validation
# Business Requirement

# Application supports:

# Chrome
# Firefox
# Edge
# Input

# User enters browser.

# Expected Output
# Browser	Result
# Chrome	Supported
# Firefox	Supported
# Edge	Supported
# Safari	Not Supported
# Concepts Used
# Lists
# Membership Operator (in)

supported_browsers = ["Chrome", "Firefox", "Edge"]
browser = input("Enter browser: ").lower()
if browser in supported_browsers:
    print("Browser is supported")
else:
    print("Browser is not supported")
