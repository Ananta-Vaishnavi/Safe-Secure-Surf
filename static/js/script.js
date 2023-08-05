document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
    const resultDiv = document.getElementById("result");

    form.addEventListener("submit", function(event) {
        event.preventDefault();
        const url = form.elements.url.value;

        // Perform AJAX request to Flask backend
        fetch("/check_phishing", {
            method: "POST",
            body: JSON.stringify({ url: url }),
            headers: {
                "Content-Type": "application/json"
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.is_phishing) {
                resultDiv.innerHTML = "<p>The URL is suspicious and may be a phishing attempt.</p>";
            } else {
                const proceed = confirm("The URL seems safe. Do you want to proceed?");
                if (proceed) {
                    window.open(url, "_blank");
                }
            }
        })
        .catch(error => {
            resultDiv.innerHTML = "<p>Error occurred while processing the URL. Please try again later.</p>";
            console.error(error);
        });
    });
});
