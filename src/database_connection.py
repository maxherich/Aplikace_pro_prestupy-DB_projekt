import mysql.connector
import json
import os

class DatabaseConnection:
    __instance = None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            try:

                aktutalni_cesta = os.path.dirname(__file__)
                cesta_kongiguracniho_souboru = os.path.join(aktutalni_cesta, '..', 'config', 'config.json')
                if not os.path.exists(cesta_kongiguracniho_souboru):
                    raise FileNotFoundError("Chyba: Konfigurační soubor config.json nebyl nalezen.")
                with open(cesta_kongiguracniho_souboru) as json_file:
                    data = json.load(json_file)
                    cls.connection = mysql.connector.connect(
                        host=data.get("host"),
                        port=data.get("port"),
                        user=data.get("user"),
                        password=data.get("password"),
                        database=data.get("database")
                    )
                    print("Pripojeno.")
            except Exception as e:
                print(e)
        return cls.__instance
