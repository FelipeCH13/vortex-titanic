# 🚢 Análisis de Supervivencia: El Desastre del Titanic

## 📖 Descripción
Este proyecto realiza un **Análisis Exploratorio de Datos (EDA)** sobre el conjunto de datos histórico del Titanic. El objetivo es identificar los factores determinantes que influyeron en la probabilidad de supervivencia de los pasajeros, aplicando técnicas de limpieza de datos, imputación estadística y visualización avanzada con Python.

## 🛠️ Tecnologías Utilizadas
* **Python 3.x**
* **Pandas:** Manipulación y limpieza de datos.
* **Matplotlib & Seaborn:** Visualización de datos estadística.
* **Numpy:** Operaciones lógicas y tratamiento de nulos.

## 🧼 Limpieza y Estandarización
Para asegurar la integridad del análisis, se realizaron los siguientes ajustes:
1. **Edad (`Age`):** Presentaba un **19.8% de nulos**. Se aplicó imputación por la **media** para preservar el volumen de la muestra (891 registros).
2. **Cabina (`Cabin`):** Con un **77% de nulos**, se creó la categoría **"Desconocido"** para no perder información del resto de las columnas.
3. **Embarque (`Embarked`):** Los 2 nulos se reemplazaron por la **moda**, completando el set de datos.

## 📊 Preguntas de Negocio y Hallazgos

### 1. ¿Cuál fue la tasa general de supervivencia?
De los 891 pasajeros registrados, solo el **38.38%** sobrevivió (**342 personas**).

### 2. ¿El nivel socioeconómico influyó en la posibilidad de rescate?
| Clase | Tasa de Supervivencia |
| :--- | :--- |
| **1ª Clase** | **62%** |
| **2ª Clase** | **47%** |
| **3ª Clase** | **24%** |

### 3. ¿Realmente se cumplió la política de "mujeres y niños primero"?
* **Mujeres:** Supervivencia del **75%** (adultas) y **67%** (niñas).
* **Hombres:** Supervivencia del **16%** (adultos) y **43%** (niños).

### 4. ¿Existe una intersección crítica entre género y clase social?
Las mujeres de **3ª clase** presentaron la tasa más baja de su género (**50%**), mientras que los hombres de **2ª y 3ª clase** representaron el segmento con menor probabilidad de supervivencia de todo el barco.

> ### 🚨 El Mito del Protocolo Universal
> Mientras que los niños de 1ª y 2ª clase fueron rescatados en su **100%**, los niños de 3ª clase tuvieron una tasa de apenas el **32%**. Esto demuestra que la clase social fue un filtro más potente que la edad.

---

## 🚀 Cómo ejecutar el proyecto
1. Clona este repositorio:
   ```bash
   git clone [https://github.com/tu-usuario/titanic-analysis.git](https://github.com/tu-usuario/titanic-analysis.git)