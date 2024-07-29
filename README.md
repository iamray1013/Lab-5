# Fish Weight Prediction

This project is a simple web application that predicts the weight of a fish based on its measurements. The app is built using Flask and a Linear Regression model trained on the Fish Market dataset.

## Dataset

The Fish Market dataset contains measurements of fish specimens. The dataset includes the following features:
- `Length1`: Vertical length
- `Length2`: Diagonal length
- `Length3`: Cross length
- `Height`: Height of the fish
- `Width`: Diagonal width

The target variable is `Weight`, which represents the weight of the fish in grams.

## Files

### 1. `app.py`

The `app.py` file contains the Flask web application code. It performs the following tasks:
- Loads the Fish Market dataset.
- Selects the features (`Length1`, `Length2`, `Length3`, `Height`, `Width`) and the target variable (`Weight`).
- Splits the data into training and testing sets.
- Trains a Linear Regression model on the training data.
- Defines routes for the web application, including the home page and the prediction functionality.

### 2. `templates/index.html`

The `index.html` file is an HTML template for the web page. It includes:
- A form for users to input the fish measurements (`Length1`, `Length2`, `Length3`, `Height`, `Width`).
- A section to display the predicted weight of the fish.

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fish-weight-prediction.git
