from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/display_value', methods=['POST'])
def display_value():
    try:
        # Get the displayed data from the form
        displayed_data = request.get_data()

        # Now you can do something with the displayed data
        print("Received display data:", displayed_data.decode('utf-8'))  # Assuming it's UTF-8 encoded data

        # You can perform additional processing or analysis on the data if needed

        return jsonify({"message": "Display data received successfully"})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True, port=5001)
