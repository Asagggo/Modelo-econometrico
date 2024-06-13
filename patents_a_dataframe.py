import pandas as pd

# Leer el archivo Excel original
archivo_entrada = r'C:\Users\adria\Downloads\Data modelo tesis\Anual\Por grupo\OECD AyB\Patents Related to IA\Patentes con etiqueta WDB (nofiltered).xlsx'  # Ruta archivo
df = pd.read_excel(archivo_entrada)

# Transformar la tabla
df_transformado = df.melt(id_vars=['country'], var_name='times', value_name='Patentes')

# Asegurarse de que los datos están en el orden correcto
df_transformado = df_transformado.sort_values(by=['country', 'times'])

# Guardar el nuevo archivo Excel
archivo_salida = 'archivo_transformado.xlsx'  # Nombre del nuevo archivo Excel
df_transformado.to_excel(archivo_salida, index=False)
