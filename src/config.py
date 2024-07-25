"""Module providing access to the configuration file."""
import logging
from typing import Optional

from path import Path
from strictyaml import load, Map, Int, Str

from src import log

# Setup logging
log.setup_logging()
logger = logging.getLogger(__name__)

# YAML validation schema for the config.yaml
schema = Map({
    "instamon": Map({
        "database": Str(),
        "scrap_interval": Int(),
        "timeout_sec": Int()
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
parsed_config = load_config('src/config.yaml')

# Providing getter access to the configuration file
config = {
    'SCRAP_INTERVAL':
        parsed_config['instamon']['scrap_interval'],
    'DB_SQ3_FILE':
        parsed_config['instamon']['database'],
    'TIMEOUT_SEC':
        parsed_config['instamon']['timeout_sec'],
}

"""Lambda getter expression to access the configuration file values."""
get = lambda keyname: config[keyname]
