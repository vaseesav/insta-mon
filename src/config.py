"""Module providing access to the configuration file."""
import logging
from typing import Optional

from path import Path
from strictyaml import load, Map, Int

from src import log

# Setup logging
log.setup_logging()
logger = logging.getLogger(__name__)

# YAML validation schema for the config.yaml
schema = Map({
    "instamon": Map({
        "scrap_interval": Int()
    })
})


def load_config(file_path: str) -> Optional[dict]:
    """
    Load and validate the configuration file.

    Args:
        file_path (str): Path to the configuration file.

    Returns:
        dict: Validated (against the schema) configuration.
    """
    try:
        config_file_string = Path(file_path).read_text()
        parsed_config_file = load(yaml_string=config_file_string, schema=schema).data
        return parsed_config_file
    except RuntimeError as runtime_error:
        logger.critical('Failed to load or parse the configuration file: %s', runtime_error)
        return None


# Load the configuration file
parsed_config = load_config('config.yaml')

# Providing getter access to the configuration file
config = {
    'URLS':
        parsed_config['instamon']['scrap_interval']}

"""Lambda getter expression to access the configuration file values."""
get = lambda keyname: config[keyname]
