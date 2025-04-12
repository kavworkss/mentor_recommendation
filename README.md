Here’s the updated version of the README without the file structure in code blocks:

```markdown
# CLAT Mentor Recommendation System

This is a content-based mentor recommendation system built using Python, Pandas, Scikit-learn, and Streamlit, designed to help CLAT aspirants find suitable mentors (CLAT toppers) based on profile similarity.

## Features
- Loads mock data for both aspirants and mentors.
- Processes features like preferred subjects, college tier, preparation level, learning style, and mentor expertise.
- Calculates similarity using Cosine Similarity between profile vectors.
- Displays top 3 mentor recommendations using a stylish Streamlit interface.
- Includes mentor quote support, animated match score progress bars, and responsive flash card designs.
- Enables detailed mentor view with navigation through query parameters.

## File Structure
- `app.py`: Main Streamlit application
- `recommendation.py`: Preprocessing and recommendation logic
- `style.css`: Custom CSS for layout, glow effects, and styling
- `data/`: Contains sample data
  - `aspirants.csv`: Mock data for aspirants
  - `mentors.csv`: Mentor profile data with quotes
- `pages/`: Contains separate pages for Streamlit app
  - `mentor_details.py`: Detailed mentor view page
- `README.md`: Project documentation

## Approach
The system uses content-based filtering to recommend mentors by comparing feature vectors of aspirants and mentors:
- Vectorizing subject expertise and teaching strengths using Multi-Label Binarizer.
- One-Hot Encoding categorical attributes like tier, prep level, and learning style.
- Computing Cosine Similarity to measure profile match.
- Selecting top 3 highest scoring mentors.

## Future Improvements
- Incorporate feedback from aspirants on mentor effectiveness.
- Add ratings or satisfaction metrics post-mentorship.
- Track whether a recommendation was accepted or acted upon.
- Develop a hybrid recommendation engine that combines collaborative filtering with content-based logic.

## Setup Instructions

### Requirements
- Python 3.8 or higher
- streamlit
- pandas
- scikit-learn
- numpy

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/mentor_recommendation.git
   cd mentor_recommendation
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the App
To start the Streamlit application:
```bash
streamlit run app.py
```

## Architecture Overview
- Streamlit for the web interface.
- Python scripts for feature processing and recommendation logic.
- CSV files for sample aspirant and mentor data.
- Query-based navigation between pages.

## Contact
For questions or suggestions, please open an issue or connect via GitHub.
```

This version keeps the file structure in a simple list format without code blocks. It should be ready for direct copy-pasting into your GitHub repository!
