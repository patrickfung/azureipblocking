# Define imports
import msal
import requests
import json

# Enter the details of your AAD app registration
client_id = '<Your Client ID>'
client_secret = '<Your Client Secret>'
authority = 'https://login.microsoftonline.com/<Tenant ID>'
scope = ['https://graph.microsoft.com/.default']

# Create an MSAL instance providing the client_id, authority and client_credential parameters
client = msal.ConfidentialClientApplication(client_id, authority=authority, client_credential=client_secret)

# First, try to lookup an access token in cache
token_result = client.acquire_token_silent(scope, account=None)

# If the token is available in cache, save it to a variable
if token_result:
  access_token = 'Bearer ' + token_result['access_token']
  print('Access token was loaded from cache')

# If the token is not available in cache, acquire a new one from Azure AD and save it to a variable
if not token_result:
  token_result = client.acquire_token_for_client(scopes=scope)
  access_token = 'Bearer ' + token_result['access_token']
  print('New access token was acquired from Azure AD')

#print(access_token)

url = 'https://graph.microsoft.com/v1.0/identity/conditionalAccess/namedLocations/<Name Location ID>'
headers = {
  'Authorization': access_token
}
headers["Content-Type"] = "application/json"

# Make a GET request to the provided url, passing the access token in a header
graph_result = requests.get(url=url, headers=headers)

# Print the results in a JSON format
print(graph_result.json())

jsonFile = open('dataset.json', 'r')

json_data = json.load(jsonFile)

print(json_data['ipRanges'])

# Making a PATCH request
resp = requests.patch(url=url, headers=headers, data=json.dumps(json_data))

# check status code for response received
# success code - 200
print(resp)

# print content of request
print(resp.status_code)

jsonFile.close()
