# Game-Rating-Predictor using SVM

# The Goal of Project:
The purpose of this project is to build a model that will be trained on given data and will predict the ranting from 0 to 10 from the comment that we give.First, we will import the necessary libraries and the will load the data from csv file 'bgg-13m-reviews.csv'. Now, we will pre-process the data by formating the comments and rating and will divide into DataFrames and vectorize every DataFrames. I have used SVM classifier because it is a supervised machine learning algorithm that can be used for classification. In general terms SVM is very good when you have a huge number of features. For example for text classification in a bag of words model

# Deploy Flask Implementation Using AWS EC2
- Download my repository
- Download data from here: https://www.kaggle.com/jvanelteren/boardgamegeek-reviews 
- Now run trainModel.py to get 2 files: vectorizer.pkl and model.pkl
- Make an account in AWS and launch EC2 instance
- use this command to copy all files of your flask app to EC2 instance: scp -i path/to/key file/to/copy user@ec2-xx-xx-xxx- xxx.compute-1.amazonaws.com:path/to/file
- now using command pip install -r /path/to/requirements.txt install all requirements in your instance.
- Now run command sudo python3 app.py 
- Make sure to use python3 and pip3 for linux instance.
- Now go on aws and using Public DNS (IPv4) you can see your application.
