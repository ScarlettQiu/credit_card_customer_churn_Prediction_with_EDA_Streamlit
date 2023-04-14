import streamlit as st
from fileload import read, clean
import pandas as pd
import time  # to simulate a real time data, time loop

import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development

name = "Credit Card Customers EDA Dashboard"

st.header(name)
st.markdown('''
---
👩‍🚀Created by [Yu Qiu](https://www.linkedin.com/in/yuqiuscarlettvelvet/).
''')


dataset_url = "https://raw.githubusercontent.com/ScarlettQiu/credit_card_customer_churn_prediction/af46862bff782f1008725fa49db88d1e36fc8d43/BankChurners.csv"

@st.experimental_memo
def get_data() -> pd.DataFrame:
    return read(dataset_url)

df = get_data()

with st.sidebar:
    st.write("Average Figures of Credit Card Customers")
    job_filter = st.selectbox("Select Customer Status", pd.unique(df["Attrition_Flag"]))

# top-level filters
#job_filter = st.selectbox("Select Customer Status", pd.unique(df["Attrition_Flag"]))

# dataframe filter
    df = df[df["Attrition_Flag"] == job_filter]

    avg_age = df['Customer_Age'].mean()
    avg_dep = df['Dependent_count'].mean()
    count_married = df['Marital_Status'][df['Marital_Status'] == 'Married'].count()
    count = df['Marital_Status'].count()
    percent_married = round(count_married/count,2)

    avg_trans = df['Total_Trans_Ct'].mean()
    avg_Amt = df['Total_Trans_Amt'].mean()
    avg_amt_ch = df['Total_Amt_Chng_Q4_Q1'].mean()
    avg_ct_ch = df['Total_Ct_Chng_Q4_Q1'].mean()
    avg_relation = df['Months_on_book'].mean()
    num_prod = df['Total_Relationship_Count'].mean()
    mon_inactive = df['Months_Inactive_12_mon'].mean()
    contact_mon = df['Contacts_Count_12_mon'].mean()
    credit_lim = df['Credit_Limit'].mean()
    revolving = df['Total_Revolving_Bal'].mean()
    open_to_buy = df['Avg_Open_To_Buy'].mean()
    utilization_ratio = df['Avg_Utilization_Ratio'].mean()
    count_platinum = df['Card_Category'][df['Card_Category'] == 'Platinum'].count()
    count_card = df['Card_Category'].count()
    percent_card = round(count_platinum / count_card, 4)

#print(percent_married)
#create 3 columns
    kpi1, kpi2 = st.columns(2)

#fill in those three columns with respective metrics or KPIs
    kpi1.metric(
        label = 'Average Age',
        value = round(avg_age)
    )

    kpi2.metric(
        label = 'Num of Dependents',
        value = round(avg_dep)
    )

    kpi3, kpi4 = st.columns(2)

    # fill in those three columns with respective metrics or KPIs
    kpi4.metric(
        label='Num of Transactions (12-Mon)',
        value=round(avg_trans)
    )

    kpi3.metric(
        label = 'Married Percentage',
        value=percent_married
    )

    kpi5, kpi6 = st.columns(2)

    # fill in those three columns with respective metrics or KPIs
    kpi5.metric(
        label='Transactions Amount (12-Mon)',
        value=round(avg_Amt, 1)
    )

    kpi6.metric(
        label = 'Length of Relationship',
        value=round(avg_relation, 1)
    )

    kpi7, kpi8 = st.columns(2)

    # fill in those three columns with respective metrics or KPIs
    kpi5.metric(
        label='Num of Contacts',
        value=round(contact_mon)
    )

    kpi6.metric(
        label = 'Platinum Card Ratio',
        value= percent_card
    )

    kpi9, kpi10 = st.columns(2)

    # fill in those three columns with respective metrics or KPIs
    kpi9.metric(
        label='Num of Products Holding',
        value=round(num_prod)
    )

    kpi10.metric(
        label = 'Num of Months Inactive',
        value=round(mon_inactive, 1)
    )

    kpi11, kpi12 = st.columns(2)
    # fill in those three columns with respective metrics or KPIs
    kpi11.metric(
        label='Credit Card Credit Limit',
        value=round(credit_lim, 1)
    )

    kpi12.metric(
        label = 'Revolving Balance',
        value=round(revolving, 1)
    )

    kpi13, kpi14 = st.columns(2)
    # fill in those three columns with respective metrics or KPIs
    kpi13.metric(
        label='Open to Buy Credit Line',
        value=round(open_to_buy,1)
    )

    kpi14.metric(
        label = 'Card Utilization Ratio',
        value=round(utilization_ratio,2)
    )
