def calculate_tax_refund(income, withholdings, deductions, credits):
    """
    Calculate whether the user gets a refund or owes taxes.
    
    :param income: Annual income of the user.
    :param withholdings: Amount of taxes withheld from paychecks.
    :param deductions: Total deductions the user can claim.
    :param credits: Total tax credits the user can claim.
    :return: A string stating either the refund amount or taxes owed.
    """
    # Simple tax calculation with a 22% tax rate for this example
    tax_owed = income * 0.22
    total_deductions = deductions + credits
    net_tax = tax_owed - withholdings - total_deductions

    if net_tax > 0:
        return f"You owe ${net_tax:.2f} in taxes."
    else:
        return f"You will receive a tax refund of ${abs(net_tax):.2f}."
