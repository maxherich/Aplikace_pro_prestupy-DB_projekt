class Prestup:
    def __init__(self,id, hrac_id, kupujici_klub_id, datum, cena):
        self.id = id
        self.hrac_id = hrac_id
        self.kupujici_klub_id = kupujici_klub_id
        self.datum = datum
        self.cena = cena

from database_connection import DatabaseConnection

conn = DatabaseConnection()
cursor = conn.connection.cursor()

class Prestup_Repository:

    def pridat(self, hrac_id, kupujici_klub_id, datum, cena):
        sql = f"CALL nakup_hrace (%s, %s, %s);"
        values = (kupujici_klub_id, hrac_id, cena)
        cursor.execute(sql, values)
        conn.connection.commit()

        sql = f"INSERT INTO prestup (hrac_id, kupujici_klub_id, datum, cena) VALUES (%s, %s, %s, %s)"
        values = (hrac_id, kupujici_klub_id, datum, cena)
        cursor.execute(sql, values)
        conn.connection.commit()

    def vyhledat(self, hrac_id, kupujici_klub_id, datum, cena):
        sql = f"SELECT * FROM prestup WHERE hrac_id = %s AND kupujici_klub_id = %s AND datum = %s AND cena = %s "
        values = (hrac_id, kupujici_klub_id, datum, cena)
        cursor.execute(sql, values)
        conn.connection.commit()
        return cursor.fetch()