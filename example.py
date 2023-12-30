from dapnet_api import DAPNET

# Beispielverwendung der Send Methode
response = DAPNET.Send('Testnachricht', 'destinationcallsign', 'txgroup', 'yourcallsign', 'yourpassword')
print(response)
