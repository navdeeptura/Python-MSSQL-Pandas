import logging
import sys
import os

import pytest

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from config.logger_config import setup_logger
from config.db_config import get_db_settings
from scripts.db_connection import get_connection

@pytest.fixture(scope="session", autouse=True)
def configure_logging():
    log_level = logging.DEBUG
    log_path = os.path.join(project_root, "test_run.log")

    # Clean the log file before tests begin
    open(log_path, 'w').close()

    setup_logger(log_level, log_path)
    logging.info("Logger initialized for test run.")

@pytest.fixture(scope="session")
def db_settings():
    db_config_path = os.path.join(project_root, "config", "db_config.ini")
    return get_db_settings(db_config_path)

@pytest.fixture(scope="session")
def db_conn(db_settings):
    conn = get_connection(db_settings)
    yield conn
    conn.close()

@pytest.fixture
def db_cursor(db_conn):
    cursor = db_conn.cursor()
    try:
        yield cursor
    finally:
        cursor.close()

@pytest.fixture(autouse=True)
def log_test_seperator(request):
    test_name = request.node.name.upper()
    separator = "=" * 120

    logging.info(separator)
    logging.info(f"Starting Test : '{test_name}'")
    yield
    logging.info(f"Finished Test: '{test_name}'")
    logging.info(separator)






