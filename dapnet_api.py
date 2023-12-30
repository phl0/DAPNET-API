# Autor: Erik Schauer, DO1FFE, do1ffe@darc.de
# Programmname: DAPNET API Client mit Send Methode
# Erstelldatum: 29. Dezember 2023

import requests

class DAPNET:
    """
    Diese Klasse implementiert einen Client für die DAPNET API.
    Sie ermöglicht das Senden von Nachrichten über das DAPNET-Netzwerk.
    """

    def __init__(self, callsign, password, url='http://dapnet.db0sda.ampr.org:8080/calls'):
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
        response = requests.post(self.url, headers=self.headers, auth=(self.callsign, self.password), json=data)
        return response

    @staticmethod
    def Send(message, to_callsign, transmitter_group, my_dapnet_callsign, my_dapnet_password):
        """
        Statische Methode zur Vereinfachung des Nachrichtenversands über DAPNET.

        :param message: Der Inhalt der Nachricht.
        :param to_callsign: Das Zielrufzeichen oder eine Liste von Zielrufzeichen.
        :param transmitter_group: Die Transmittergruppe oder eine Liste von Transmittergruppen.
        :param my_dapnet_callsign: Das eigene Rufzeichen für die Authentifizierung.
        :param my_dapnet_password: Das Passwort für die Authentifizierung.
        :return: Das Response-Objekt der HTTP-Anfrage.
        """
        client = DAPNET(my_dapnet_callsign, my_dapnet_password)
        return client.send_message(message, to_callsign, transmitter_group)
