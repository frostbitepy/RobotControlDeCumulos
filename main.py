import pandas as pd
from automation_scripts.sebaot_logging import start_sebaot_application, stop_sebaot_application
from automation_scripts.excel_operations import read_operations_gs, extract_operations
from automation_scripts.imprimir_listado import generar_listado_sebaot
from automation_scripts.calculos import calcular_suma_vigente, calcular_exclusion, calcular_inclusion
from automation_scripts.script_logger import logger



ubicacionOperaciones = "C:/Users/francisco/Desktop/Excel/PlanillaDeOperaciones.xlsx"
ubicacionListado = "C:/Users/francisco/Desktop/Excel/listado.xlsx"

if __name__ == "__main__":
    logger.info("Iniciando script")
    # Start the Sebaot application
    start_sebaot_application()
    logger.info("Sebaot iniciado")

    # Read the operations from the Excel sheet
    new_operations = read_operations_gs(ubicacionOperaciones)
    logger.info("Operaciones leidas")

    # Crear una lista de diccionarios con los datos
    data = []
    # Itera a través de los números de documento en el diccionario:
    for cliente, documento, fecha_nacimiento, operacion, fecha_inicio, fecha_vencimiento, suma_asegurada in zip(new_operations["nombres"], new_operations["nro_documento"], new_operations["fecha_nacimiento"], new_operations["nro_operacion"], new_operations["fecha_inicio"], new_operations["fecha_vencimiento"], new_operations["suma_asegurada"]):
        # Llama a la función generar_listado_sebaot para cada número de documento:
        generar_listado_sebaot(documento)
        logger.info("Listado generado para el cliente: %s", cliente)
        logger.info("Con numero de documento: %s", documento)
        # print("Listado generado para el cliente:", cliente)
        # print("Con numero de documento:", documento)
        listado_operaciones = extract_operations(ubicacionListado)
        monto_vigente = calcular_suma_vigente(fecha_inicio, fecha_vencimiento, listado_operaciones["Poliza"], listado_operaciones["Desde"], listado_operaciones["Hasta"])
        logger.info("Suma vigente: %s", monto_vigente)
        # print("Suma vigente 1: " + str(monto_vigente))
        monto_inclusion = calcular_inclusion(monto_vigente, suma_asegurada)
        monto_exclusion = calcular_exclusion(monto_vigente, suma_asegurada)
        logger.info("Inclusion: %s", monto_inclusion)
        logger.info("Exclusion: %s", monto_exclusion)
        # print("Inclusion 1: " + str(monto_inclusion))
        # print("Exclusion 1: " + str(monto_exclusion))

        # Agregar los datos a la lista de diccionarios
        data.append({
            'Cliente': cliente,
            'Documento': documento,
            'Fecha Nacimiento': fecha_nacimiento,
            'Operacion': operacion,
            'Fecha Inicio': fecha_inicio,
            'Fecha Vencimiento': fecha_vencimiento,
            'Capital Recibido': suma_asegurada,
            'Suma Vigente': monto_vigente,
            'Inclusion': monto_inclusion,
            'Exclusion': monto_exclusion,
        })

    # Crear un DataFrame de Pandas con los datos
    df = pd.DataFrame(data)
    # Guardar el DataFrame en un nuevo archivo Excel
    df.to_excel('C:/Users/francisco/Desktop/Excel/resultado_control.xlsx', index=False)
    logger.info("Archivo de control generado")
        
    stop_sebaot_application()
    logger.info("Sebaot cerrado")    
    logger.info("Script finalizado")

