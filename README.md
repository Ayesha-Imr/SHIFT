# SHIFT ![icon48](https://github.com/user-attachments/assets/aeaf3bbb-a48d-4391-9129-723f6d3dd72d)


SHIFT is a browser extension that analyzes the sustainability and eco-friendliness of a product, and provides eco-friendly alternatives. Helping you shift towards sustainability, one purchase swap at a time.

## Langflow Flows

### Product Eco-Friendliness Analysis Flow
![image](https://github.com/user-attachments/assets/e373cc40-b59f-40e6-a3f6-8f58a03d05f8)

Explanation: A URL is passed in as input to the URL component which extracts all the text from the webpage. Then the extracted text is truncated to keep only the first 6000 characters to stay within the token limit of the Groq API and also to remove unnecessary information towards the bottom of the page. Next, the extracted and  truncated text is passed on to the Groq API with Llama3-70b model as the LLM along with a custom prompt that directs the LLM to give a proper formatted response (Python dict format) for ease in extraction later. The LLM response is then parsed to extract the different components (rating, TLDR, details and product_description) in separate variables for frontend display. The product_description is not displayed at the frontend but used as the input to the second flow which is discussed below.

### Sustainable Alternatives Flow
![image](https://github.com/user-attachments/assets/85918829-06a5-4f5b-90d1-038e3a28ed7d)
This flow consists of a Tool-calling Agent which again uses Llama3-70b LLM through Groq API. It has access to a Search Tool which utilises Search API, using Google as the search engine. The product_description extracted from the previous flow (discussed above) is passed as an input to this agent with instructions to search for similar but more sustainable alternatives for the product on the internet by utilising the Search Tool. After enough tool invocations, the agent generates a response based on the search results which is then passed to the frontend for display.

## Frontend (Chrome Extension)
The frontend of the SHIFT browser extension is built using HTML, CSS, and JavaScript. HTML structures the content and layout, CSS provides styling for a clean, user-friendly interface, and JavaScript implements interactive features and functionality, including fetching data from the backend and dynamically updating the UI. Additionally, Chrome Extension APIs are used to facilitate integration with the browser, allowing SHIFT to interact with web pages and perform analyses seamlessly.

![image](https://github.com/user-attachments/assets/18aa0462-d104-4e9a-b9cd-9c9ed2ea5011)      ![image](https://github.com/user-attachments/assets/d08da3db-021f-42a6-9374-80295fbd6474) ![image](https://github.com/user-attachments/assets/edeec5bf-6c32-4be1-9264-1a673ce48ff4)       ![image](https://github.com/user-attachments/assets/808a78b5-0d05-4dbc-8a6e-34098b6f2d95)   ![image](https://github.com/user-attachments/assets/c49b097b-4079-4f5c-9283-9f78d307cf2b)






## Project Setup

### Prerequisites
- Python >=3.10
- Chrome browser

### Steps to Setup Locally

1. **Clone the repository**
   ```sh
   git clone https://github.com/Ayesha-Imr/SHIFT.git
    ```
   
2. Create a virtual environment

   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```
  
3. Install dependencies

    ```sh
    pip install -r requirements.txt
    
    ```

4. Setup environment variables

   Rename env.txt to .env
   
   Open .env and add your API keys for Groq (https://console.groq.com/keys) and Search API (https://searchapi.io/):
   ```sh
   GROQ_API_KEY=your_groq_api_key
   SEARCH_API_KEY=your_search_api_key
    ```
6. Run the Python server
   ```sh
   python app.py
    ```
7. Load the Chrome Extension

   Open Chrome and go to chrome://extensions/.
   
   Enable "Developer mode" by clicking the toggle switch in the top right corner.
  
   Click the "Load unpacked" button and select the extension directory of the project.

8. Using the Extension

   Click on the extension icon in the Chrome toolbar.

   Use the "Analyse Product" button to get a detailed analysis of a product's sustainability.
   
   Use the "Get Alternatives" button to get eco-friendly alternatives.

   
9. Project Structure
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

   Note: Due to some unstability issues with Langflow, you might run into some issues with building custom components and fetching repsonses on the first few tries. But keep restarting the Python server and rerun it, it will eventually work.
