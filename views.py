import os
import pandas as pd
import numpy as np
import pickle
from datetime import datetime
from django.http import JsonResponse
import logging

# Configure logging
logger = logging.getLogger(__name__)

# Load the trained model from the pickle file
model_path = os.path.join(os.path.dirname(__file__), 'tree_model.pkl')
try:
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    logger.error("Model file not found at %s", model_path)

def predict_stock_price(request):
    future_date_str = request.GET.get('date', None)

    if future_date_str:
        try:
            future_date = pd.to_datetime(future_date_str).toordinal()
            future_price = model.predict(np.array([[future_date]]))

            response_data = {
                'predicted_price': future_price[0],
                'input_date': future_date_str
            }
            logger.info("Response data: %s", response_data)

            return JsonResponse(response_data, status=200)

        except ValueError as ve:
            logger.error("Date conversion error: %s", str(ve))
            return JsonResponse({'error': 'Invalid date format. Please use YYYY-MM-DD.'}, status=400)
        except Exception as e:
            logger.error("Error in prediction: %s", str(e))
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'No date provided'}, status=400)


def get_stock_price_data(request):
    try:
        # Define the path to the Excel file
        excel_file_path = os.path.join(os.path.dirname(__file__), 'predicted_vs_actual_each_date.xlsx')
        data = pd.read_excel(excel_file_path, parse_dates=['Date'])

        # Print column names for debugging
        logger.info("Columns in Excel file: %s", data.columns.tolist())

        # Rename the columns to match expected names
        data.rename(columns={
            'Actual Close Price': 'Actual Price',
            'Predicted Price': 'Predicted Price'
        }, inplace=True)

        # Ensure the necessary columns are present
        if {'Date', 'Actual Price', 'Predicted Price'}.issubset(data.columns):
            # Sort by date in ascending order
            data = data.sort_values(by='Date', ascending=True)

            # Prepare the JSON response
            response_data = {
                'dates': data['Date'].dt.strftime('%Y-%m-%d').tolist(),  # Format dates as strings
                'actual_prices': data['Actual Price'].tolist(),
                'predicted_prices': data['Predicted Price'].tolist()
            }
            
            return JsonResponse(response_data, status=200)

        else:
            logger.error("The Excel file must contain 'Date', 'Actual Price', and 'Predicted Price' columns.")
            return JsonResponse({'error': "Invalid Excel format. Columns 'Date', 'Actual Price', 'Predicted Price' required."}, status=400)

    except FileNotFoundError:
        logger.error("Excel file not found at %s", excel_file_path)
        return JsonResponse({'error': 'Excel file not found.'}, status=404)

    except Exception as e:
        logger.error("Error reading Excel or preparing data: %s", str(e))
        return JsonResponse({'error': str(e)}, status=500)
