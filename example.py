import os
import json
from dotenv import load_dotenv
load_dotenv()

from self_sensored.self_sensored import SelfSensored

#################
# Parameters
#################
HOST = "http://127.0.0.1"
PORT = 8080
USERNAME = os.environ.get("API_USERNAME")
PASSWORD = os.environ.get("API_PASSWORD")

#################
# Helpers
#################
def pj(data):
    print(json.dumps(data, indent = 2))

#################
# Initialize
#################
ss = SelfSensored(HOST, PORT)

#################
# Login
#################
print("Login:")
pj(ss.login(USERNAME, PASSWORD))
print()

#################
# Add Native Description
#################
data = {
    "platform": "ios",
    "name": "heartRate",
    "datatype": "HKQuantityTypeIdentifier",
    "description": "A quantity sample type that measures the user’s heart rate.",
    "link": "https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/1615138-heartrate?changes=latest_minor",
}
native_description = ss.add_native_descriptor(**data)

print("Native description results:")
pj(native_description)
print()

#################
# Add Native Description
#################
data = {
    "platform": "ios",
    "name": "heartRate",
    "datatype": "HKQuantityTypeIdentifier",
    "description": "A quantity sample type that measures the user’s heart rate.",
    "link": "https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/1615138-heartrate?changes=latest_minor",
}
test = ss.add_native_descriptor(**data)
print()
pj(test)
