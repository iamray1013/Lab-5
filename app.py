from flask import Flask, request, render_template
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Load the dataset
fish_data = pd.read_csv('Fish.csv')

# Feature selection
X = fish_data[['Length1', 'Length2', 'Length3', 'Height', 'Width']]
y = fish_data['Weight']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = LinearRegression()
model.fit(X_train, y_train)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    length1 = float(request.form['Length1'])
    length2 = float(request.form['Length2'])
    length3 = float(request.form['Length3'])
    height = float(request.form['Height'])
    width = float(request.form['Width'])

    input_data = pd.DataFrame([[length1, length2, length3, height, width]], 
                              columns=['Length1', 'Length2', 'Length3', 'Height', 'Width'])
    prediction = model.predict(input_data)
    predicted_weight = prediction[0]

    return render_template('index.html', prediction_text=f'Predicted Fish Weight: {predicted_weight:.2f} grams')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
