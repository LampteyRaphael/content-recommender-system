import streamlit as st
import pandas as pd

# Load course data
@st.cache_data
def load_data():
    data = pd.read_csv('courses.csv')
    return data

data = load_data()

# Sidebar for user input
st.sidebar.header("User Input Features")

# Collect user preferences
category = st.sidebar.selectbox("Category", options=data['category'].unique())
difficulty = st.sidebar.selectbox("Difficulty", options=data['difficulty'].unique())
rating = st.sidebar.slider("Minimum Rating", min_value=0.0, max_value=5.0, value=4.0, step=0.1)

# Filter data based on user input
filtered_data = data[
    (data['category'] == category) &
    (data['difficulty'] == difficulty) &
    (data['rating'] >= rating)
]

# Display filtered data
st.header("Recommended Courses")
st.write(f"Based on your preferences, we found {len(filtered_data)} courses:")
st.dataframe(filtered_data)

# Display course details
for index, row in filtered_data.iterrows():
    st.subheader(f"{row['course_name']}")
    st.write(f"Category: {row['category']}")
    st.write(f"Difficulty: {row['difficulty']}")
    st.write(f"Rating: {row['rating']}")
