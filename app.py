from flask import Flask, request, render_template
import joblib
import re
import unicodedata

app = Flask(__name__)

# Load model and preprocessing tools
clf = joblib.load('mood_model.pkl')
vect = joblib.load('tfidf_vectorizer.pkl')
selector = joblib.load('feature_selector.pkl')

# Text cleaning function (same as during training)
def clean_text(text):
    if not isinstance(text, str):
        return ""
    # Unicode normalization
    text = unicodedata.normalize('NFC', text)
    # Keep only Khmer letters and spaces
    text = re.sub(r'[^\w\s\u1780-\u17FF\u19E0-\u19FF]', '', text)
    # Normalize spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text.lower()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    raw_text = request.form['text']
    cleaned_text = clean_text(raw_text)
    
    # Transform using the same pipeline as during training
    X_tfidf = vect.transform([cleaned_text])
    X_selected = selector.transform(X_tfidf)
    
    mood = clf.predict(X_selected)[0]
    probas = clf.predict_proba(X_selected)[0]
    
    mood_probs = {
        cls: round(float(probas[i]) * 100, 2)
        for i, cls in enumerate(clf.classes_)
    }

    return render_template('index.html', text=raw_text, mood=mood, probs=mood_probs)

if __name__ == '__main__':
    app.run(debug=True)