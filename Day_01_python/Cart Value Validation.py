# Scenario 10: Cart Value Validation
# Business Requirement

# Free shipping above:

# ₹500
# Test Cases
# Cart Value	Expected
# 499	Shipping Charges Apply
# 500	Free Shipping
# 501	Free Shipping
# Concepts Used
# Boundary Testing
# Comparison Operators

cart_value = float(input("Enter cart value: "))
if cart_value >= 500:
    print("Free Shipping")
else:
    print("Shipping Charges Apply")
