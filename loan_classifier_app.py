import streamlit as st
import pandas as pd
import pickle
import toml

loan_classifier = pickle.load(open(r'C:\Users\kylel\Desktop\Loan classifier\RFC_Loan_Classifer.pkl', 'rb'))

st.write("""
# Loan Classification Model
This is a Credit Score Classification Model.
""")

st.divider()

st.sidebar.header('Welcome!')
st.sidebar.markdown('_Please fill up the following information:_')

def user_input_features():
    annual_income = st.sidebar.text_input('Annual Income:',0)
    monthly = st.sidebar.text_input('Monthly in-hand Salary:',0)
    bank_acct_count = st.sidebar.text_input('Number of Bank Accounts:',0)
    cc_count = st.sidebar.text_input('Number of Credit Cards:',0)
    interest_rate = st.sidebar.text_input('Interest Rate(%):',0)
    num_loans = st.sidebar.text_input('Number of Active Loans:',0)
    delay_dd = st.sidebar.text_input('Number of days payment was delayed from due date:',0)
    delayed_payment = st.sidebar.text_input('Number of delayed payments:',0)
    credit_mix = st.sidebar.selectbox('Select Credit Mix:', ['Standard','Good','Bad'])
    outstanding_debt = st.sidebar.text_input('Outstanding debt amount:',0)
    credit_hist_age = st.sidebar.text_input('Credit history age (days):',0)
    monthly_balance = st.sidebar.text_input('Monthly bank balance amount:',0)
    
    if credit_mix == 'Standard':
        credit_mix =1
    elif credit_mix == 'Good':
        credit_mix = 2
    else:
        credit_mix = 0
    
    data = {'Annual_Income': annual_income,
            'Monthly_Inhand_Salary': monthly,
            'Num_Bank_Accounts': bank_acct_count,
            'Num_Credit_Card': cc_count,
            'Interest_Rate': interest_rate,
            'Num_of_Loan': num_loans,
           'Delay_from_due_date': delay_dd,
           'Num_of_Delayed_Payment': delayed_payment,
           'Credit_Mix': credit_mix,
           'Outstanding_Debt': outstanding_debt,
           'Credit_History_Age': credit_hist_age,
           'Monthly_Balance': monthly_balance}
    
    
    features = pd.DataFrame(data, index=[0])
    return features
                      
df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

if st.sidebar.button("Predict Credit Score"):
    prediction = loan_classifier.predict(df)
    
    st.divider()
    st.subheader("Prediction")
    if prediction == 'Standard':
        st.write('Credit Score: Standard')
    elif prediction == 'Good':
        st.write('Credit Score: Good')
    else:
        st.write('Credit Score: Bad')
    
    #st.subheader("Prediction")   
    #st.write('Credit Score: ' .join(str(prediction)))

