import streamlit as st
from fileload import read
import pandas as pd
import time  # to simulate a real time data, time loop

import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development

name = "Credit Card Customers App"

st.text(name)



dataset_url = "https://raw.githubusercontent.com/ScarlettQiu/credit_card_customer_churn_prediction/af46862bff782f1008725fa49db88d1e36fc8d43/BankChurners.csv"

@st.experimental_memo
def get_data() -> pd.DataFrame:
    return read(dataset_url)

df = get_data()

# top-level filters
job_filter = st.selectbox("Select Customer Status", pd.unique(df["Attrition_Flag"]))

# dataframe filter
df = df[df["Attrition_Flag"] == job_filter]

avg_age = df['Customer_Age'].mean()
avg_dep = df['Dependent_count'].mean()
count_married = df['Marital_Status'][df['Marital_Status'] == 'Married'].count()
#create 3 columns
kpi1, kpi2, kpi3 = st.columns(3)

#fill in those three columns with respective metrics or KPIs
kpi1.metric(
    label = 'Age',
    value = round(avg_age)
)

kpi2.metric(
    label = 'Dependent_count',
    value = round(avg_dep)
)

kpi3.metric(
    label = 'Married Count',
    value=int(count_married)
)



edu = df.groupby('Attrition_Flag', as_index=False)['Education_Level'].value_counts(normalize=True).reset_index()

#create two columns for charts


st.markdown("Bar chart: Proportion of customers by education level and Customer Status")
fig = px.bar(edu, x='Education_Level', y='proportion')
st.write(fig)


st.markdown("Histogram: Distribution of Customer Age")
fig = px.histogram(df, x='Customer_Age')
st.write(fig)
