import streamlit as st
from fileload import read
import pandas as pd
import time  # to simulate a real time data, time loop

import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development

name = "Credit Card Customers EDA Dashboard"

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



st.markdown("Histogram: Distribution of Customer Age")
fig = px.histogram(df, x='Customer_Age')
st.write(fig)

# dataframe filter
df2 = get_data()
edu = df2.groupby('Attrition_Flag', as_index=False)['Education_Level'].value_counts(normalize=True).reset_index()

#create two columns for charts

gender_df = df2.groupby('Attrition_Flag', as_index=False)['Gender'].value_counts().reset_index()
st.markdown("Bar chart: Number of customers by gender and customer status")
fig = px.bar(gender_df, x='Gender', y='count', color='Attrition_Flag', barmode='group')
st.write(fig)


st.markdown("Bar chart: Proportion of customers by education level and Customer Status")
fig = px.bar(edu, x='Education_Level', y='proportion', color='Attrition_Flag', barmode='group')
st.write(fig)

marrige = df2.groupby('Attrition_Flag', as_index=False)['Marital_Status'].value_counts(normalize=True).reset_index()
st.markdown("Bar chart: Proportion of customers by Marital Status and Customer Status")
fig = px.bar(marrige, x='Marital_Status', y='proportion', color='Attrition_Flag', barmode='group')
st.write(fig)

income_df = df2.groupby('Attrition_Flag', as_index=False)['Income_Category'].value_counts().reset_index()
st.markdown("Bar chart: Income Category by Customer Status")
fig = px.bar(income_df, x='Income_Category', y='count', color='Attrition_Flag', barmode='group')
st.write(fig)

card = df2.groupby('Attrition_Flag', as_index=False)['Card_Category'].value_counts(normalize=True).reset_index()
st.markdown("Bar chart: Proportion of customers by Card Category and Customer Status")
fig = px.bar(card, x='Card_Category', y='proportion', color='Attrition_Flag', barmode='group')
st.write(fig)



#calculate the aveage credit limit by attrition flag
credit = df2.groupby('Attrition_Flag')['Credit_Limit'].mean().reset_index()
status = credit['Attrition_Flag']
value = credit['Credit_Limit']
# create two columns for charts
fig_col1, fig_col2 = st.columns(2)

with fig_col1:
    st.markdown("Bar chart of Average Credit Limit by Customer Status")
    fig1 = px.bar(x=status, y = value, text = round(value,2), width=300, height=400)
    st.write(fig1)

trans_df = df2.groupby('Attrition_Flag')['Total_Trans_Amt'].mean().reset_index()
status = trans_df['Attrition_Flag']
value = trans_df['Total_Trans_Amt']

with fig_col2:
    st.markdown("Bar chart of Average Transaction Amount by Customer Status")
    fig2= px.bar(x=status, y = value, text = round(value,2), width=300, height=400)
    st.write(fig2)

trans_ct = df2.groupby('Attrition_Flag')['Total_Trans_Ct'].mean().reset_index()
status = trans_ct['Attrition_Flag']
value = trans_ct['Total_Trans_Ct']
# create two columns for charts
fig_col1, fig_col2 = st.columns(2)

with fig_col1:
    st.markdown("Bar chart of Average Number of Transactions by Customer Status")
    fig1 = px.bar(x=status, y = value, text = round(value,2), width=300, height=400)
    st.write(fig1)

change = df2.groupby('Attrition_Flag')['Total_Ct_Chng_Q4_Q1'].mean().reset_index()
status = change['Attrition_Flag']
value = change['Total_Ct_Chng_Q4_Q1']

with fig_col2:
    st.markdown("Bar chart of Average Difference in Transaction Amount betwwen Q1 & Q4")
    fig2= px.bar(x=status, y = value, text = round(value,2), width=300, height=400)
    st.write(fig2)

inactive = df2.groupby('Attrition_Flag')['Months_Inactive_12_mon'].mean().reset_index()
status = inactive['Attrition_Flag']
value = inactive['Months_Inactive_12_mon']
# create two columns for charts
fig_col1, fig_col2 = st.columns(2)

with fig_col1:
    st.markdown("Bar chart of Average number of months the customer is inactive by customer status")
    fig1 = px.bar(x=status, y = value, text = round(value,2), width=300, height=400)
    st.write(fig1)

num_pro = df2.groupby('Attrition_Flag')['Total_Relationship_Count'].mean().reset_index()
status = num_pro['Attrition_Flag']
value = num_pro['Total_Relationship_Count']

with fig_col2:
    st.markdown("Bar chart of Average number of products the customer is holding by Customer status")
    fig2= px.bar(x=status, y = value, text = round(value,2), width=300, height=400)
    st.write(fig2)

length = df2.groupby('Attrition_Flag')['Months_on_book'].mean().reset_index()
status = length['Attrition_Flag']
value = length['Months_on_book']
# create two columns for charts
fig_col1, fig_col2 = st.columns(2)

with fig_col1:
    st.markdown("Bar chart of Average Length of the Relationship with Bank")
    fig1 = px.bar(x=status, y = value, text = round(value,2), width=300, height=400)
    st.write(fig1)

with fig_col2:
    st.markdown("Boxplot of Difference in Transaction Amount betwwen Q1 & Q4")
    fig2= px.box(df2, x='Attrition_Flag', y = 'Total_Ct_Chng_Q4_Q1', width=300, height=400)
    st.write(fig2)

# create two columns for charts
fig_col1, fig_col2 = st.columns(2)

with fig_col1:
    st.markdown("Box Plot of card utilization ratio")
    fig1= px.box(df2, x='Attrition_Flag', y = 'Avg_Utilization_Ratio', width=300, height=400)
    st.write(fig1)

with fig_col2:
    st.markdown("Box Plot of Total Credit Card Revolving Balance")
    fig2= px.box(df2, x='Attrition_Flag', y = 'Total_Revolving_Bal', width=300, height=400)
    st.write(fig2)

st.markdown("Scatter Plot: Total_Revolving_Bal and Total_Trans_Amt Colored by Customer Status")
fig = px.scatter(df2, x='Total_Revolving_Bal', y='Total_Trans_Amt', color='Attrition_Flag')
st.write(fig)

st.markdown("Scatter Plot: Total_Ct_Chng & Total_Relationship_Count Colored by Customer Status")
fig = px.scatter(df2, x='Total_Ct_Chng_Q4_Q1', y='Total_Relationship_Count', color='Attrition_Flag')
st.write(fig)

st.markdown("Scatter Plot: Dependent_count & Months_on_book Colored by Customer Status")
fig = px.scatter(df2, x='Dependent_count', y='Months_on_book', color='Attrition_Flag')
st.write(fig)

df_cleaned = df.drop(['CLIENTNUM','Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1', 'Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2'], axis=1)
numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
newdf = df_cleaned.select_dtypes(include=numerics)
st.markdown("Scatter Plot: Dependent_count & Months_on_book Colored by Customer Status")
fig = px.imshow(round(newdf.corr(),1), text_auto=True, width=700, height=700)
st.write(fig)
