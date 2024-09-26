
document.getElementById('predictButton').addEventListener('click', function() {
    const dateInput = document.getElementById('dateInput').value;
    const resultDiv = document.getElementById('result');

    if (!dateInput) {
        resultDiv.innerHTML = '<p style="color:red;">Please enter a date.</p>';
        return;
    }

    // Construct the API URL
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
                resultDiv.innerHTML = `<p style="color:red;">Error: ${data.error}</p>`;
            } else {
                resultDiv.innerHTML = `<p>Predicted Price: $${data.predicted_price.toFixed(2)}</p>`;
            }
        })
        .catch(error => {
            resultDiv.innerHTML = `<p style="color:red;">Error fetching data: ${error.message}</p>`;
        });
});

