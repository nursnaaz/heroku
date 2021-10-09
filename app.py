import pandas as pd
from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("pipe.pkl")

@app.route('/')
def hi():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return "Hello how are you"

@app.route('/predict', methods=['POST'])
def predict():
    print(request.form.values())
    inp = [i for i in request.form.values()]

    test = {"experience":inp[0],"test_score":int(inp[1]),"interview_score":int(inp[2])}
    print(test)
    test_df = pd.DataFrame([test])
    print(test_df)
    res = model.predict(test_df)
    print(res[0])
    #return str(res[0])
    return render_template('index.html', prediction = "Employee Salary is {} ".format(str(res[0])))


if __name__ == "__main__":
    app.run(port = 9000, debug = True)