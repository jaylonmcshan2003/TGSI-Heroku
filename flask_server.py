from flask import Flask, request, jsonify
from flask_cors import CORS
from pyBotScript import fill_out_form
app = Flask(__name__)
CORS(app, supports_credentials=True, allow_headers=["Content-Type"])

@app.after_request
def add_cors_headers(response):
    # Add CORS headers
    #response.headers['Access-Control-Allow-Origin'] = 'https://123gosolution.lightning.force.com'
    print("Adding CORS headers...")
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Methods'] = 'GET,HEAD,OPTIONS,POST,PUT'
    response.headers['Access-Control-Allow-Headers'] = 'Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers'
    print("Headers added successfully:", response.headers)
    response.headers['Content-Security-Policy'] = "connect-src 'self' http://10.10.0.238:5000"


    #response.headers['Content-Security-Policy'] = "connect-src 'self' http://10.10.0.238:5000"
    
    return response

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS'])
def handle_post_request():
    try:
        # Receive the POST request datawh
        data = request.json
        
        # Extract customer information from the POST request data
        firstName = data.get('firstName')
        lastName = data.get('lastName')
        mailingStreet = data.get('mailingStreet')
        mailingCity = data.get('mailingCity')
        mailingPostalCode = data.get('mailingPostalCode')
        contactId = data.get('contactId')
        print(contactId)
        
        # Call the fill_out_form function with extracted customer information
        fill_out_form(firstName, lastName, mailingStreet, mailingCity, mailingPostalCode, contactId)
        # Perform any necessary processing or forwarding here
        return jsonify(success=True)
    except Exception as e:
        print("An error occurred:", e)
        return jsonify(success=False, error=str(e))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    #app.run(port=5000)
    #app.run(debug=True, ssl_context='adhoc', port=5000)