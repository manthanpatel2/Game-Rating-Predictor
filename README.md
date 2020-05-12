# comment-predictor using SVM
This project implement SVM to predict rating of a comment on game review dataset from Kaggle.

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
