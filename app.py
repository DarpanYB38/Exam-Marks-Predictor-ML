from flask import Flask, request, render_template
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form
        hours = data.get('textmarks')
        age = data.get('textage')
        internet = data.get('textinternet')
        if 'buttonpredict' in request.form:
            path = "--------<your file path>------/Exammarks.csv"
            data = pd.read_csv(path)
            medianvalue = data.hours.median()
            data.hours = data.hours.fillna(medianvalue)
            inputs = data.drop('marks', axis=1)
            output = data['marks']
            
            model = LinearRegression()
            model.fit(inputs, output)
            result = model.predict([[float(hours), int(age), int(internet)]])
            return render_template('index.html', result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
