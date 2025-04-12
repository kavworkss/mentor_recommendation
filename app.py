import streamlit as st
import pandas as pd
import html
from recommendation import preprocess_data, recommend_mentors

st.set_page_config(page_title="CLAT Mentor Recommender", layout="wide")
st.markdown("<style>" + open("style.css").read() + "</style>", unsafe_allow_html=True)

@st.cache_data
def load_all_data():
    aspirants_df = pd.read_csv("data/aspirants.csv")
    mentors_df = pd.read_csv("data/mentors.csv")
    return preprocess_data(aspirants_df, mentors_df)

aspirants_df, mentors_df, aspirant_features, mentor_features = load_all_data()

st.sidebar.title("🎯 Aspirant Profile")
aspirant_name = st.sidebar.selectbox("Choose your name", aspirants_df["Name"])
aspirant_index = aspirants_df[aspirants_df["Name"] == aspirant_name].index[0]

if st.sidebar.button("🔍 Find My Mentors"):
    selected_aspirant = aspirants_df.iloc[aspirant_index]
    recommended = recommend_mentors(selected_aspirant, mentors_df, aspirant_features, mentor_features)

    st.markdown(f"<h4 style='margin-top:10px;'>👋 Hi {aspirant_name}, here are your top 3 mentors:</h4>", unsafe_allow_html=True)

    cols = st.columns(3)
    for col, (_, mentor) in zip(cols, recommended.iterrows()):
        match_score = round(mentor["MatchScore"] * 100, 2)
        with col:
            st.markdown(f"""
            <div class='flash-card'>
                <div class='card-content'>
                    <h4>{mentor['Name']} ({mentor['AlmaMaterTier']})</h4>
                    <p>🎯 <b>Subjects:</b> {mentor['SubjectExpertise']}</p>
                    <p>📚 <b>Strengths:</b> {mentor['TeachingStrengths']}</p>
                    <p>🧠 <b>Experience:</b> {mentor['Experience']}</p>
                    <p>🕒 <b>Availability:</b> {mentor['Availability']}</p>
                    <p>💬 <b>Quote:</b> {html.escape(mentor['Quote'])}</p>
                    <div class='match-bar-container'>
                        <div class='match-bar-fill' style='width: {match_score}%;'></div>
                    </div>
                    <div class='match-bar-label'>{match_score}% Match</div>
                    <a target="_self" href="/mentor_details?name={mentor['Name']}">
                        <button class='contact-button'>📩 Contact Mentor</button>
                    </a>
                </div>
            </div>
            """, unsafe_allow_html=True)
