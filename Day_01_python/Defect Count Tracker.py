# Scenario 8: Defect Count Tracker
# Business Requirement

# Count defects.

# Given
# defects = [
#     "Critical",
#     "Major",
#     "Critical",
#     "Minor",
#     "Major",
#     "Critical"
# ]
# Output
# Critical: 3

# Major: 2

# Minor: 1
# Concepts Used
# Lists
# Count Method

defects = [
    "Critical",
    "Major",
    "Critical",
    "Minor",
    "Major",
    "Critical"
]

print(f"Critical: {defects.count('Critical')}")
print(f"Major: {defects.count('Major')}")
print(f"Minor: {defects.count('Minor')}")