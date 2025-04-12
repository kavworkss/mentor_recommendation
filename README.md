#CLAT Mentor Recommendation System
*This project is a content-based mentor recommendation system built using Python, Pandas, Scikit-learn, and *Streamlit. It is designed to help CLAT aspirants find suitable mentors (CLAT toppers) based on profile similarity.

#Features
*Loads mock data for both aspirants and mentors
*Processes features like preferred subjects, college tier, preparation level, learning style, and mentor expertise
*Calculates similarity using Cosine Similarity between profile vectors
*Displays top 3 mentor recommendations using a stylish Streamlit interface
*Includes mentor quote support, animated match score progress bars, and responsive flash card designs
*Enables detailed mentor view with navigation through query parameters

#File Structure

mentor_recommendation/
│
├── app.py                   # Main Streamlit application
├── recommendation.py        # Preprocessing and recommendation logic
├── style.css                # Custom CSS for layout, glow effects, and styling
├── data/
│   ├── aspirants.csv        # Mock data for aspirants
│   └── mentors.csv          # Mentor profile data with quotes
├── pages/
│   └── mentor_details.py    # Detailed mentor view page
└── README.md                # Project documentation

#Approach
*The system uses content-based filtering to recommend mentors by comparing feature vectors of aspirants and mentors. Key steps include:
*Vectorizing subject expertise and teaching strengths using Multi-Label Binarizer
*One-Hot Encoding categorical attributes like tier, prep level, and learning style
*Computing Cosine Similarity to measure profile match
*Selecting top 3 highest scoring mentors

#Future Improvements
*The system can be enhanced over time by incorporating:
*Feedback from aspirants on mentor effectiveness
*Ratings or satisfaction metrics post-mentorship
*Tracking whether a recommendation was accepted or acted upon
*A hybrid recommendation engine that combines collaborative filtering with content-based logic

#Setup Instructions
*Requirements
*Python 3.8 or higher
*streamlit
*pandas
*scikit-learn
*numpy

#Installation
*Clone the repository
git clone https://github.com/your-username/mentor_recommendation.git
cd mentor_recommendation
*Install dependencies
pip install -r requirements.txt
*Running the App
Use the following command to start the Streamlit application:
streamlit run app.py

#Architecture Overview
*Streamlit for the web interface
*Python scripts for feature processing and recommendation logic
*CSV files for sample aspirant and mentor data
*Query-based navigation between pages

#Contact
For questions or suggestions, please open an issue or connect via GitHub.

