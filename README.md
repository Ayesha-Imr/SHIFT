# SHIFT ![icon48](https://github.com/user-attachments/assets/aeaf3bbb-a48d-4391-9129-723f6d3dd72d)


SHIFT is a browser extension that analyzes the sustainability and eco-friendliness of a product, and provides eco-friendly alternatives. Helping you shift towards sustainability, one purchase swap at a time.

## Langflow Flows

### Product Eco-Friendliness Analysis Flow
![image](https://github.com/user-attachments/assets/e373cc40-b59f-40e6-a3f6-8f58a03d05f8)


### Sustainable Alternatives Flow
![image](https://github.com/user-attachments/assets/85918829-06a5-4f5b-90d1-038e3a28ed7d)


## Project Setup

### Prerequisites
- Python >=3.10
- Chrome browser

### Steps to Setup Locally

1. **Clone the repository**
   ```sh
   git clone https://github.com/your-username/repo-name.git
   cd repo-name
    ```
   
2. Create a virtual environment

   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```
  
3. Install dependencies

    ```sh
    pip install -r requirements.txt
    Setup environment variables
    ```

4. Rename env.txt to .env
  Open .env and add your API keys for Groq and Search API:
   ```sh
   GROQ_API_KEY=your_groq_api_key
   SEARCH_API_KEY=your_search_api_key
    ```
5. Run the Python server
   ```sh
   python app.py
    ```
6. Load the Chrome Extension

   Open Chrome and go to chrome://extensions/.
   
   Enable "Developer mode" by clicking the toggle switch in the top right corner.
  
   Click the "Load unpacked" button and select the extension directory of the project.

7. Using the Extension

   Click on the extension icon in the Chrome toolbar.

   Use the "Analyse Product" button to get a detailed analysis of a product's sustainability.
   
   Use the "Get Alternatives" button to get eco-friendly alternatives.

   
8. Project Structure
   ```sh
    langflowapp/
    │
    ├── backend/
    │   ├── __pycache__/
    │   ├── app.py
    │   ├── flow_one.py
    │   ├── flow_two.py
    │   ├── Product Eco-Friendliness Analysis.json
    │   ├── requirements.txt
        ├── .env
    │   └── Sustainable Alternatives.json
    │
    ├── extension/
    │   ├── background.js
    │   ├── icon16.png
    │   ├── icon48.png
    │   ├── icon128.png
    │   ├── manifest.json
    │   ├── popup.html
    │   ├── popup.js
    │   └── styles.css
    │
    ├── venv/
    ├── .gitignore
    └── README.md
    ```
