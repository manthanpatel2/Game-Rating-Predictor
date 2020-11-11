# Game-Rating-Predictor using SVM

### The Goal of Project:
 The purpose of this project is to build a model that will be trained on given data and will predict the ranting from 0 to 10 from the comment that we give.First, we will import the necessary libraries and the will load the data from csv file 'bgg-13m-reviews.csv'. Now, we will pre-process the data by formating the comments and rating and will divide into DataFrames and vectorize every DataFrames. I have used SVM classifier because it is a supervised machine learning algorithm that can be used for classification. In general terms SVM is very good when you have a huge number of features. For example for text classification in a bag of words model

### Dataset:
The dataset used in this project is "BoardGameGeek Review", around 13 million reviews of game, from kaggle.
 
Link: https://www.kaggle.com/jvanelteren/boardgamegeek-reviews 
 
### Vectorization:
I have used tf-idf algorithm to trasnform text into meaningful representation of numbers  which wil be used to fit in machine learning algorithm for predition.

### SVM Classifier:
SVM performs very good in text classification for this typpe of larg datset. SVM with direct tf-idf vectors does the best both for quality & performance for text classification in a bag of words model. 

###  Run localy:
- Download my repository 
- Open my repo in console 
- create virtual environment
- Now install all the requirement by running following command:
```
 pip install -r requiremnet.txt
```
- Now run following comand to start the app localy
```
 python app.py
```

### Deploy Flask Implementation Using AWS EC2
- Launch EC2 instance on AWS
- Use this command to copy all files of your flask app to EC2 instance:
```
 scp -i path/to/key file/to/copy user@ec2-xx-xx-xxx- xxx.compute-1.amazonaws.com:path/to/file
```
- Now use this command to install all requirements in your instance.
```
 pip install -r /path/to/requirements.txt
```
- Now run this command to start app:
```
 sudo python3 app.py 
```
- Make sure to use python3 and pip3 for linux instance.
- Now go on aws and using Public DNS (IPv4) you can see your application.
