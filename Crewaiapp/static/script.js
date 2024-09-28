// static/script.js

function submitForm() {
    const form = document.getElementById('taxForm');
    const formData = new FormData(form);

    // Send the form data to the Flask backend using fetch API
    fetch('/submit', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        // Display the message in the status div
        document.getElementById('status').innerText = data.message;
        if (data.download_link) {
            // Create a download link if the form was filled successfully
            const downloadLink = document.createElement('a');
            downloadLink.href = data.download_link;
            downloadLink.innerText = "Download Filled Form";
            document.getElementById('status').appendChild(downloadLink);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('status').innerText = 'An error occurred while submitting the form.';
    });
}
