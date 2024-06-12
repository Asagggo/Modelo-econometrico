import pandas as pd
import numpy as np

# Cargar el archivo de Excel
file_path = r'C:\Users\adria\Downloads\Data modelo tesis\Anual\Por grupo\OECD A y B\Patents Related to IA\Análisis de patentes por país.xlsx'
data = pd.read_excel(file_path)

# Calcular el total de patentes por país sumando las columnas de años
data['total_patents'] = data.iloc[:, 1:].sum(axis=1)

# Calcular la media y la desviación estándar
mean_patents = data['total_patents'].mean()
std_dev_patents = data['total_patents'].std()

# Definir los límites para detectar outliers
lower_limit = mean_patents - 2 * std_dev_patents
upper_limit = mean_patents + 2 * std_dev_patents

# Identificar outliers
outliers = data[(data['total_patents'] < lower_limit) | (data['total_patents'] > upper_limit)]

# Calcular el valor mínimo de patentes para incluir un país
min_patents_inclusion = lower_limit

# Guardar los resultados en un nuevo archivo de Excel
with pd.ExcelWriter('Análisis_de_patentes_resultados.xlsx') as writer:
    data.to_excel(writer, sheet_name='Patentes por país', index=False)
    outliers.to_excel(writer, sheet_name='Outliers', index=False)
    pd.DataFrame({'Media': [mean_patents], 'Desviación estándar': [std_dev_patents], 
                  'Límite inferior': [lower_limit], 'Límite superior': [upper_limit], 
                  'Mínimo para inclusión': [min_patents_inclusion]}).to_excel(writer, sheet_name='Estadísticas', index=False)

print(f"Media: {mean_patents}")
print(f"Desviación estándar: {std_dev_patents}")
print(f"Límite inferior: {lower_limit}")
print(f"Límite superior: {upper_limit}")
print(f"Mínimo para inclusión: {min_patents_inclusion}")
print(f"Outliers: {outliers['country'].tolist()}")

