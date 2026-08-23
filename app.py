from flask import Flask, request, render_template
import model

app = Flask(__name__)

@app.route('/')
def home():
    # Serve the HTML form page
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract data from form input
    input_data = request.form.to_dict()
    prediction = model.make_prediction(input_data)
    # Render prediction in HTML
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
