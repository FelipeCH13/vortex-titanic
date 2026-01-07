import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

## ------------------------------------------1. Carga de datos y limpieza-----------------------------------------
file_path = 'data/train.csv'

##Creacion del DataFrame
df = pd.read_csv(file_path)
# print("Las primeras filas del DataFrame son:")
# print(df.info())
# print(df.head())

## Limpieza del DataFrame
print(df.isnull().sum()) ## Validacion de los nulos
## Nulos identificados en las columnas Age, Cabin y Embarked
mean_age = df['Age'].mean() ## Calculo de la media general de todo el barco
df['Age'] = df['Age'].fillna(mean_age)
df['Cabin'] = df['Cabin'].fillna('Desconocido')
mode_embarked = df['Embarked'].mode()[0]  ## Calculo de la moda de la columna Embarked
df['Embarked'] = df['Embarked'].fillna(mode_embarked)
df['IsChild'] = np.where(df['Age'] < 16, 'Child', 'Adult')

## ----------------------------------------2.Analisis General de Supervivencia----------------------------------------
general_survived = df['Survived'].agg(['mean', 'sum', 'count'])
print(f'De los {general_survived["count"]} pasajeros, {general_survived["sum"]} sobrevivieron, lo que representa una tasa de supervivencia del {general_survived["mean"]*100:.2f}%.')

## ----------------------------------------3. Agrupacion por Genero y Clase----------------------------------------

gen_class_survived = df.groupby('Pclass') ['Survived'].agg(['mean','sum','count']).sort_values(by='mean', ascending=False)
print("Análisis de supervivencia por clase:")
print(gen_class_survived)

gen_sex_class_survived = df.groupby(['Sex','Pclass']) ['Survived'].agg(['mean','sum','count']).sort_values(by='mean', ascending=False)
print("Análisis de supervivencia por género y clase:")
print(gen_sex_class_survived)

gen_age_survived = df.groupby(['Sex','IsChild']) ['Survived'].agg(['mean','sum','count']).sort_values(by='mean', ascending=False)
print("Análisis de supervivencia por género y edad:")
print(gen_age_survived)

gen_class_age_survived = df.groupby(['Sex','IsChild', 'Pclass']) ['Survived'].agg(['mean','sum','count'])
print("Análisis de supervivencia por género, edad y clase:")
print(gen_class_age_survived)


## -----------------------------------------4: Visualización de datos----------------------------------------------------
if not os.path.exists('images'):
    os.makedirs('images')

sns.barplot(x='Sex', y='Survived', data=df)
plt.show() # Esta línea es la que efectivamente "abre" la ventana con el gráfico
plt.savefig('images/supervivencia_genero.png') # Guardamos

## Ejemplo avanzado: Supervivencia por género y clase
# Configuramos el estilo visual
sns.set_theme(style="whitegrid")
# Creamos el gráfico usando 'hue' para separar por Clase
sns.barplot(x='Sex', y='Survived', hue='Pclass', data=df)
# Personalizamos los títulos
plt.title('Supervivencia: Género vs Clase')
plt.ylabel('Tasa de Supervivencia')
plt.show()
plt.savefig('images/supervivencia_genero_clase.png') # Guardamos

# Ejemplo adicional: Gráfico de cajas para edades por clase y supervivencia
plt.figure(figsize=(10, 6))
# Histograma de edades
sns.histplot(data=df, x='Age', kde=True, color='teal')
plt.title('Distribución de Edades en el Titanic')
plt.show()
plt.savefig('images/distribucion_edades.png') # Guardamos

# Gráfico de cajas, mostrando la distribución de edades por clase y supervivencia
sns.catplot(
    data=df, 
    kind="bar",
    x="IsChild", 
    y="Survived", 
    hue="Pclass",
    col="Sex", 
    palette="viridis", 
    alpha=.8, 
    height=5
)

plt.subplots_adjust(top=0.85)
plt.suptitle('Supervivencia: El impacto de la Clase y Edad por Género')
plt.savefig('images/analisis_final_interseccional.png') # Guardamos usando el objeto g
plt.show()