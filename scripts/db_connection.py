import pyodbc

def get_connection(db_settings):
    connection_string = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={db_settings['server']};"
        f"DATABASE={db_settings['database']};"
        f"UID={db_settings['user']};"
        f"PWD={db_settings['password']};"
    )
    return pyodbc.connect(connection_string)