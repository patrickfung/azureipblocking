#Import Library

import json
import ipaddress

#Function
#Function 1 - IP Validation#
from ipaddress import ip_address, IPv4Address

def validIPAddress(IP: str) -> str:
    try:
        return "IPv4" if type(ip_address(IP)) is IPv4Address else "IPv6"
    except ValueError:
        return "Invalid"

#Function 2 - Json Update#
def write_json(new_data, filename='dataset.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["ipRanges"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

#Main Program#

#Check Existing Data Set#
jsonFile = open('dataset.json')

json_data = json.load(jsonFile)

print(json_data['ipRanges'])

jsonFile.close()

#Read th file#

myfile = open("sourceip.txt", "r")
myline = myfile.readline()
while myline:
   myline = myline.strip()
   actionflag = '1'
   #IP Validation#
   if (validIPAddress(myline)) == 'IPv4':
     print('New IPv4 address to process...')
     sourceip = myline + '/32'
   elif (validIPAddress(myline)) == 'IPv6':
     print('New IPv6 address to process..')
     sourceip = myline + '/64'
   else:
     print('No new IP or wrong IP information. Action suspended.')
     sourceip = 'FAULT'
   print(myline)
   #Data Checking#
   if sourceip != 'FAULT':
      check_value = {"@odata.type": "#microsoft.graph.iPv4CidrRange","cidrAddress": sourceip}
      if check_value in json_data['ipRanges']:
        print('IP value is in existing JSON Dataset. Action suspended.')
        actionflag = '0'
   newdata = {"@odata.type": "#microsoft.graph.iPv4CidrRange",
              "cidrAddress": sourceip
              }
   #Update the JSON Data Set
   if actionflag == '1' and sourceip != 'FAULT':
     write_json(newdata)
     print('Action Done')
   else:
     print('Action Suspended')
   myline = myfile.readline()
myfile.close()

open("sourceip.txt", "w").close()