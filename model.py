import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

# Load and preprocess the dataset
df = pd.read_csv("career_data.csv")

le_skills = LabelEncoder()
le_interests = LabelEncoder()
le_style = LabelEncoder()
le_career = LabelEncoder()

df['Skills_encoded'] = le_skills.fit_transform(df['Skills'])
df['Interests_encoded'] = le_interests.fit_transform(df['Interests'])
df['Work_encoded'] = le_style.fit_transform(df['Work_Style'])
df['Career_encoded'] = le_career.fit_transform(df['Recommended_Career'])

X = df[['Skills_encoded', 'Interests_encoded', 'Math_Score', 'English_Score',
        'Logical_Score', 'Creativity', 'Communication', 'Programming', 'Work_encoded']]
y = df['Career_encoded']

model = DecisionTreeClassifier()
model.fit(X, y)

def predict_career(skills, interests, math, eng, logic, creative, comm, prog, work_style):
    input_df = pd.DataFrame([{
        'Skills_encoded': le_skills.transform([skills])[0],
        'Interests_encoded': le_interests.transform([interests])[0],
        'Math_Score': math,
        'English_Score': eng,
        'Logical_Score': logic,
        'Creativity': creative,
        'Communication': comm,
        'Programming': prog,
        'Work_encoded': le_style.transform([work_style])[0]
    }])
    pred = model.predict(input_df)
    return le_career.inverse_transform(pred)[0]
