from flask import Flask, render_template, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

# Load CSV data
csv_file_path = os.path.join(os.path.dirname(__file__), 'chatbot_data.csv')
try:
    chatbot_data = pd.read_csv(csv_file_path)
    print(chatbot_data)  # Print contents to verify it loads correctly
except FileNotFoundError:
    print(f"Error: '{csv_file_path}' not found. Please check the file path.")

# Function to get the response from the chatbot data
def get_response(user_input):
    user_input = user_input.strip().lower()
    print(f"User input: {user_input}")  # Debugging user input

    for _, row in chatbot_data.iterrows():
        print(f"Checking input '{row['input']}' against user input")  # Debugging each row match
        if user_input in row['input'].lower():
            print(f"Match found! Response: {row['response']}")
            return row['response']
    
    print("No match found. Sending default response.")
    return "Sorry, I didn't understand that."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    response = get_response(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
