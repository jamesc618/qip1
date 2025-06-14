from flask import Flask, render_template, request
from model.predict import predict_from_input, predict_from_csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'csv_file' in request.files and request.files['csv_file'].filename != '':
        file = request.files['csv_file']
        result = predict_from_csv(file)
    else:
        features = {
            'pe_ratio': float(request.form['pe_ratio']),
            'pb_ratio': float(request.form['pb_ratio']),
            'de_ratio': float(request.form['de_ratio']),
            'market_cap': float(request.form['market_cap']),
            'revenue_growth': float(request.form['revenue_growth']),
        }
        result = predict_from_input(features)
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
