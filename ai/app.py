from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('iris_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the request
    data = request.json
    features = np.array(data['features']).reshape(1, -1)  # Reshape for a single sample

    # Make prediction
    prediction = model.predict(features)
    
    # Return the result as a JSON response
    return jsonify({'predicted_class': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