# dataframe filter
df2 = get_data()
edu = df2.groupby('Attrition_Flag', as_index=False)['Education_Level'].value_counts(normalize=True).reset_index()

st.markdown("Histogram: Distribution of Customer Age")
fig = px.histogram(df2, x='Customer_Age')
st.write(fig)

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



# create two columns for charts
fig_col1, fig_col2 = st.columns(2)

with fig_col1:
    st.markdown("Boxplot of Credit Card Limit")
    fig1 = px.box(df2, x='Attrition_Flag', y = 'Credit_Limit', width=300, height=400)
    st.write(fig1)

with fig_col2:
    st.markdown("Boxplot of Transaction Amount in Last 12 Months")
    fig2= px.box(df2, x='Attrition_Flag', y = 'Total_Trans_Amt', width=300, height=400)
    st.write(fig2)    

# create two columns for charts
fig_col1, fig_col2 = st.columns(2)

with fig_col1:
    st.markdown("Boxplot of Average Number of Transactions")
    fig1 = px.box(df2, x='Attrition_Flag', y = 'Total_Trans_Ct', width=300, height=400)
    st.write(fig1)

with fig_col2:
    st.markdown("Boxplot of Average Difference in Transaction Amount betwwen Q1 & Q4")
    fig2= px.box(df2, x='Attrition_Flag', y = 'Total_Ct_Chng_Q4_Q1', width=300, height=400)
    st.write(fig2)


# create two columns for charts
fig_col1, fig_col2 = st.columns(2)

with fig_col1:
    st.markdown("Boxplot of Length of Relationship")
    fig1 = px.box(df2, x='Attrition_Flag', y = 'Months_on_book', width=300, height=400)
    st.write(fig1)

with fig_col2:
    st.markdown("Boxplot of Length being Inactive in Last 12 Months")
    fig2= px.box(df2, x='Attrition_Flag', y = 'Months_Inactive_12_mon', width=300, height=400)
    st.write(fig2)

# create two columns for charts
fig_col1, fig_col2 = st.columns(2)

with fig_col1:
    st.markdown("Boxplot of Total Number of Products Customers Holding")
    fig1 = px.box(df2, x='Attrition_Flag', y = 'Total_Relationship_Count', width=300, height=400)
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

st.markdown("Scatter Plot: Total_Revolving_Bal vs Total_Trans_Amt Colored by Customer Status")
fig = px.scatter(df2, x='Total_Revolving_Bal', y='Total_Trans_Amt', color='Attrition_Flag')
st.write(fig)

st.markdown("Scatter Plot: Total_Ct_Chng vs Total_Relationship_Count Colored by Customer Status")
fig = px.scatter(df2, x='Total_Ct_Chng_Q4_Q1', y='Total_Relationship_Count', color='Attrition_Flag')
st.write(fig)

st.markdown("Scatter Plot: Dependent_count vs Months_on_book Colored by Customer Status")
fig = px.scatter(df2, x='Dependent_count', y='Months_on_book', color='Attrition_Flag')
st.write(fig)

#df_cleaned = df.drop(['CLIENTNUM','Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1', 'Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2'], axis=1)
df_cleaned = clean(df2)
numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
newdf = df_cleaned.select_dtypes(include=numerics)
st.markdown("Correlation Heatmap")
fig = px.imshow(round(newdf.corr(),1), text_auto=True, width=700, height=700)
st.write(fig)
