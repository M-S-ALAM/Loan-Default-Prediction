"""
Inference of Loan Default Prediction.
===============================================
This module to predict the given customer is
defaulter based on category, amount, employed
status and many more things
"""
import pandas as pd
import numpy as np

class Loan_Default_prediction:
    """

    """
    def __init__(self, data):
        self.test_data = None
        self.data = data


    def add_feature(self):
        
        
        
    def predict(self):
        self.test_data = pd.DataFrame(self.test, index=[0])

        

def main():
    loan_amount = 0.0
    rate = 11.84
    tenure = 6
    employ_type = 'Salaried'
    tier_employ = 'B'
    experience = 1.5
    total_income = 125000.0
    gender = 'Female'
    married = 'Yes'
    dependents = 0
    home = 'rent'
    social_profile = 'No'
    no_of_loans = 0.0
    interest_reccived = 852.69
    total_payment = 1824.15
    reccived_payment = 971.46
    deling_2ys = 0.0
    is_verified = 'missing'
    value = {'Amount': loan_amount, 'Interest Rate': rate, 'Tenure(years)': tenure, 'Employmet type': employ_type,
             'Tier of Employment': tier_employ, 'Work Experience': experience, 'Total Income(PA)': total_income,
             'Gender': gender, 'Married': married, 'Dependents': dependents, 'Home': home,
             'Social Profile': social_profile, 'Number of loans': no_of_loans, 'Interest Received': interest_reccived,
             'Total Payement ': total_payment, 'Received Principal': reccived_payment, 'Delinq_2yrs': deling_2ys,
             'Is_verified': is_verified}


if __name__=='__main__':
    main()