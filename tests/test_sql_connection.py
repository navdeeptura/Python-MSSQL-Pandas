import logging
import pytest

from scripts.sql_query_utils import run_query

#pytestmark = pytest.mark.current

#@pytest.mark.current
def test_insert_new_student(db_cursor):
    query = """
        INSERT INTO student_information 
        (first_name, last_name, phone, address, city)
        VALUES ('Kulw', 'fixow', '777771117', 'financial drive 2', 'brampton')
        """
    rows_inserted = run_query(db_cursor, query)
    db_cursor.connection.commit()
    logging.info(f"rows_inserted are : {rows_inserted}")
    assert rows_inserted == 1

#@pytest.mark.current
def test_update_table_name(db_cursor):
    query = """
        UPDATE student_information 
        SET 
            phone = '6666666666', 
            address = 'Long Roa222', 
            city = 'Mississauga'
        WHERE (
            first_name = 'NIYA' 
            and last_name = 'TU'
            )"""

    data = run_query(db_cursor, query)
    db_cursor.connection.commit()
    logging.info(data)
    assert data > 0

@pytest.mark.current
def test_delete_from_table(db_cursor):
    query = """DELETE FROM student_information WHERE first_name = 'Kulw'"""
    data = run_query(db_cursor, query)
    logging.info(f"Number of rows deleted: '{data}'")
    assert data == 1

@pytest.mark.current
def test_sql_connection(db_cursor):
    query = "SELECT id, first_name, last_name, phone, address, city FROM student_information;"
    #logging.info(query)
    data = run_query(db_cursor, query, "dict")
    for row in data:
        logging.info(row)
    assert data[0]["first_name"] == "Navdeep"



