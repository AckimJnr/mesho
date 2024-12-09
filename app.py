# import os
# from flask import Flask, request
# from send_sms import send_sms

# app = Flask(__name__)

# #TODO: create incoming messages route
# @app.route('/incoming-messages', methods=['POST'])
# def incoming_messages():
#    data = request.get_json(force=True)
#    print(f'Incoming message...\n ${data}')
#    return Response(status=200)


# #TODO: create delivery reports route.

# if __name__ == "__main__":
#     #TODO: Call send message function
    
#     app.run(debug=True, port = os.environ.get("PORT"))

import os
from flask import Flask, request, Response, jsonify
from send_sms import send_sms  # Assuming send_sms is defined in another file

app = Flask(__name__)

# Route to handle incoming messages
@app.route('/incoming-messages', methods=['POST'])
def incoming_messages():
    try:
        data = request.get_json(force=True)  # Parse incoming JSON data
        print(f"Incoming message: {data}")
        # Process the message (e.g., respond to sender or store in DB)
        return Response(status=200)
    except Exception as e:
        print(f"Error handling incoming message: {e}")
        return jsonify({"error": "Failed to process message"}), 500

# Route to handle delivery reports
@app.route('/delivery-reports', methods=['POST'])
def delivery_reports():
    try:
        data = request.get_json(force=True)  # Parse incoming JSON data
        print(f"Delivery report received: {data}")
        # Process the delivery report (e.g., update message status in DB)
        return Response(status=200)
    except Exception as e:
        print(f"Error handling delivery report: {e}")
        return jsonify({"error": "Failed to process delivery report"}), 500

if __name__ == "__main__":
    # Send an SMS message at startup (optional)
    try:
        recipient = os.environ.get("RECIPIENT_PHONE", "+1234567890")  # Replace with a valid default
        message = "This is a test message from the Flask app."
        response = send_sms(recipient, message)  # Call send_sms function
        print(f"SMS sent: {response}")
    except Exception as e:
        print(f"Failed to send SMS at startup: {e}")
    
    # Start the Flask app
    port = int(os.environ.get("PORT", 5000))  # Default to port 5000 if not set
    app.run(debug=True, port=port)
