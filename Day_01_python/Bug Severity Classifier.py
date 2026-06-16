# Scenario 3: Bug Severity Classifier
# Business Requirement

# Defects should be categorized.

# Input
# severity = input()
# Rules
# Severity	Action
# Critical	Stop Release
# High	Fix Immediately
# Medium	Schedule in Sprint
# Low	Defer
# Invalid Input	Ask User Again
# Example

# Input:

# Critical

# Output:

# Release Blocked
# Concepts Used
# If
# Elif
# Else

#Solution 1:
# severity = input("Enter bug severity (Critical, High, Medium, Low): ").lower()
# if severity == "critical":
#     print("Stop Release")
# elif severity == "high":
#     print("Fix Immediately")
# elif severity == "medium":
#     print("Schedule in Sprint")
# elif severity == "low":
#     print("Defer")
# else:
#     print("Invalid Input")


#Solution 2:
severity_action={
    "critical": "Stop Release", 
    "high": "Fix Immediately", 
    "medium": "Schedule in Sprint", 
    "low": "Defer"
}

severity = input("Enter bug severity (Critical, High, Medium, Low): ").lower()  
print(severity_action.get(severity, "Invalid Input"))

