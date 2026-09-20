import pandas as pd
import numpy as np

def load_and_clean_data(filepath):
    """
    Loads the mental health survey data and performs basic cleaning.
    """
    print(f"Loading data from {filepath}...")
    df = pd.read_csv(filepath)
    
    print(f"Initial shape: {df.shape}")
    
    # 1. Clean 'Age' column (handle outliers)
    # Some ages might be negative or unrealistically high, let's keep it between 15 and 100
    df['Age'] = df['Age'].apply(lambda x: x if 15 <= x <= 100 else np.nan)
    
    # 2. Clean 'Gender' column
    # The gender column has many variations (e.g., 'M', 'Male', 'm', 'Female', 'F', 'f', 'Woman', etc.)
    # Let's standardize them into basic categories for simpler analysis
    male_terms = ['male', 'm', 'man', 'cis male', 'male-ish', 'maile', 'mal', 'male (cis)', 'make', 'male ', 'msle']
    female_terms = ['female', 'f', 'woman', 'cis female', 'femake', 'female ', 'cis-female/femme', 'female (cis)']
    
    df['Gender'] = df['Gender'].str.lower().str.strip()
    df['Gender'] = df['Gender'].apply(lambda x: 'Male' if x in male_terms else ('Female' if x in female_terms else 'Other/Trans/Queer'))
    
    # 3. Handle missing values
    # Fill missing values in categorical columns with 'Unknown'
    cols_to_fill = ['state', 'self_employed', 'work_interfere', 'comments']
    for col in cols_to_fill:
        if col in df.columns:
            df[col] = df[col].fillna('Unknown')
    
    print("Data cleaning completed.")
    return df

if __name__ == "__main__":
    file_name = 'survey.csv'
    
    # Load and clean
    cleaned_df = load_and_clean_data(file_name)
    
    # Display summary
    print("\n--- Cleaned Dataset Info ---")
    print(cleaned_df.info())
    
    print("\n--- Gender Distribution ---")
    print(cleaned_df['Gender'].value_counts())
    
    print("\n--- Treatment sought by Gender ---")
    print(pd.crosstab(cleaned_df['Gender'], cleaned_df['treatment']))
    
    # Optionally save the cleaned dataset
    # cleaned_df.to_csv('cleaned_survey.csv', index=False)
    # print("\nCleaned data saved to 'cleaned_survey.csv'")
