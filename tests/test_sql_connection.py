import pytest
import pyodbc
import logging
from tests.conftest import db_settings

pytestmark = pytest.mark.current

def test_sql_connection(db_cursor):
    db_cursor.execute(
        "Select first_name, last_name, phone, address, city from student_information;")
    data = db_cursor.fetchall()
    logging.info(data)
    assert data[0][0] == "Navdeep"

