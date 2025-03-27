import logging
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from config.logger_config import setup_logger

log_level = logging.DEBUG
log_path = os.path.join(project_root, "test_run.log")
setup_logger(log_level, log_path)
