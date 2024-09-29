const ctx = document.getElementById('priceChart').getContext('2d');
let priceChart;

document.getElementById('predictButton').addEventListener('click', function() {
    const dateInput = document.getElementById('dateInput').value;
    const resultDiv = document.getElementById('result');

    if (!dateInput) {
        resultDiv.innerHTML = '<p style="color:red;">Please enter a date.</p>';
        return;
    }

    // Construct the API URL for prediction
    const apiUrl = `http://127.0.0.1:8000/myapp/predict/?date=${dateInput}`;

    // Fetch the predicted stock price from the API
    fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok: ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            // Display the result
            if (data.error) {
                resultDiv.innerHTML = `<p class="error">Error: ${data.error}</p>`;
            } else {
                resultDiv.innerHTML = `<p>Predicted Price: $${data.predicted_price.toFixed(2)}</p>`;
            }
        })
        .catch(error => {
            resultDiv.innerHTML = `<p class="error">Error fetching data: ${error.message}</p>`;
        });

    // Fetch the stock data to display on the chart
    fetch('http://127.0.0.1:8000/myapp/stock_data/')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok: ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            if (data.error) {
                console.error("Error fetching stock data:", data.error);
                return;
            }

            const dates = data.dates;
            const actualPrices = data.actual_prices;
            const predictedPrices = data.predicted_prices;

            // Create or update the chart
            if (priceChart) {
                priceChart.destroy(); // Destroy existing chart instance
            }

            priceChart = new Chart(ctx, {
                type: 'line', // Chart type
                data: {
                    labels: dates, // X-axis labels
                    datasets: [
                        {
                            label: 'Actual Price',
                            data: actualPrices,
                            borderColor: 'rgba(75, 192, 192, 1)',
                            backgroundColor: 'rgba(75, 192, 192, 0.2)',
                            fill: true,
                        },
                        {
                            label: 'Predicted Price',
                            data: predictedPrices,
                            borderColor: 'rgba(255, 99, 132, 1)',
                            backgroundColor: 'rgba(255, 99, 132, 0.2)',
                            fill: true,
                        },
                    ],
                },
                options: {
                    responsive: true,
                    scales: {
                        x: {
                            title: {
                                display: true,
                                text: 'Date',
                            },
                        },
                        y: {
                            title: {
                                display: true,
                                text: 'Price',
                            },
                        },
                    },
                },
            });
        })
        .catch(error => {
            console.error("Error fetching stock data:", error.message);
        });
});

