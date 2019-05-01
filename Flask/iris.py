from os import path

import pandas as pd
from sklearn.externals import joblib
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from flask import Flask, jsonify, make_response, request, render_template, app

app = Flask(__name__)

def predict(query):
    features = list(query.values())
    location = r"/Users/rahulreddy/Documents/MachineLearning/datasets/iris.csv"
    #check if the data frame is persisted
    if path.isfile('df_training.pkl') :
        df_training=joblib.load('df_training.pkl')
    else:
        # load the training data from breast cancer data set
        df_training = pd.read_csv(location)
        #persist the object in a file
        joblib.dump(df_training, 'df_training.pkl')
    # copy the predictor variables into X and responses in y
    X = df_training[['sepal_length','sepal_width', 'petal_length', 'petal_width']]
    y = df_training['class']
    # split the data into training and test data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=9)
    # instantiate the classifier
    knn = KNeighborsClassifier(n_neighbors=5)
    # fit the training data
    knn.fit(X_train, y_train)
    # making predictions on the testing set
    y_pred = knn.predict(X_test)
    #sample = [[3, 5, 4, 2], [2, 3, 5, 4]]
    pred = knn.predict([features])
    return pred

@app.route('/')
def home():
   return render_template('iris.html')

@app.route('/rest')
def homeRest():
   return render_template('irisRest.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      pred =predict(result)
      jsonify({'prediction': list(pred)})
      return render_template("result.html",result = result, prediction= pred)

@app.route('/rest/result',methods = ['POST', 'GET'])
def rest_result():
   if request.method == 'POST':
      result = request.form
      pred =predict(result)
      return jsonify({'prediction': list(pred)})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':

    app.run(debug=True)
