import pytest
import logging

from scripts.sql_query_utils import run_query

pytestmark = pytest.mark.current

def test_sql_connection(db_cursor):
    query = "Select first_name, last_name, phone, address, city from student_information;"
    data = run_query(db_cursor, query)
    logging.info(data)
    assert data[0][0] == "Navdeep"