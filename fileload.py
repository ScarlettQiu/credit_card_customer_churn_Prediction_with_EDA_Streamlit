
#create the function to read the file
def read(path):
    import pandas as pd
    df = pd.read_csv(path)
    return df


def clean(df):
    df_cleaned = df.drop(['CLIENTNUM','Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1', 'Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2'], axis=1)
    return df_cleaned


if __name__ == "__main__":
    # Main functions to Run
    df = read('https://raw.githubusercontent.com/ScarlettQiu/credit_card_customer_churn_prediction/af46862bff782f1008725fa49db88d1e36fc8d43/BankChurners.csv')
    print(df.info())
    # check the missing values in this dataset
    print(df.isnull().sum())
    #clean dateset
    df_cleaned = df.drop(['CLIENTNUM','Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1', 'Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2'], axis=1)
    print(df_cleaned.info())
