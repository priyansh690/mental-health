# Streamlit App Plan: Mental Health in Tech

## 1. Overview
A Streamlit web application to visualize and explore the Mental Health in Tech dataset interactively. It will allow users to answer the inspiration questions regarding geographic variations and predictors of mental health illness in the workplace.

## 2. Pages / Sections

### A. Home Page (Overview)
- **Title**: Mental Health in Tech Survey (2014)
- **Description**: Brief introduction to the dataset, source (OSMI), and the purpose of the app.
- **Key Metrics (KPIs)**: Total respondents, percentage seeking treatment, top countries represented.

### B. Geographic Analysis
- **Goal**: Address "How does the frequency of mental health illness vary by geographic location?"
- **Visualizations**:
  - Choropleth map of respondents by Country.
  - Bar chart comparing the percentage of positive 'treatment' responses by top countries.
  - (For US data) State-by-state breakdown of attitudes and treatment seeking.
- **Filters**: Filter by Gender, Age group, or Tech Company status.

### C. Workplace Predictors & Attitudes
- **Goal**: Address "What are the strongest predictors of mental health illness or certain attitudes?"
- **Visualizations**:
  - Breakdown of 'treatment' by 'family_history'.
  - Correlation between 'benefits' (does employer provide benefits) and 'treatment'.
  - Analysis of 'mental_health_consequence' vs 'phys_health_consequence'.
  - Impact of 'remote_work' and 'tech_company' on mental health status.

### D. Data Explorer (Optional)
- Allow users to view raw data.
- Interactive filtering capabilities to slice and dice the dataset.

## 3. Tech Stack & Requirements
- `streamlit`: For the web app framework.
- `pandas`: For data manipulation and cleaning.
- `plotly` or `altair`: For interactive visualizations (better suited for Streamlit than matplotlib/seaborn).

## 4. Next Steps
1. Finish the data cleaning process in `eda.py` (specifically Age and Gender).
2. Save the cleaned dataset to a new CSV (e.g., `cleaned_survey.csv`).
3. Create `app.py` and begin implementing the layout using Streamlit.
