import pandas as pd
import numpy as np
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.svm import LinearSVC

from os.path import join
from sys import path

#joining file path
filePath = join(join(path[0], 'boardgamegeek-reviews'), 'bgg-13m-reviews.csv')

print(filePath)

#load raw data
def loadData(path):
    d = pd.read_csv(path)
    d = d[['comment', 'rating']].copy()
    d = d.fillna('')
    
    return d


#format raw data
def formatRawData(rawData):
    rawData['comment'] = [c.strip().lower() for c in rawData['comment']]
    rawData['comment'] = [c if c.islower() else '' for c in rawData['comment']]
    
    #only take data with comments
    rawData = rawData[rawData['comment'].apply(lambda alpha: len(alpha) > 0)]
    #only take data with ratings 1 or greater
    rawData = rawData[rawData['rating'].apply(lambda alpha: float(alpha) >= 1)]
    rawData = rawData.sample(frac = 1).reset_index(drop = True)  
    
    rawData['rating'] = [float(rating) for rating in rawData['rating']]
    
    
    #for i in range(len(rawData)):
     #   words = re.split(r'\W+', rawData['comment'][i])
      #  stop_words = set(stopwords.words('english'))
       # words = [w for w in words if not w in stop_words]
        #rawData.loc[i, 'comment'] = ' '.join(map(str, words)).lower()
        
    return rawData



rawData = loadData(filePath)
print(rawData['comment'][0])
print(len(rawData))

data = formatRawData(rawData)
print(data['comment'][0])
print(len(data))


#devide formatted data
def divideData(data, train):
    data = data.sample(frac=1).reset_index(drop = True)
    #dataLen = len(data['comment'])
    dataLen = data.shape[0]
    
    trainData = data[:int(train * dataLen)]
    devData = data[int(train * dataLen):int((train + 1)/2 * dataLen)]
    testData = data[int((train + 1)/2 * dataLen):]
    
    trainData = trainData.sample(frac = 1).reset_index(drop = True)
    devData = devData.sample(frac = 1).reset_index(drop = True)
    testData = testData.sample(frac = 1).reset_index(drop = True)
    
    return [trainData, devData, testData]



trainData, devData, testData = divideData(data, 0.92).copy()
print(trainData.shape[0])
print(devData.shape[0])
print(testData.shape[0])


#vectorizer implementation
def vectorizeData(data, vectorizer):
    data_c = vectorizer.transform(data['comment'])
    data_r = np.asarray([int(r) if r%int(r) <= 0.5 else int(r + 1) for r in data['rating']])
    
    return [data_c, data_r]


#vectorizze data
vectorizer = TfidfVectorizer(ngram_range=(1, 2))
vectorizer.fit(trainData['comment'])
train_c, train_r = vectorizeData(trainData, vectorizer).copy()
test_c, test_r = vectorizeData(testData, vectorizer).copy()
dev_c, dev_r = vectorizeData(devData, vectorizer).copy()


#training of model
svm = LinearSVC(C = 0.1)
svm.fit(train_c, train_r)


#accuracy using dev
predDev_r = svm.predict(dev_c)
accuracy = accuracy_score(dev_r, predDev_r)*100
print('SVM accuracy using dev data: {:.5f}%\n'.format(accuracy))


#calculating final accuracy of our model
predTest_r = svm.predict(test_c)
fAccuracy = accuracy_score(test_r, predTest_r)*100
print('SVM Final accuracy: {:.5f}%\n'.format(fAccuracy))

# while True:
#     comment = input('\n Enter your comment: ')

#     print("Type 'q' to quit." )

#     if comment == 'q': break
#     comment = vectorizer.transform([comment])
#     rate = model.predict(comment)[0]
#     print(rate)

# #save the model as a pickle in a file so we can use trained model to predict comment's rating
joblib.dump(svm, 'model.pkl')

joblib.dump(vectorizer, 'vectorizer.pkl')


