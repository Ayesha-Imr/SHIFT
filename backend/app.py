from flask import Flask, request, jsonify
from flask_cors import CORS
from flow_one import run_flow
from flow_two import get_alternatives

app = Flask(__name__)
CORS(app)

@app.route('/analyse', methods=['POST'])
def analyse():
    data = request.json
    url = data.get('url')
    print(url)
    # Perform analysis using the run_flow function
    print(f"Received URL: {url}")
    analysis_result = run_flow(url)
    print(analysis_result)
    return jsonify({"message": "Analysis completed", "result": analysis_result})

@app.route('/alternatives', methods=['POST'])
def alternatives():
    data = request.json
    description = data.get('description')
    print("description received at backend: ", description)
    # Perform alternative fetching using the get_alternatives function
    alternatives_result = get_alternatives(description)
    print(alternatives_result)
    return jsonify({"message": "Alternatives fetched", "alternatives": alternatives_result})

if __name__ == '__main__':
    app.run(debug=True)
