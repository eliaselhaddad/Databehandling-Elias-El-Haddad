import matplotlib.pyplot as plt
import seaborn as sns


def plot_missing_values(df):
    # Calculate missing values
    missing_values = df.isnull().sum().sort_values(ascending=True)
    missing_values = missing_values[missing_values > 0]
    plt.figure(figsize=(10, 5))
    sns.barplot(x=missing_values.index, y=missing_values.values) # index is the column name, values is the number of missing values
    plt.xticks(rotation=90)
    plt.title('Missing values')
    plt.show()

    
    
    
    
    
    







