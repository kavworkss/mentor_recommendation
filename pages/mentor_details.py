import streamlit as st
import pandas as pd
import html
from recommendation import preprocess_data

st.set_page_config(layout="wide", page_title="Mentor Details")

st.markdown("""
<style>
h2 {
    color: #003366;
}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    aspirants_df = pd.read_csv("data/aspirants.csv")
    mentors_df = pd.read_csv("data/mentors.csv")
    return preprocess_data(aspirants_df, mentors_df)

_, mentors_df, _, _ = load_data()

query_params = st.query_params
mentor_name = query_params.get("name", "")

mentor_row = mentors_df[mentors_df["Name"] == mentor_name]

if not mentor_row.empty:
    mentor = mentor_row.iloc[0]
    st.title(f"👨‍🏫 Mentor: {mentor['Name']}")
    st.write(f"**Subject Expertise**: {mentor['SubjectExpertise']}")
    st.write(f"**Alma Mater Tier**: {mentor['AlmaMaterTier']}")
    st.write(f"**Teaching Strengths**: {mentor['TeachingStrengths']}")
    st.write(f"**Experience**: {mentor['Experience']}")
    st.write(f"**Availability**: {mentor['Availability']}")
    st.write(f"**Quote**: {html.escape(mentor['Quote'])}")
else:
    st.warning("Mentor not found.")
