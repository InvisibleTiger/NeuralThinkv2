import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report
import joblib

# Step 1: Data Collection and Preparation
data = pd.read_csv('data.csv')  # Load your labeled dataset
text = data['text']  # Extract the text data
labels = data['label']  # Extract the corresponding labels

# Step 2: Feature Extraction
vectorizer = TfidfVectorizer()  # Initialize TF-IDF vectorizer
features = vectorizer.fit_transform(text)  # Convert text to TF-IDF features

# Step 3: Splitting the Dataset
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Step 4: Model Selection
svm = SVC()  # Initialize Support Vector Machine classifier

# Step 5: Training and Parameter Tuning
svm.fit(X_train, y_train)  # Train the SVM classifier

# Step 6: Model Evaluation
y_pred = svm.predict(X_test)  # Predict the labels for test set
print(classification_report(y_test, y_pred))  # Print classification report

# Step 7: Model Export
joblib.dump(svm, 'model.pkl')  # Export the trained model as 'model.pkl'