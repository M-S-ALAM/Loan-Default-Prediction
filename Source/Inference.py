"""
Inference of Loan Default Prediction.
===============================================
This module to predict the given customer is
defaulter based on category, amount, employed
status and many more things
"""
import pandas as pd
import re
import pickle
import numpy as np


class Loan_Default_prediction:
    """

    """

    def __init__(self, data):
        self.test_data = None
        self.data = data

    def preprocessing(self):
        numbers = re.compile(r"[-+]?(\d*\.\d+|\d+)")
        self.test_data['Work Experience'] = self.test_data['Work Experience'].apply(
            lambda x: self.avg_property_area(str(x)))
        data = self.add_feature()
        return data

    def avg_property_area(self, x):
        numbers = re.compile(r"[-+]?(\d*\.\d+|\d+)")
        x = numbers.findall(x)
        if len(x) == 1:
            return np.float16(x[0])
        elif len(x) == 2:
            return (np.float16(x[0]) + np.float16(x[1])) / 2
        else:
            return 0

    def add_feature(self):
        fileName = '/home/shobot/Desktop/Project/Loan Default Prediction/model/loan_category_map.pkl'
        with open(fileName, 'rb') as file:
            loan_category = pickle.load(file)
        self.test_data['Defaulter by Loan Category'] = self.test_data['Loan Category'].map(loan_category)
        fileName = '/home/shobot/Desktop/Project/Loan Default Prediction/model/employmet_type_map.pkl'
        with open(fileName, 'rb') as file:
            employment_map = pickle.load(file)
        self.test_data['Defaulter by Employmet type'] = self.test_data['Employmet type'].map(employment_map)
        fileName = '/home/shobot/Desktop/Project/Loan Default Prediction/model/home_map.pkl'
        with open(fileName, 'rb') as file:
            home_map = pickle.load(file)
        self.test_data['Defaulter by Home'] = self.test_data['Home'].map(home_map)
        fileName = '/home/shobot/Desktop/Project/Loan Default Prediction/model/Is_verified_map.pkl'
        with open(fileName, 'rb') as file:
            verified_map = pickle.load(file)
        self.test_data['Defaulter by Is_verified'] = self.test_data['Is_verified'].map(verified_map)
        self.test_data.drop(
            ['Loan Category', 'Employmet type', 'Tier of Employment', 'Gender', 'Married', 'Home', 'Social Profile',
             'Is_verified'], axis=1, inplace=True)
        return self.test_data

    def predict(self):
        self.test_data = pd.DataFrame(self.data, index=[0])
        x_test = self.preprocessing()
        filename = '/home/shobot/Desktop/Project/Loan Default Prediction/model/features.pkl'
        with open(filename, 'rb') as file:
            featuresMod = pickle.load(file)
        featuresMod = list(featuresMod)
        featuresMod.remove('Defaulter')
        x_test.columns = featuresMod
        fileName = '/home/shobot/Desktop/Project/Loan Default Prediction/model/classification_model.pkl'
        with open(fileName, 'rb') as file:
            model = pickle.load(file)
        prediction = model.predict(x_test)
        if prediction[0]:
            text = 'This is a defaulter id'
        else:
            text = 'This is not a defaulter id'
        return text


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
    loan_category = 'Consolidation'
    value = {'Loan Category': loan_category, 'Amount': loan_amount, 'Interest Rate': rate, 'Tenure(years)': tenure,
             'Employmet type': employ_type,
             'Tier of Employment': tier_employ, 'Work Experience': experience, 'Total Income(PA)': total_income,
             'Gender': gender, 'Married': married, 'Dependents': dependents, 'Home': home,
             'Social Profile': social_profile, 'Number of loans': no_of_loans, 'Interest Received': interest_reccived,
             'Total Payement ': total_payment, 'Received Principal': reccived_payment, 'Delinq_2yrs': deling_2ys,
             'Is_verified': is_verified}
    loan = Loan_Default_prediction(value)
    text = loan.predict()
    print(text)


if __name__ == '__main__':
    main()
