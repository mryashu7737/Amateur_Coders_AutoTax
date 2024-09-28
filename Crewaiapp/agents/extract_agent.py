class ExtractAgent:
    def __init__(self):
        pass

    def ask_user_for_input(self):
        # Simulate user data collection (could be expanded for dynamic input)
        user_data = {}
        user_data['PAN'] = input("Enter your PAN: ")
        user_data['First Name'] = input("Enter your First Name: ")
        user_data['Middle Name'] = input("Enter your Middle Name: ")
        user_data['Last Name'] = input("Enter your Last Name: ")
        user_data['Date of Birth'] = input("Enter your Date of Birth (DD/MM/YYYY): ")
        user_data['Aadhaar Number'] = input("Enter your Aadhaar Number: ")
        user_data['Mobile Number'] = input("Enter your Mobile Number: ")
        user_data['Email Address'] = input("Enter your Email Address: ")

        return user_data
