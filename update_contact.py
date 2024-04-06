import logging
import requests
from simple_salesforce import Salesforce
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# USERNAME = "programmers@thegosolution.com.jaylonm"
# PASSWORD = "Violin##19"
# SECURITY_TOKEN = "XbAmo2VRTxDx3HpKm6mqHtf1"
# CONSUMER_KEY = "3MVG9KshNav2_JdrizuvezzTlzjv11Vy7JV9wX3DUp1ReycdB_ExmcQSUf58SxxTqm.rlnXrTVCFWD.uUlIgE"
# CONSUMER_SECRET = "5747F63AE7EE2E7003CCA19F70EB2E56B9E5AF1CDCB5149D8910433C411BAD1B"

# # Authenticate with Salesforce
# sf = Salesforce(
#     username=USERNAME,
#     password=PASSWORD,
#     security_token=SECURITY_TOKEN,
#     consumer_key=CONSUMER_KEY,
#     consumer_secret=CONSUMER_SECRET,
#     domain='test'  # Change to your Salesforce domain if not using a sandbox
# )

USERNAME = "jaylon.mcshan@thegosolution.com"
PASSWORD = "Violin##19"
SECURITY_TOKEN = "DhGl3GfatCRMyrbb7Ou8sNUQW"
CONSUMER_KEY = "3MVG9KsVczVNcM8yQQIoTGjDxF_EUO1sPlgFDIrwAxyZCSqRt0WTtliVfkvCtSsVIPtU0Uy1NEBop5oxvjYeN"
CONSUMER_SECRET = "2AACFB7BCAE1265ECFDFCF4087B58556D5286511578AC14A1DE0FC872BA47169"

# Authenticate with Salesforce
sf = Salesforce(
        username=USERNAME,
        password=PASSWORD,
        security_token=SECURITY_TOKEN,
        client_id=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET,
        domain='login'
    )

def update_contact(dl_number, contactId):
    try:
        # Update the contact record with the new DL number
        data = {
            "TGS_Drivers_License_Number__c": dl_number
        }

        print("Updating contact with data:", data)
        result = sf.Contact.update(contactId, data)
        print("API Response:", result)
        
        if result == True:
            print("Contact record updated successfully")
            return True
        else:
            print("Failed to update contact record. Result:", result)
            return False
    except Exception as e:
        print("An error occurred during contact update:", str(e))
        return False
