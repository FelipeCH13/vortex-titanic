import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

## Directorio del archivo CSV
file_path = 'data/train.csv'

##Creacion del DataFrame
df = pd.read_csv(file_path)
print("Las primeras filas del DataFrame son:")
## print(df.head())

##------------------------------------------Problema 1: Aplicar filtros----------------------------------------------------

mujeres = df[df['Sex'] == 'female']
mujeres_sobrevivientes = mujeres[mujeres['Survived'] == 1]
print (f'Número de mujeres sobrevivientes: {len(mujeres_sobrevivientes)}')

# Filtramos por sexo Y por supervivencia al mismo tiempo
sobrevivientes_f = df[(df['Sex'] == 'female') & (df['Survived'] == 1)]
print(len(sobrevivientes_f))

# Número total de pasajeros (hombres y mujeres) que eran de Primera Clase
ejercicio_1 = df[(df['Pclass'] == 1) & (df['Survived'] == 1)]
print(f'Número de pasajeros de primera clase que sobrevivieron: {len(ejercicio_1)}')


##------------------------------------------Problema 2: Calcular la tasa de supervivencia por genero----------------------------------------------------
# Ejemplo agrupacion
# Agrupamos por clase y sumamos la columna de sobrevivientes
sobrevivientes_por_clase = df.groupby('Pclass')['Survived'].sum()
print(sobrevivientes_por_clase)

tasa_supervivencia_genero = df.groupby('Sex')['Survived'].mean() * 100
print(f"Tasa de supervivencia por género: \n{tasa_supervivencia_genero}")

## Utilizando agrupamiento multinivel
## Mean calcula el promedio de la columna Survived para cada grupo
## Sort_values ordena los resultados en orden descendente
tasa_supervivencia_genero_class = df.groupby(['Sex','Pclass'])['Survived'].mean().sort_values(ascending=False) * 100
print(f"Tasa de supervivencia por : \n{tasa_supervivencia_genero_class.round(2)}")

# Agrupamos y pedimos promedio y conteo
analisis = df.groupby(['Sex', 'Pclass'])['Survived'].agg(['mean', 'count', 'sum'])
print(analisis)

# Cuenta cuántos valores nulos hay en cada columna
# Isnull devuelve un DataFrame de booleanos indicando si cada valor es nulo
print(df.isnull().sum())

edad_promedio_por_genero = df.groupby('Sex')['Age'].mean()
print(f'Edad promedio por género: \n{edad_promedio_por_genero.round(2)}')

## Lo que hace Dropna es eliminar las filas que tienen valores nulos en la columna Age
df_cleaned = df.dropna(subset=['Age'])
edad_promedio_por_genero_cleaned = df_cleaned.groupby('Sex')['Age'].mean()
print(f'Edad promedio por género (sin valores nulos): \n{edad_promedio_por_genero_cleaned.round(2)}')

##-----------------------------------------Ejemplo de imputación de datos nulos----------------------------------------------------
# 1. Calculamos la media general de todo el barco
media_total = df['Age'].mean()

# 2. Creamos una copia y rellenamos los nulos
## Copy crea una copia del DataFrame original para no modificarlo directamente
df_imputed = df.copy()
# Se selecciona la columna 'Age' y se rellenan los valores nulos con la media total calculada
# Fillna rellena los valores nulos con el valor especificado
df_imputed['Age'] = df_imputed['Age'].fillna(media_total)

# 3. Calculamos el promedio por género con los datos rellenados
edad_promedio_imputed = df_imputed.groupby('Sex')['Age'].mean()
print(f'Edad promedio con nulos rellenados: \n{edad_promedio_imputed.round(2)}')

##------------------------------------------Problema 3: Visualización de datos----------------------------------------------------
# sns.barplot(x='Sex', y='Survived', data=df)
# plt.show() # Esta línea es la que efectivamente "abre" la ventana con el gráfico

## Ejemplo avanzado: Supervivencia por género y clase
# Configuramos el estilo visual
sns.set_theme(style="whitegrid")

# Creamos el gráfico usando 'hue' para separar por Clase
sns.barplot(x='Sex', y='Survived', hue='Pclass', data=df)

# Personalizamos los títulos
plt.title('Supervivencia: Género vs Clase')
plt.ylabel('Tasa de Supervivencia')
plt.show()

# Ejemplo adicional: Gráfico de cajas para edades por clase y supervivencia
plt.figure(figsize=(10, 6))
# Histograma de edades
sns.histplot(data=df, x='Age', kde=True, color='teal')
plt.title('Distribución de Edades en el Titanic')
plt.show()