import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the trained model
model = joblib.load('model.pkl')
vectorizer = TfidfVectorizer()  # Initialize TF-IDF vectorizer

# Example text to classify
new_text = ["This is a positive review"]

# Feature extraction
new_features = vectorizer.transform(new_text)

# Classify the new text
predicted_labels = model.predict(new_features)

# Print the predicted labels
print(predicted_labels)