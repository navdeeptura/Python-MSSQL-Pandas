import logging

def run_query(cursor, query, params=None):
    logging.info(f"Executing SQL query: {query}")

    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        logging.error(f"Query failed: {e}")
        raise