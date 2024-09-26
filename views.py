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





