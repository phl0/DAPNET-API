# Autor: Erik Schauer, DO1FFE, do1ffe@darc.de
# Programmname: DAPNET API Client mit Send Methode
# Erstelldatum: 29. Dezember 2023

import requests
from requests.auth import HTTPBasicAuth

class DAPNET:
    """
    Diese Klasse implementiert einen Client für die DAPNET API.
    Sie ermöglicht das Senden von Nachrichten über das DAPNET-Netzwerk.
    """

    def __init__(self, callsign, password, url='https://hampager.de/api/calls'):
        self.callsign = callsign
        self.password = password
        self.url = url
        self.headers = {'Content-type': 'application/json'}

    def send_message(self, message, destination_callsign, tx_group, emergency=False):
        data = {
            "text": message,
            "callSignNames": [destination_callsign] if isinstance(destination_callsign, str) else destination_callsign,
            "transmitterGroupNames": [tx_group] if isinstance(tx_group, str) else tx_group,
            "emergency": emergency
        }
        response = requests.post(self.url, headers=self.headers, auth=HTTPBasicAuth(self.callsign, self.password), json=data)
        return response

    def log_message(self, message, destination_callsign, transmitter_group, emergency=False):
        """
        Sendet eine Logging-Nachricht über das DAPNET-Netzwerk.

        :param message: Der Inhalt der Nachricht.
        :param destination_callsign: Das Zielrufzeichen für die Nachricht.
        :param transmitter_group: Die Transmittergruppe für die Nachricht.
        :param emergency: Notfall-Flag (Standard False).
        :return: Das Response-Objekt der HTTP-Anfrage.
        """
        return self.send_message(message, destination_callsign, transmitter_group, emergency)
