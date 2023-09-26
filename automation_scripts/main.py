from sebaot_logging import start_sebaot_application
from excel_extract_operations import read_operations_gs
from imprimir_listado import generar_listado_sebaot


ubicacionOperaciones = "C:/Users/francisco/Desktop/Excel/PlanillaDeOperaciones.xlsx"

if __name__ == "__main__":
    # Start the Sebaot application
    start_sebaot_application()

    # Read the operations from the Excel sheet
    operations = read_operations_gs(ubicacionOperaciones)

    # Itera a través de los números de documento en el diccionario:
    for documento in operations["nro_documento"]:
        # Llama a la función generar_listado_sebaot para cada número de documento:
        generar_listado_sebaot(documento)


