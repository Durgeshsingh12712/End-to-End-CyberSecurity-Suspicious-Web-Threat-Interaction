from flask import Flask, request, render_template

from cyberSecurity.pipeline import PredictionPipeline, CustomData

app = Flask(__name__)

app.route('/')
def index():
    return render_template('index.html')

app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
            bytes_in=float(request.form.get('bytes_in')),
            bytes_out=float(request.form.get('bytes_out')),
            duration_seconds=float(request.form.get('duration_seconds')),
            src_ip_country_code=request.form.get('src_ip_country_code')
        )

        pred_df = data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline = PredictionPipeline()
        print("Mid Prediction")

        results = predict_pipeline.predict(pred_df)
        print("After Prediction")

        threat_status = "Suspicious" if results[0] == 1 else "Normal"

        return render_template('results.html', results=threat_status)
    
if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)