document.addEventListener("DOMContentLoaded", () => {
    let description = ""; // Variable to store the description text

    document.getElementById("analyseButton").addEventListener("click", () => {
        chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
            let url = tabs[0].url;
            let resultDiv = document.getElementById("result");
            let initialInfo = document.getElementById("initialInfo");
            let analyseButton = document.getElementById("analyseButton");
            let alternativesButton = document.getElementById("alternativesButton");

            // Hide initial information and button
            initialInfo.style.display = "none";
            analyseButton.style.display = "none";
            resultDiv.style.display = "block"; // Show the result div

            // Show loading animation
            resultDiv.innerHTML = `
                <div class="loader"></div>
                <p>Please wait a few seconds, your product is being analysed</p>
            `;

            fetch('http://127.0.0.1:5000/analyse', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ url: url })
            })
            .then(response => response.json())
            .then(data => {
                console.log('URL received:', data.url);

                // Parse the result to extract rating, summary, detail, and description
                const lines = data.result.split('\n');
                const rating = lines[0];
                const summary = lines[1];
                const detailLines = lines.slice(2);
                let detail = "";
                const descIndex = detailLines.findIndex(line => line.startsWith("Description:"));

                if (descIndex !== -1) {
                    detail = detailLines.slice(0, descIndex).join(' ');
                    description = detailLines.slice(descIndex).join(' ').replace("Description: ", "");
                } else {
                    detail = detailLines.join(' ');
                }

                // Log the description for later use
                console.log("Description at frontend: ", description);

                // Display the result in the popup
                resultDiv.innerHTML = `
                    <div class="rating">${rating}</div>
                    <div class="summary">${summary}</div>
                    <div class="detail">${detail}</div>
                `;

                // Show the alternatives button after displaying the result
                alternativesButton.style.display = "block";
            })
            .catch((error) => {
                console.error('Error:', error);
                resultDiv.innerHTML = `<p>Error: ${error.message}</p>`;
            });
        });
    });

    document.getElementById("alternativesButton").addEventListener("click", () => {
        let resultDiv = document.getElementById("result");
        // Show loading animation while fetching alternatives
        resultDiv.innerHTML = `
            <div class="loader"></div>
            <p>Please give me a minute - just fetching some cool eco-friendly alternatives for you!</p>
        `;

        alternativesButton.style.display = "none";

        // Call the backend API to get alternatives
        fetch('http://127.0.0.1:5000/alternatives', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ description: description })
        })
        .then(response => response.json())
        .then(data => {
            console.log('Alternatives received:', data.alternatives);
            // Display the alternatives in the result div
            resultDiv.innerHTML = `<div class="alternatives">${data.alternatives}</div>`;
        })
        .catch((error) => {
            console.error('Error:', error);
            resultDiv.innerHTML = `<p>Error: ${error.message}</p>`;
        });
    });
});
