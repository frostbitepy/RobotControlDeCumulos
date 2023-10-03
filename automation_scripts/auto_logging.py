import logging

# Configura la configuración de registro
logging.basicConfig(filename='mi_programa.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_function_call(func):
    """
    Decorador que registra la llamada a una función.
    """
    def wrapper(*args, **kwargs):
        function_name = func.__name__
        logging.info(f"Llamando a la función: {function_name}")
        result = func(*args, **kwargs)
        logging.info(f"Función {function_name} completada")
        return result
    return wrapper

def log_event(event_description):
    """
    Registra un evento personalizado.
    """
    logging.info(event_description)

def log_error(error_description):
    """
    Registra un mensaje de error.
    """
    logging.error(error_description)