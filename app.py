import streamlit as st

st.title('Loan Default Prediction')

col1, col2, col3 = st.columns(3)

with col1:
    loan_category = st.selectbox('Loan Category',
                                 options=['Consolidation', 'Credit Card', 'Home', 'Other ', 'Business', 'Car ',
                                          'Medical '])
    loan_amount = st.number_input('Loan Amount', min_value=0., max_value=10000000.)
    rate = st.number_input('Interest rate', min_value=5.00, max_value=25.0, format="%.2f")
    tenure = st.number_input('Tenure', min_value=1, max_value=5)
    employ_type = st.selectbox('Employment type', options=['Salaried', 'Self - Employeed', 'Missing'])
    tier_employ = st.selectbox('Tier of Employment', options=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'Missing'])

with col2:
    experience = st.number_input('work Experience', min_value=0, max_value=20)
    total_income = st.number_input('Total annual income', min_value=4000, max_value=8000000)
    gender = st.selectbox('Gender', options=['Female', 'Other', 'Male'])
    married = st.selectbox('Marital status', options=['Yes', 'No', 'Missing'])
    dependents = st.number_input('Dependents', min_value=0, max_value=5)
    home = st.selectbox('Home', options=['rent', 'mortgage', 'own', 'none', 'other'])

with col3:
    social_profile = st.selectbox('Social Profile', options=['No', 'missing', 'Yes'])
    no_of_loans = st.number_input('No. of Loans', min_value=0, max_value=10)
    interest_reccived = st.number_input('Interest Received', min_value=0., max_value=25000.00, format="%.2f")
    total_payment = st.number_input('Total Payment', min_value=0.0, max_value=60000.00, format="%.2f")
    reccived_payment = st.number_input('Received payment', min_value=0., max_value=25000.00, format="%.2f")
    deling_2ys = st.number_input('Number of delinquencies', min_value=0, max_value=20)

is_verified = st.selectbox('Is verified', options=['missing', 'Source Verified', 'Verified', 'Not Verified'])

value = {'Amount': loan_amount, 'Interest Rate': rate, 'Tenure(years)': tenure, 'Employmet type': employ_type, 'Tier of Employment': tier_employ, 'Work Experience': experience, 'Total Income(PA)': total_income, 'Gender': gender, 'Married': married, 'Dependents': dependents, 'Home': home, 'Social Profile': social_profile, 'Number of loans': no_of_loans, 'Interest Received': interest_reccived, 'Total Payement ': total_payment,'Received Principal': reccived_payment, 'Delinq_2yrs': deling_2ys, 'Is_verified': is_verified}
submit_button = st.button(label='Prediction', type='primary')
if submit_button:
    st.write(value)
def main():
    pass


if __name__ == '__main__':
    main()
