import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Set page config
st.set_page_config(page_title="Mental Health in Tech", layout="wide")

import os

@st.cache_data
def load_and_clean_data():
    base_dir = os.path.dirname(__file__)
    filepath = os.path.join(base_dir, 'survey.csv')
    df = pd.read_csv(filepath)
    
    # Clean 'Age' column
    df['Age'] = df['Age'].apply(lambda x: x if 15 <= x <= 100 else np.nan)
    
    # Clean 'Gender' column
    male_terms = ['male', 'm', 'man', 'cis male', 'male-ish', 'maile', 'mal', 'male (cis)', 'make', 'male ', 'msle']
    female_terms = ['female', 'f', 'woman', 'cis female', 'femake', 'female ', 'cis-female/femme', 'female (cis)']
    
    df['Gender'] = df['Gender'].str.lower().str.strip()
    df['Gender'] = df['Gender'].apply(lambda x: 'Male' if x in male_terms else ('Female' if x in female_terms else 'Other/Trans/Queer'))
    
    # Handle missing values
    cols_to_fill = ['state', 'self_employed', 'work_interfere', 'comments']
    for col in cols_to_fill:
        if col in df.columns:
            df[col] = df[col].fillna('Unknown')
            
    return df

# Main App
st.title("Mental Health in Tech Workplace Survey 🧠💻")
st.markdown("This dashboard explores the 2014 survey measuring attitudes towards mental health and frequency of mental health disorders in the tech workplace.")

# Load Data
with st.spinner("Loading data..."):
    df = load_and_clean_data()

# Show raw data
if st.checkbox("Show Raw Data"):
    st.dataframe(df)

st.markdown("---")

# Metrics
total_responses = len(df)
treatment_sought = len(df[df['treatment'] == 'Yes'])
pct_treatment = (treatment_sought / total_responses) * 100

col1, col2, col3 = st.columns(3)
col1.metric("Total Responses", total_responses)
col2.metric("Sought Treatment", treatment_sought)
col3.metric("% Sought Treatment", f"{pct_treatment:.1f}%")

st.markdown("---")

# Visualizations
col1, col2 = st.columns(2)

with col1:
    st.subheader("Gender Distribution")
    fig_gender = px.pie(df, names='Gender', hole=0.4, color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig_gender, use_container_width=True)

with col2:
    st.subheader("Treatment Sought by Gender")
    treatment_gender = df.groupby(['Gender', 'treatment']).size().reset_index(name='Count')
    fig_treatment = px.bar(treatment_gender, x='Gender', y='Count', color='treatment', barmode='group')
    st.plotly_chart(fig_treatment, use_container_width=True)

col3, col4 = st.columns(2)

with col3:
    st.subheader("Age Distribution")
    fig_age = px.histogram(df, x='Age', nbins=30, color_discrete_sequence=['#636EFA'])
    st.plotly_chart(fig_age, use_container_width=True)

with col4:
    st.subheader("Does mental health interfere with work?")
    interfere = df['work_interfere'].value_counts().reset_index()
    interfere.columns = ['work_interfere', 'Count']
    fig_interfere = px.bar(interfere, x='work_interfere', y='Count', color='work_interfere')
    st.plotly_chart(fig_interfere, use_container_width=True)

st.markdown("---")
st.subheader("Top 10 Countries by Responses")
top_countries = df['Country'].value_counts().head(10).reset_index()
top_countries.columns = ['Country', 'Count']
fig_countries = px.bar(top_countries, y='Country', x='Count', orientation='h', color='Count')
st.plotly_chart(fig_countries, use_container_width=True)

