import matplotlib.pyplot as plt
import seaborn as sns


def plot_missing_values(df):
    # Create a list of columns that have missing values
    cols_with_missing = [col for col in df.columns if df[col].isnull().any()] # any() returns True if any of the values in the column is missing
    # Create a bar plot of the columns that have missing values
    sns.barplot(x=cols_with_missing, y=df[cols_with_missing].isnull().sum())
    plt.xticks(rotation=90)
    plt.show()







