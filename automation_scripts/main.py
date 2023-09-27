from sebaot_logging import start_sebaot_application
from excel_extract_operations import read_operations_gs, extract_operations
from imprimir_listado import generar_listado_sebaot
from calculos import calcular_suma_vigente


ubicacionOperaciones = "C:/Users/francisco/Desktop/Excel/PlanillaDeOperaciones.xlsx"
ubicacionListado = "C:/Users/francisco/Desktop/Excel/listado.xlsx"

if __name__ == "__main__":
    # Start the Sebaot application
    start_sebaot_application()

    # Read the operations from the Excel sheet
    new_operations = read_operations_gs(ubicacionOperaciones)

    # Itera a través de los números de documento en el diccionario:
    for documento, fecha_inicio, fecha_vencimiento, suma_asegurada in zip(new_operations["nro_documento"], new_operations["fecha_inicio"], new_operations["fecha_vencimiento"], new_operations["suma_asegurada"]):
        # Llama a la función generar_listado_sebaot para cada número de documento:
        generar_listado_sebaot(documento)
        print("Listado generado para el documento:", documento)
        listado_operaciones = extract_operations(ubicacionListado)
        monto_vigente = calcular_suma_vigente(fecha_inicio, fecha_vencimiento, suma_asegurada, listado_operaciones["Desde"], listado_operaciones["Hasta"])
        print(monto_vigente)


