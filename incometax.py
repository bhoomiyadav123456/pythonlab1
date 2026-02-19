def calculate_tax(income, age):
    tax = 0

    # Set exemption limit based on age
    if age >= 60:
        exemption_limit = 300000
    else:
        exemption_limit = 250000

    # No tax if income is within exemption limit
    if income <= exemption_limit:
        return 0

    # Calculate tax based on slabs
    # 5% slab
    if income > exemption_limit:
        taxable_amount = min(income, 500000) - exemption_limit
        tax += taxable_amount * 0.05

    # 20% slab
    if income > 500000:
        taxable_amount = min(income, 1000000) - 500000
        tax += taxable_amount * 0.20

    # 30% slab
    if income > 1000000:
        taxable_amount = income - 1000000
        tax += taxable_amount * 0.30

    return tax


# Taking user input
income = float(input("Enter your annual income (₹): "))
age = int(input("Enter your age: "))

tax_amount = calculate_tax(income, age)

print(f"\nTotal Tax Payable: ₹{tax_amount:,.2f} - incometax.py:39")