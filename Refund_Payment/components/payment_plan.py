def calculate_payment_plan(amount_owed, months):
    """
    Calculate monthly payment for the given number of months.
    
    :param amount_owed: Total tax amount owed.
    :param months: Number of months over which the user wants to pay.
    :return: A string with the monthly payment plan details.
    """
    if months == 0:
        return "Cannot divide by zero months."
    monthly_payment = amount_owed / months
    return f"Your monthly payment over {months} months will be ${monthly_payment:.2f}."
