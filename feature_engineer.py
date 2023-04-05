from fileload import read, clean

#encoding categorical variables
def encode(file):
    import pandas as pd
    df = read(file)
    df_cleaned = clean(df)
    categorical = df_cleaned.columns[df_cleaned.dtypes == object]
    df_new = pd.get_dummies(df_cleaned, columns=categorical, drop_first=True)
    return df_new

#split the dataset
def split(df):
    y = df['Attrition_Flag_Existing Customer']
    x = df.drop(['Attrition_Flag_Existing Customer'], axis=1)
    from sklearn.model_selection import train_test_split
    train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.3, random_state=111)
    return train_x, test_x, train_y, test_y




#oversampling
def over_sampling(train_x, train_y):
    from imblearn.over_sampling import RandomOverSampler
    ros = RandomOverSampler(random_state=2)
    train_x, train_y = ros.fit_resample(train_x, train_y)
    return train_x, train_y

#feature scaling
def scale(df):
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    sc.fit(df)
    df_scale = sc.transform(df)
    train_x_tran = sc.transform(df_scale)
    import pandas as pd
    train_x_std = pd.DataFrame(train_x_tran, columns=df.columns)
    return train_x_std

#PCA: Feature selection
def pca(df):
    from sklearn.decomposition import PCA
    pca = PCA(n_components=32)
    train_x_pca = pca.fit_transform(df)
    import pandas as pd
    train_x_pca_fit = pd.DataFrame(train_x_pca, columns=df.columns)
    return pca, train_x_pca_fit


if __name__ == "__main__":
    # Main functions to Run
    df = encode('/Users/qiuyu/Desktop/ALY6140/M2/Capstone/BankChurners.csv')
    print(df.head())
    train_x, test_x, train_y, test_y=split(df)
    # check the shape of training set and test set
    print('The shape of train_x is {}.'.format(train_x.shape))
    print('The shape of test_x is {}.'.format(test_x.shape))
    print('The shape of train_y is {}.'.format(train_y.shape))
    print('The shape of test_y is {}.'.format(test_y.shape))
    train_x, train_y = over_sampling(train_x, train_y)
    print(train_y.value_counts().reset_index())
    train_x_std = scale(train_x)
    test_x_std = scale(test_x)
    pca, train_x_pca_fit = pca(train_x_std)
    explained_variance=pca.explained_variance_ratio_
    # plot the Ratio of Variance Explained by the Variable
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.plot(train_x.columns, explained_variance)
    plt.title('Ratio of Variance Explained by the Variable')
    plt.ylabel('Ratio of Variance')
    plt.xticks(rotation=90)
    plt.show()

    import pandas as pd
    # calculate the cumulative ratio
    pca_df = pd.DataFrame(train_x.columns, explained_variance).reset_index()
    pca_df.columns = ['variance', 'features']
    pca_df['variance_cum'] = pca_df['variance'].cumsum(axis=0)

    import seaborn as sns
    # plot the cumulative ratio
    fig, ax = plt.subplots(figsize=(10, 6))
    line = sns.lineplot(x='features', y='variance_cum', data=pca_df)

    # Annotate label points
    plt.title('Cumulative Ratio of Variance Explained by the Variable')
    plt.ylabel('Ratio of Variance')
    plt.xticks(rotation=90)
    plt.show()

    columns = pca_df[pca_df['variance_cum'] > 0.96]['features']
    train_x_select = train_x.drop(columns, axis = 1)
    print(train_x_select)
