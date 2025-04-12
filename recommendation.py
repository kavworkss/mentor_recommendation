import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer, OneHotEncoder, StandardScaler
from sklearn.metrics.pairwise import cosine_similarity

def encode_features(df, feature_columns, multilabel=False):
    if multilabel:
        df_copy = df.copy()
        for col in feature_columns:
            df_copy[col] = df_copy[col].apply(lambda x: [s.strip() for s in x.split(',')])
        mlb = MultiLabelBinarizer()
        encoded = mlb.fit_transform(df_copy[feature_columns[0]])
        return pd.DataFrame(encoded, columns=mlb.classes_)
    else:
        ohe = OneHotEncoder(sparse_output=False)
        encoded = ohe.fit_transform(df[feature_columns])
        return pd.DataFrame(encoded, columns=ohe.get_feature_names_out(feature_columns))

def preprocess_data(aspirants_df, mentors_df):
    asp_subjects = encode_features(aspirants_df, ["PreferredSubjects"], multilabel=True)
    men_subjects = encode_features(mentors_df, ["SubjectExpertise"], multilabel=True)

    asp_cat = encode_features(aspirants_df, ["TargetCollegeTier", "PrepLevel", "LearningStyle"])
    men_cat = encode_features(mentors_df, ["AlmaMaterTier", "Availability"])

    aspirant_features = pd.concat([asp_subjects, asp_cat], axis=1)
    mentor_features = pd.concat([men_subjects, men_cat], axis=1)

    combined_cols = sorted(set(aspirant_features.columns).union(set(mentor_features.columns)))
    aspirant_features = aspirant_features.reindex(columns=combined_cols, fill_value=0)
    mentor_features = mentor_features.reindex(columns=combined_cols, fill_value=0)

    scaler = StandardScaler()
    aspirant_features_scaled = scaler.fit_transform(aspirant_features)
    mentor_features_scaled = scaler.transform(mentor_features)

    return aspirants_df, mentors_df, pd.DataFrame(aspirant_features_scaled), pd.DataFrame(mentor_features_scaled)

def recommend_mentors(selected_aspirant, mentors_df, aspirant_features, mentor_features):
    idx = selected_aspirant.name
    similarity = cosine_similarity([aspirant_features.iloc[idx]], mentor_features)[0]
    mentors_df = mentors_df.copy()
    mentors_df["MatchScore"] = similarity
    top = mentors_df.sort_values("MatchScore", ascending=False).head(3)
    return top
