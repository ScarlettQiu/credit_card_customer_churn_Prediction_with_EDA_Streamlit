from fileload import read, clean
from feature_engineer import encode, split, over_sampling, scale, pca

def rf_selected(train_x, train_y):
    from sklearn.ensemble import RandomForestClassifier
    rf_s = RandomForestClassifier(random_state=333)
    rf_s.fit(train_x, train_y)
    return rf_s

def predict(test_x, rf_s):
    pred = rf_s.predict(test_x)
    return pred

def tune(model, train_x, train_y):
    from sklearn.model_selection import RandomizedSearchCV
    from scipy.stats import randint
    param_dist = {'n_estimators': randint(50, 500),
                  'max_depth': randint(1, 20)}
    # Use random search to find the best hyperparameters
    rand_search_s = RandomizedSearchCV(model,
                                       param_distributions=param_dist,
                                       n_iter=5,
                                       cv=5)
    rand_search_s.fit(train_x, train_y)
    best_rf_s = rand_search_s.best_estimator_
    return best_rf_s

def metric(test_y, pred_y):
    from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, ConfusionMatrixDisplay
    accuracy_s = accuracy_score(test_y, pred_y)
    precision_s = precision_score(test_y, pred_y)
    recall_s = recall_score(test_y, pred_y)

    print("Accuracy of Random Forest with PCA selected Features:", accuracy_s)
    print("Precision of Random Forest with PCA selected Features:", precision_s)
    print("Recall of Random Forest with PCA selected Features:", recall_s)

if __name__ == "__main__":
    # Main functions to Run
    import pandas as pd
    df_cleaned = encode('https://raw.githubusercontent.com/ScarlettQiu/credit_card_customer_churn_prediction/af46862bff782f1008725fa49db88d1e36fc8d43/BankChurners.csv')
    train_x, test_x, train_y, test_y = split(df_cleaned)
    train_x_o, train_y_o = over_sampling(train_x, train_y)
    train_x_std = scale(train_x_o)
    pca, train_x_pca_fit = pca(train_x_std)
    explained_variance = pca.explained_variance_ratio_
    pca_df = pd.DataFrame(train_x.columns, explained_variance).reset_index()
    pca_df.columns = ['variance', 'features']
    pca_df['variance_cum'] = pca_df['variance'].cumsum(axis=0)
    columns = pca_df[pca_df['variance_cum'] > 0.96]['features']
    train_x_sel = train_x.drop(columns, axis = 1)
    test_x_sel = test_x.drop(columns, axis=1)
    rf_s = rf_selected(train_x_sel, train_y)
    pred = predict(test_x_sel, rf_s)
    best_rf_s = tune(rf_s, train_x_sel, train_y)
    pred_y = predict(test_x_sel, best_rf_s)
    metric(test_y, pred_y)
