
# Stock Price Prediction Application

This Django application predicts future stock prices using a Decision Tree regression model. It allows users to input a future date and displays the predicted stock price along with a plot of historical closing prices.

## Features

- Predicts stock prices based on historical data.
- Visualizes historical and predicted prices in a graph.
- Simple web interface for user interaction.

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS
- **Data Science**: Pandas, NumPy, Matplotlib, Scikit-learn

## Installation

1. **Clone the repository**:
   
   git clone <https://github.com/acrobyte007/Stock_Price_Prediction>
   cd stock-price-prediction
Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required packages:


pip install django pandas numpy matplotlib scikit-learn
Download the stock data: Make sure to have the apple_stock_data.csv file in the root directory of the project.

Run the server:
python manage.py runserver
Open your browser and go to http://127.0.0.1:8000/myapp/predict/ to access the application.

Usage
Enter a future date in the provided input field (format: YYYY-MM-DD).
Click on the "Predict" button.
View the predicted stock price and the plot comparing historical and predicted prices.
File Structure
stock-price-prediction/
│
├── myapp/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── apple_stock_data.csv
├── manage.py
└── stock_price_prediction/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py

Acknowledgements
Django
Pandas
NumPy
Matplotlib
Scikit-learn

# Stock Price Prediction Application

This Django application predicts future stock prices using a Decision Tree regression model. It allows users to input a future date and displays the predicted stock price along with a plot of historical closing prices.

## Features

- Predicts stock prices based on historical data.
- Simple web interface for user interaction.

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS
- **Data Science**: Pandas, NumPy, Matplotlib, Scikit-learn

