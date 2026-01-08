import mysql.connector
import json

class DatabaseConnection:
    __instance = None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            try:
                with open("config.json") as json_file:
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
