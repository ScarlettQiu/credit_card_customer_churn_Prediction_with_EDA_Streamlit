from fileload import read, clean
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = read('https://raw.githubusercontent.com/ScarlettQiu/credit_card_customer_churn_prediction/af46862bff782f1008725fa49db88d1e36fc8d43/BankChurners.csv')
df_cleaned = clean(df)
#count the number of customers by customer status
cus_status = df_cleaned['Attrition_Flag'].value_counts().reset_index()
cus_status.columns = ['status', 'num_of_cust']

#define the 2 varables for ploting
status = cus_status['status']
num_of_cust = cus_status['num_of_cust']

#set the size of the plot
fig, ax = plt.subplots(figsize=(8,6))

# Create bar chart
bar_container = plt.bar(status, num_of_cust, color=['green', 'orange'])

plt.xlabel("Customer Status")
plt.ylabel("Number of Customers")
plt.title("Bar chart of Number of Customers by Customer Status")
plt.bar_label(bar_container)
plt.show()

#calculate the customer churn rate
percent_cust = df_cleaned.Attrition_Flag.value_counts(normalize=True).mul(100).round(2).astype(str) + '%'
print('The customer churn rate of this bank currently is', percent_cust[1])

#plot the histogram of customer age
fig, ax = plt.subplots(figsize=(8,6))
ax.hist(df_cleaned['Customer_Age'])
ax.set_title('Distribution of Customer Age')
ax.set_xlabel('customer age')
ax.set_ylabel('Frequency')

#bar chart of number of dependent of customers
fig, ax = plt.subplots(figsize=(8,6))
ax.bar(df_cleaned['Dependent_count'].value_counts().index, df_cleaned['Dependent_count'].value_counts().values)
ax.set_title('Number of customers by Dependen Count')
ax.set_xlabel('Dependent Count')
ax.set_ylabel('Count of Customers')

#plot the box plot of Total Credit Card Revolving Balance
fig, ax = plt.subplots(figsize=(8,6))
sns.boxplot(x=df_cleaned['Attrition_Flag'], y=df_cleaned['Total_Revolving_Bal'], showmeans=True)
plt.xlabel("Customer Status")
plt.ylabel("Total Revolving Balance")
plt.title("Box Plot of Total Credit Card Revolving Balance")
plt.show()

#plot the boxplot of card utimization ratio
fig, ax = plt.subplots(figsize=(8,6))
sns.boxplot(x=df_cleaned['Attrition_Flag'], y=df_cleaned['Avg_Utilization_Ratio'], showmeans=True)
plt.xlabel("Customer Status")
plt.ylabel("Avg_Utilization_Ratio")
plt.title("Box Plot of card utilization ratio")
plt.show()

#plot bar chart of Proportion of customers by education level and Customer Status
edu = df_cleaned.groupby('Attrition_Flag', as_index=False)['Education_Level'].value_counts(normalize=True).reset_index()

fig, ax = plt.subplots(figsize=(8,6))
# plot with seaborn barplot
sns.barplot(data=edu, x='Education_Level', y='proportion', hue='Attrition_Flag')

plt.xlabel("Education Level")
plt.ylabel("Proportion")
plt.title("Bar chart of Proportion of customers by education level and Customer Status")
plt.bar_label(bar_container)
plt.show()


#plot the bar chart of Proportion of customers by Card Category and Customer Status

card = df_cleaned.groupby('Attrition_Flag', as_index=False)['Card_Category'].value_counts(normalize=True).reset_index()

fig, ax = plt.subplots(figsize=(8,6))
# plot with seaborn barplot
sns.barplot(data=card, x='Card_Category', y='proportion', hue='Attrition_Flag')

plt.xlabel("Card Category")
plt.ylabel("Proportion")
plt.title("Bar chart of Proportion of customers by Card Category and Customer Status")
plt.bar_label(bar_container)
plt.show()

#plot the bar chart of Proportion of customers by Marital Status and Customer Status

