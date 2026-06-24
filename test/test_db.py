# test/test_db.py
from app.db.mysql import get_connection


connection = get_connection()

print("Database Connected Successfully", connection)

connection.close()