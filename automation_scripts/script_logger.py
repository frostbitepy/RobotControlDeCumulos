import logging

# Create a logger object
logger = logging.getLogger(__name__)

# Configure the logger
logger.setLevel(logging.INFO)

# Create a file handler and set the log level
file_handler = logging.FileHandler('script_log.log')
file_handler.setLevel(logging.INFO)

# Create a formatter and attach it to the handler
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(file_handler)