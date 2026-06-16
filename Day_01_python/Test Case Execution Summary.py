# Scenario 2: Test Case Execution Summary
# Business Requirement

# QA team executed test cases and needs summary.

# Given:
# passed = 120
# failed = 15
# blocked = 5
# not_executed = 10
# Output:
# Total Test Cases: 150

# Executed: 140

# Execution Percentage: 93.33%

# Pass Percentage: 85.71%
# Challenge

# Calculate percentages dynamically.

# Concepts Used
# Variables
# Arithmetic Operators 	

passed = 120
failed = 15 
blocked = 5
not_executed = 10

total_test_cases = passed + failed + blocked + not_executed
executed = passed + failed + blocked
execution_percentage = (executed / total_test_cases) * 100
pass_percentage = (passed / executed) * 100

print(f"Total Test Cases: {total_test_cases}")
print(f"Executed: {executed}")
print(f"Execution Percentage: {execution_percentage:.2f}%")
print(f"Pass Percentage: {pass_percentage:.2f}%")
