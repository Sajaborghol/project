import mysql.connector


def get_database_connection():
    db= mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        passwd="Sb241203@",
        database="new_schema"
    )
    return db, db.cursor()