class Klub:
    def __init__(self,id, nazev, liga_id, majitel_id):
        self.id = id
        self.nazev = nazev
        self.liga_id = liga_id
        self.majitel_id = majitel_id

import csv
from database_connection import DatabaseConnection

conn = DatabaseConnection()
cursor = conn.connection.cursor()

class Klub_Repository:

    def pridat(self, nazev, liga_id, majitel_id):
        sql = f"INSERT INTO klub (nazev, liga_id, majitel_id) VALUES (%s, %s, %s)"
        values = (nazev, liga_id, majitel_id)
        cursor.execute(sql, values)
        conn.connection.commit()

    def smazat(self, nazev):
        sql = f"DELETE FROM klub WHERE nazev = %s"
        values = (nazev,)
        cursor.execute(sql, values)
        conn.connection.commit()

    def seznam_klubu(self):
        sql = f"SELECT * FROM klub"
        cursor.execute(sql)
        return cursor.fetchall()

    def import_z_csv(self, cesta_k_souboru):
        with open(cesta_k_souboru, "r", encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader, None)
            for row in reader:
                self.pridat(row[0], row[1], row[2])