marrige = df_cleaned.groupby('Attrition_Flag', as_index=False)['Marital_Status'].value_counts(normalize=True).reset_index()
fig, ax = plt.subplots(figsize=(8,6))
# plot with seaborn barplot
sns.barplot(data=marrige, x='Marital_Status', y='proportion', hue='Attrition_Flag')

plt.xlabel("Marital Status")
plt.ylabel("Proportion")
plt.title("Bar chart of Proportion of customers by Marital Status and Customer Status")
plt.bar_label(bar_container)
plt.show()


#bar chart of Number of customers by gender and customer status
gender_df = df_cleaned.groupby('Attrition_Flag', as_index=False)['Gender'].value_counts().reset_index()
fig, ax = plt.subplots(figsize=(8,6))
# plot with seaborn barplot
sns.barplot(data=gender_df, x='Gender', y='count', hue='Attrition_Flag')

plt.xlabel("Gender")
plt.ylabel("Number of Customers")
plt.title("Bar chart of Number of customers by gender and customer status")
plt.show()


#Bar chart of Income Category by Customer Status
income_df = df_cleaned.groupby('Attrition_Flag', as_index=False)['Income_Category'].value_counts().reset_index()
fig, ax = plt.subplots(figsize=(8,6))
# plot with seaborn barplot
sns.barplot(data=income_df, x='Income_Category', y='count', hue='Attrition_Flag')

plt.xlabel("Income Category")
plt.ylabel("Number of customers")
plt.title("Bar chart of Income Category by Customer Status")
plt.show()

# calculate the aveage credit limit by attrition flag
credit = df_cleaned.groupby('Attrition_Flag')['Credit_Limit'].mean().reset_index()

status = credit['Attrition_Flag']
value = credit['Credit_Limit']

# set the size of the plot
fig, ax = plt.subplots(figsize=(8, 6))

# Create bars with different colors
bar_container = plt.bar(status, value, color=['green', 'orange'])

plt.xlabel("Customer Status")
plt.ylabel("Average Credit Limit")
plt.title("Bar chart of Average Credit Limit by Customer Status")
plt.bar_label(bar_container)
plt.show()


#calculate the aveage Total_Trans_Amt by attrition flag

trans_df = df_cleaned.groupby('Attrition_Flag')['Total_Trans_Amt'].mean().reset_index()

status = trans_df['Attrition_Flag']
value = trans_df['Total_Trans_Amt']


#set the size of the plot
fig, ax = plt.subplots(figsize=(8,6))

# Create bars with different colors
bar_container = plt.bar(status, value, color=['green', 'orange'])

plt.xlabel("Customer Status")
plt.ylabel("Average Transaction Amount")
plt.title("Bar chart of Average Transaction Amount by Customer Status")
plt.bar_label(bar_container)
plt.show()


#calculate the aveage Total_Trans_Ct by attrition flag
trans_ct = df_cleaned.groupby('Attrition_Flag')['Total_Trans_Ct'].mean().reset_index()

status = trans_ct['Attrition_Flag']
value = trans_ct['Total_Trans_Ct']


#set the size of the plot
fig, ax = plt.subplots(figsize=(8,6))

# Create bars with different colors
bar_container = plt.bar(status, value, color=['green', 'orange'])

plt.xlabel("Customer Status")
plt.ylabel("Average Number of Transactions")
plt.title("Bar chart of Average Number of Transactions by Customer Status")
plt.bar_label(bar_container)
plt.show()



#calculate the aveage Total_Ct_Chng_Q4_Q1 by attrition flag
change = df_cleaned.groupby('Attrition_Flag')['Total_Ct_Chng_Q4_Q1'].mean().reset_index()
status = change['Attrition_Flag']
value = change['Total_Ct_Chng_Q4_Q1']


#set the size of the plot
fig, ax = plt.subplots(figsize=(8,6))

# Create bars with different colors
bar_container = plt.bar(status, value, color=['green', 'orange'])

plt.xlabel("Customer Status")
plt.ylabel("Average Difference in Transaction Amount between Q1 & Q4")
plt.title("Bar chart of Average Difference in Transaction Amount betwwen Q1 & Q4")
plt.bar_label(bar_container)
plt.show()



