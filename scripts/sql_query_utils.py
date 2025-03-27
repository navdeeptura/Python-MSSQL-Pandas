import logging
import pyodbc

from tests.conftest import db_settings

def run_query(cursor, query, params=None):
    logging.info(f"Executing SQL query: {query}")
    cursor.close() #cleaning SQL query

    cursor = cursor.connection.cursor() #fresh cursor

    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)

    return cursor.fetchall()