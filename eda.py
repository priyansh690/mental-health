import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the dataset (Make sure to place your dataset in the same directory and update the filename)
# df = pd.read_csv('survey.csv')

def load_and_clean_data(filepath):
    """Loads and performs basic cleaning on the dataset."""
    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        print(f"Error: Could not find file at {filepath}. Please ensure the dataset is downloaded.")
        return None

    # Basic cleaning steps would go here
    # 1. Handle missing values (e.g., 'work_interfere', 'state', 'self_employed', 'comments')
    # 2. Standardize 'Gender' column (which is notoriously messy in this dataset)
    # 3. Handle outliers in 'Age'
    
    return df

def basic_eda(df):
    """Prints basic information about the dataset."""
    print("--- Dataset Info ---")
    print(df.info())
    
    print("\n--- Summary Statistics ---")
    print(df.describe(include='all'))
    
    print("\n--- Missing Values ---")
    print(df.isnull().sum())

def plot_treatment_distribution(df):
    """Plots the distribution of the target variable 'treatment'."""
    plt.figure(figsize=(8, 6))
    sns.countplot(x='treatment', data=df)
    plt.title('Distribution of Treatment Seeking')
    plt.show()

def plot_age_distribution(df):
    """Plots the distribution of Age (assuming basic cleaning is done)."""
    # Filtering out extreme outliers for visualization
    valid_ages = df[(df['Age'] > 0) & (df['Age'] < 100)]
    plt.figure(figsize=(10, 6))
    sns.histplot(valid_ages['Age'], bins=30, kde=True)
    plt.title('Age Distribution')
    plt.show()

if __name__ == "__main__":
    # Example usage:
    print("Welcome to the EDA script for the Mental Health in Tech survey.")
    print("Please download the 'survey.csv' file and uncomment the loading code to run the analysis.")
    
    # df = load_and_clean_data('survey.csv')
    # if df is not None:
    #     basic_eda(df)
    #     plot_treatment_distribution(df)
    #     plot_age_distribution(df)