#plot the box plot of Difference in Transaction Amount betwwen Q1 & Q4

fig, ax = plt.subplots(figsize=(8,6))
sns.boxplot(x=df_cleaned['Attrition_Flag'], y=df_cleaned['Total_Ct_Chng_Q4_Q1'], showmeans=True)
plt.xlabel("Customer Status")
plt.ylabel("Difference in Transaction Amount between Q1 & Q4")
plt.title("Boxplot of Difference in Transaction Amount betwwen Q1 & Q4")
plt.show()


#calculate the aveage Months_Inactive_12_mon by attrition flag


inactive = df_cleaned.groupby('Attrition_Flag')['Months_Inactive_12_mon'].mean().reset_index()
status = inactive['Attrition_Flag']
value = inactive['Months_Inactive_12_mon']


#set the size of the plot
fig, ax = plt.subplots(figsize=(8,6))

# Create bars with different colors
bar_container = plt.bar(status, value, color=['green', 'orange'])

plt.xlabel("Customer Status")
plt.ylabel("Average Number of months the customer is inactive ")
plt.title("Bar chart of Average number of months the customer is inactive by customer status")
plt.bar_label(bar_container)
plt.show()


#calculate the aveage Total_Relationship_Count by attrition flag
num_pro = df_cleaned.groupby('Attrition_Flag')['Total_Relationship_Count'].mean().reset_index()

status = num_pro['Attrition_Flag']
value = num_pro['Total_Relationship_Count']


#set the size of the plot
fig, ax = plt.subplots(figsize=(8,6))

# Create bars with different colors
bar_container = plt.bar(status, value, color=['green', 'orange'])

plt.xlabel("Customer Status")
plt.ylabel("Average Number of products the customer is holding")
plt.title("Bar chart of Average number of products the customer is holding by Customer status")
plt.bar_label(bar_container)
plt.show()


#calculate the aveage Months_on_book by attrition flag

length = df_cleaned.groupby('Attrition_Flag')['Months_on_book'].mean().reset_index()
status = length['Attrition_Flag']
value = length['Months_on_book']


#set the size of the plot
fig, ax = plt.subplots(figsize=(8,6))

# Create bars with different colors
bar_container = plt.bar(status, value, color=['green', 'orange'])

plt.xlabel("Customer Status")
plt.ylabel("Average length of the relationship with bank")
plt.title("Bar chart of Average Length of the Relationship with Bank")
plt.bar_label(bar_container)
plt.show()


#plot the scatter plot
fig, ax = plt.subplots(figsize=(8,6))
sns.scatterplot(x='Total_Revolving_Bal', y='Total_Trans_Amt', hue='Attrition_Flag', data=df_cleaned, legend="full")
 # set a title and labels
ax.set_title('Scatter Plot: Total_Revolving_Bal and Total_Trans_Amt Colored by Customer Status ')
ax.set_xlabel('Total_Revolving_Bal')
ax.set_ylabel('Total_Trans_Amt')
plt.legend(["Existing Customer" , "Attrited Customer"])
plt.show()


#plot the scatter plot

fig, ax = plt.subplots(figsize=(8,6))
sns.scatterplot(x='Total_Ct_Chng_Q4_Q1', y='Total_Relationship_Count', hue='Attrition_Flag', data=df_cleaned)
# set a title and labels
ax.set_title('Scatter Plot: Total_Ct_Chng & Total_Relationship_Count Colored by Customer Status ')
ax.set_xlabel('Total_Ct_Chng_Q4_Q1')
ax.set_ylabel('Total_Relationship_Count')
plt.show()


#plot the scatter plot
fig, ax = plt.subplots(figsize=(8,6))
sns.scatterplot(x='Dependent_count', y='Months_on_book', hue='Attrition_Flag', data=df_cleaned)

# set a title and labels
ax.set_title('Scatter Plot: Dependent_count & Months_on_book Colored by Customer Status ')
ax.set_xlabel('Dependent_count')
ax.set_ylabel('Months_on_book')
plt.show()
