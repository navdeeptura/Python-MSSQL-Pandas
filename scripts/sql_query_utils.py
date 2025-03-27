import logging
import pandas as pd
import json

from sqlalchemy.dialects.mssql.information_schema import columns


def run_query(cursor, query, as_format=None, params=None):
    """
    Execute a SQL query and return results in the desired format.

    Parameters:
        cursor: pyodbc cursor object
        query (str): SQL query
        params (tuple or list): query parameters (optional)
        as_format (str or None): 'dict', 'df', 'json', or None for raw fetchall

    Returns:
        Depends on as_format:
            - None → list of tuples from fetchall()
            - 'dict' → list of dicts
            - 'df' → pandas DataFrame
            - 'json' → JSON string
    """

    logging.info(f"Executing SQL query: {query}")

    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        if query.strip().lower().startswith("select"):
            rows = cursor.fetchall()

            if as_format is None:
                return rows

            columns = [col[0] for col in cursor.description]
            result = [dict(zip(columns, row)) for row in rows]

            if as_format == "dict":
                return result
            elif as_format == "df":
                return pd.DataFrame(result)
            elif as_format == "json":
                return json.dumps(result, default=str, indent=2)
            else:
                raise ValueError(f"Unsupported format: {as_format}")

        else:
            # For INSERT/UPDATE/DELETE: return affected row count
            return cursor.rowcount

    except Exception as e:
        logging.error(f"Query failed: {e}")
        raise