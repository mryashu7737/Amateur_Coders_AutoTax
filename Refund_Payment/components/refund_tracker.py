import requests

def check_refund_status(ssn, filing_status, refund_amount):
    """
    Mock function to simulate checking refund status.
    
    In a real application, this would call the IRS API or another service.
    
    :param ssn: Social Security Number.
    :param filing_status: Filing status (e.g., Single, Married, Head of Household).
    :param refund_amount: Expected refund amount.
    :return: A string with the refund status.
    """
    # Mock response (replace this with an actual API call later)
    return f"Refund Status: Approved - Expected Disbursement: 2 weeks."
