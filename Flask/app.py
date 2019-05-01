from os import abort, path

from flask import Flask, jsonify, make_response, request, render_template
from requests import auth
import pandas as pd
from sklearn.externals import joblib
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import xlrd

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})


@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

@app.route('/predict', methods=['GET'])
def predict(query):
        if __name__ == '__main__':
            features=list(query.values())
        location = r"/Users/rahulreddy/Documents/MachineLearning/datasets/RSYSTEM-2.xlsx"
        exists = path.isfile('df_train.pkl')
        print(exists)
        #df_train = pd.read_excel(location)
        #joblib.dump(df_train, 'df_train.pkl')
        if joblib.load('df_train.pkl') is None and exists is True:
            df_train = pd.read_excel(location)
            joblib.dump(df_train, 'df_train.pkl')
        else:
            df_train = joblib.load('df_train.pkl')
        for col in df_train.iloc[:, 1:]:
            if df_train[col].dtype == 'object':
                df_train[col] = df_train[col].astype('category')
            else:
                df_train[col].dtype
        for col in df_train.iloc[:, 1:]:
            if df_train[col].dtype.name == 'category':
                df_train[col + "_Code"] = df_train[col].cat.codes
            else:
                df_train[col].dtype

        for col in df_train.iloc[:, 1:]:
            if df_train[col].dtype.name == 'category':
                df_train = df_train.drop(columns=[col])
            else:
                df_train[col].dtype
        X = df_train.iloc[:, 1:]
        y = df_train['PartNumber']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)
        knn = KNeighborsClassifier(n_neighbors=3)
        knn.fit(X_train, y_train)
        prediction = knn.predict([features])
        return prediction

@app.route('/')
def student():
   return render_template('test.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      partNumber =predict(result)
      print(jsonify({'prediction': list(partNumber)}))
      return render_template("result.html",result = result, prediction= partNumber)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)




if __name__ == '__main__':

    app.run(debug=True)
