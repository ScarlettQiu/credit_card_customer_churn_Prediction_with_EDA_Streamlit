# credit_customer_churn_prediction

## Introduction	  
Churn also referred to as "attrition" or "churn rate," is the number of subscribers that have terminated their subscriptions over a predetermined time period (Burris, 2023). Customer churn rate is important to businesses because it will affect companies’ revenue. Businesses that lose their consumers not only lost revenue but also will pay high costs to acquire new customers (Moller, 2022). Therefore it is significant that companies can predict the customers who have high loyalty and who have a high possibility of leaving. Then we could take measures to maintain current customers and reduce the churn rate. This project aims to create a model to predict their churning customers and explore the factors which might retain them to stay and the reasons that caused them to leave.   

## Overview of Dataset
The dataset used in this project is from Kaggle which is about credit card customers which include their age, gender, education level, marital status, income category, and whether they are still active in this band, etc. There are 23 variables and 10,127 records in this dataset. I chose this dataset because it involves customer attrition status, which enables me to utilize the historical data to train the models for predicting churning customers. Moreover, it contains credit card customers ’demographic, product usage, relationship with the bank, etc. This would allow me to do customer profiling and segmentation. Also, by intuition, these variables probably have significant correlations with customer attrition which would be good predictors in the model.

## Credit Card Customers Dataset Overview    
The dataset used in this project is from Kaggle which is about credit card customers which include their age, gender, education level, marital status, income category, and whether they are still active in this band, etc. There are 23 variables and 10,127 records in this dataset. I chose this dataset because it involves customer attrition status, which enables me to utilize the historical data to train the models for predicting churning customers. Moreover, it contains credit card customers ’demographic, product usage, relationship with the bank, etc. This would allow me to do customer profiling and segmentation. Also, by intuition, these variables probably have significant correlations with customer attrition which would be good predictors in the model.

![image](https://user-images.githubusercontent.com/93269907/229969952-bf72585b-1342-4ef3-b382-39706844f3db.png)
 

## Business Problems and Objective  
In this project, I will mainly solve below the 4 questions. After the analysis and model training, I answered all these 4 business problems in the conclusion.

1.	What is the customer churn rate now in this bank?  
Before doing predictions, it is better to know the customer churn rate to check whether the dataset is imbalanced. This relates to the data preparation steps. The dataset would need to be oversampled if the customer churn rate is low.  

2.	Which factors indicates that customer might leave?  
One of the goals of this project is to understand the reasons why customers left the bank. Analyzing which factors would influence customers to leave or how they impact their behaviors are the key to understanding the reasons. 

3.	Which model has the best performance in predicting customer churn?  
I will create 3 models to predict customer churn. It is important to choose the best metrics to compare the 3 models and choose the best one for the bank to do the predictions.

4.	What we could do to those customers who are predicted to leave the bank?
The purpose of this project is to find the strategies to retain the customers who might leave the bank through the analysis and prediction.   

## EDA Dashboard created using Streamlit  
#### [EDA Dashboard](https://scarlettqiu-credit-card-customer-churn-pre-eda-streamlit-x8me96.streamlit.app/)  
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://scarlettqiu-credit-card-customer-churn-pre-eda-streamlit-x8me96.streamlit.app/)   
![image](https://user-images.githubusercontent.com/93269907/230689526-69911ce5-5dca-4721-8bd6-4b697d590dbf.png)


## Models
Classification is the process of recognizing, comprehending, and classifying things into predetermined groups. In machine learning, classification algorithms use the input data to assess the probability that the target variable falls into one of the categories (Banoula, 2023). Customer churn prediction is a binary classification whose result is churn or not. Therefore, in this project, I will create 1 classification model to make the predictions.    

Random Forest: random forest could be used for both regression and classification cases. It could efficiently work with larger datasets and has a better performance than the decision tree algorithm. Moreover, it does not need normalized features.   


## References
Banoula, M. (2023, February 14). What is classification in Machine Learning: Simplilearn. Simplilearn.com. Retrieved March 11, 2023, from https://www.simplilearn.com/tutorials/machine-learning-tutorial/classification-in-machine-learning   
Burris, M. (2023, January 25). What is churn rate & what affects it?: Customer churn factors. Nutshell. Retrieved March 11, 2023, from https://www.nutshell.com/blog/3-main-factors-customer-churn-rate   
Goyal, S. (2020, November 19). Credit Card customers. Kaggle. Retrieved March 30, 2023, from https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers?datasetId=982921&searchQuery=random%2B   
Kumar, N. (2019, March 9). Advantages of XGBoost algorithm in machine learning. Advantages of XGBoost Algorithm in Machine Learning. Retrieved March 11, 2023, from http://theprofessionalspoint.blogspot.com/2019/03/advantages-of-xgboost-algorithm-in.html   
Moller, K. (2022, September 7). How to calculate churn rate: Definition and formulas. Zendesk. Retrieved March 11, 2023, from https://www.zendesk.com/blog/customer-churn-rate/   
Shafi, A. (2018, May 16). Random Forest classification with Scikit-Learn. DataCamp. Retrieved March 30, 2023, from https://www.datacamp.com/tutorial/random-forests-classifier-python   

 

