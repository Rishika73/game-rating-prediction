from flask import Flask, request, render_template
import model

app = Flask(__name__)

@app.route('/')
def home():
    # Serve the HTML form page
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.form.to_dict()
    prediction = model.make_prediction(input_data)

    return render_template(
        'index.html',
        prediction=prediction,
        form_data=input_data
    )

if __name__ == '__main__':
    app.run(debug=True)
