from django.urls import path
from . import views

urlpatterns = [
    path('predict/', views.predict_stock_price, name='predict_stock_price'),  # Endpoint for stock price prediction
    path('stock_data/', views.get_stock_price_data, name='get_stock_price_data'),  # Endpoint for retrieving stock data from Excel
]
