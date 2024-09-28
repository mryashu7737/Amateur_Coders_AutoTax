from tools.filler import FormFiller

class FillAgent:
    def __init__(self, form_path, user_data):
        self.form_filler = FormFiller(form_path)
        self.user_data = user_data

    def fill_form(self):
        # Fill the ITR form with the user data
        filled_form_path = self.form_filler.fill_form_with_data(self.user_data)
        return filled_form_path
