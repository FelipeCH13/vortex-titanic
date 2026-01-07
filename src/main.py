## Importar Librerías Necesarias
import csv

## Definir la ruta del archivo
file_path = 'data/train.csv'

## Abrir el archivo en modo lectura
## R, indica el modo en el que estamos abriendo el archivo (Read)
## El encoding es para asegurarnos que los caracteres especiales se lean correctamente
with open(file_path,'r', encoding = "utf-8") as file:

    #------------------------------------------Problema 1: Identificar Cabecera----------------------------------------------------
    ## Leer el encabezado
    ## La función readLine() lee una línea completa del archivo
    ## La función strip() elimina espacios en blanco al inicio y al final de la cadena
    cabecera = file.readline().strip()
    print("Las columnas disponibles en el registro de pasajeros es:")
    print(cabecera)

    ## Transformando el contenido en Listas
    columns_list = cabecera.split(',')
    print(columns_list)
    ## Identificando el indice de Survived
    ## La función index() devuelve el índice de la primera aparición del valor especificado
    survived_index = columns_list.index('Survived')
    print(survived_index)

    #------------------------------------------Problema 2: Contar Sobrevivientes----------------------------------------------------
    sobrevientes = 0
    iterador = 0
    for iterador in range(10):
        ## Leer cada línea del archivo
        linea = file.readline().strip()
        ## Dividir la línea en una lista de valores utilizando la coma como separador
        valores = linea.split(',')
        if valores[survived_index] == '1':
            sobrevientes += 1

    print(f'En las primeras {iterador + 1} filas, hubo {sobrevientes} sobrevientes.')

    #------------------------------------------Problema 3: Uso de librerias ----------------------------------------------------
    csv_reader = csv.reader(file)
    # Next para leer la primera línea del archivo CSV (la cabecera)
    cabecera_csv = next(csv_reader)

    sobrevientes_csv = 0
    sobrevivientes_hombres = 0
    sobrevivientes_mujeres = 0
    sobrevivientes_ninos = 0
    total_ninos = 0
    for fila in csv_reader:
        if fila[columns_list.index('Survived')] == '1':
            sobrevientes_csv += 1
            if fila[columns_list.index('Sex')] == 'female':
                sobrevivientes_mujeres += 1
            else:
                sobrevivientes_hombres += 1
            ##Niños sobrevivientes
            if fila[columns_list.index('Age')] != '' and float(fila[columns_list.index('Age')]) < 18:
                sobrevivientes_ninos += 1
        if fila[columns_list.index('Age')] != '' and float(fila[columns_list.index('Age')]) < 18:
                total_ninos += 1
    print(f'Usando la libreria CSV, el total de sobrevivientes es: {sobrevientes_csv}')
    print(f'Total de sobrevivientes mujeres: {sobrevivientes_mujeres}')
    print(f'Total de sobrevivientes hombres: {sobrevivientes_hombres}')
    print(f'Total de sobrevivientes niños: {sobrevivientes_ninos}')
    print(f'Total de niños en el dataset: {total_ninos}')

    if total_ninos > 0:
        percent_survived_children = (sobrevivientes_ninos / total_ninos) * 100
        print(f'Porcentaje de niños que sobrevivieron: {percent_survived_children:.2f}%')
    else:
        print('No hay datos de niños en el dataset.')