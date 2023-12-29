from dapnet_api import DapnetApiClient

# Beispielverwendung der SendDAPNET Methode
response = DapnetApiClient.SendDAPNET('Testnachricht', 'destinationcallsign', 'txgroup', 'yourcallsign', 'yourpassword')
print(response)
