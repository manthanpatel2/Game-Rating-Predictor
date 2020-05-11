import joblib

#read trained model & vectorizer from pickle file
try:
    model = joblib.load('model.pkl')
    vectorizer = joblib.load('vectorizer.pkl')
    print("model and vectorizer read from file")
except (FileNotFoundError):
    print('Train model using trainModel.py script')

while True:
    comment = input('\nEnter your comment: ')

    if comment == 'q': break
    comment = vectorizer.transform([comment])
    rate = model.predict(comment)[0]
    print(rate)
    print("\nType 'q' to quit." )

