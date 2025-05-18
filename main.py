import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

# Load updated dataset
df = pd.read_csv("career_data.csv")

# Encode categorical columns
le_skills = LabelEncoder()
le_interests = LabelEncoder()
le_style = LabelEncoder()
le_career = LabelEncoder()

df['Skills_encoded'] = le_skills.fit_transform(df['Skills'])
df['Interests_encoded'] = le_interests.fit_transform(df['Interests'])
df['Work_encoded'] = le_style.fit_transform(df['Work_Style'])
df['Career_encoded'] = le_career.fit_transform(df['Recommended_Career'])

# Features and target
X = df[['Skills_encoded', 'Interests_encoded', 'Math_Score', 'English_Score',
        'Logical_Score', 'Creativity', 'Communication', 'Programming', 'Work_encoded']]
y = df['Career_encoded']

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Prepare a sample input with column names
input_data = pd.DataFrame([{
    'Skills_encoded': le_skills.transform(['Python SQL'])[0],
    'Interests_encoded': le_interests.transform(['Tech'])[0],
    'Math_Score': 85,
    'English_Score': 70,
    'Logical_Score': 90,
    'Creativity': 65,
    'Communication': 75,
    'Programming': 88,
    'Work_encoded': le_style.transform(['Team'])[0]
}])

# Predict using DataFrame
pred = model.predict(input_data)
print("Recommended Career:", le_career.inverse_transform(pred)[0])
