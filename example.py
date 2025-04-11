from dapnet_api import DAPNET

client = DAPNET('callsign', 'password')

# Beispielverwendung der Send Methode
try:
    response = client.send_message('messagecontent', 'destination-callsign', 'transmitter-group')
except:
    print(response)
