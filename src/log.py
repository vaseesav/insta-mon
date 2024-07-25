"""Module provides logging functionality."""

import logging
import logging.config
import yaml


def setup_logging(path='src/logging_config.yaml'):
    """Configures the logging module."""
    with open(path, 'r') as file:
        logging_config = yaml.safe_load(file)
        logging.config.dictConfig(logging_config)


setup_logging()
logger = logging.getLogger(__name__)
