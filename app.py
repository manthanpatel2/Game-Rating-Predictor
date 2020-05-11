from flask import Flask, render_template, request, redirect, url_for
import joblib
import re
import os

try:
    model = joblib.load('model.pkl')
    vectorizer = joblib.load('vectorizer.pkl')
    print("Model and Vectorizer rrun from file")
except (FileNotFoundError):
    print('Train model using trainModel.py script')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/predict', methods=['POST', 'GET'])
def predict():
    originalComment = request.form['comment']
    originalComment = originalComment.strip()
    print(len(str(originalComment)))
    if (request.method == 'POST' and len(str(originalComment)) >= 3):
        # originalComment = request.form['comment']
        words = re.split(r'\W+', originalComment)
        for i in range(len(words)):
            words[i] = ''.join([c for c in words[i] if not c.isdigit() ])
        comment = ' '.join(map(str, words)).lower()
        print(comment)
        v_comment = vectorizer.transform([comment])
        rating = model.predict(v_comment)[0]
        return render_template('index.html', comment = comment, rating= rating)
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 80)
