import pandas as pd

# Cargar los datos de los archivos de Excel
df1 = pd.read_excel(r'C:\Users\adria\Downloads\Data modelo tesis\Anual\Por grupo\WDB AyB\WorkingVariablesDataframe.xlsx')
df2 = pd.read_excel(r'C:\Users\adria\Downloads\Data modelo tesis\Anual\Por grupo\OECD AyB\Patents Related to IA\WorkingPatentesDataframe.xlsx')

# que las columnas 'country' y 'time' sean de tipo string para evitar problemas de coincidencia
df1['country'] = df1['country'].astype(str)
df1['time'] = df1['time'].astype(str)
df2['country'] = df2['country'].astype(str)
df2['time'] = df2['time'].astype(str)

# Combinar los DataFrames con base a las columnas 'country' y 'time'
df_combined = pd.merge(df1, df2, on=['country', 'time'], how='left')

# Guardar el DataFrame combinado en un nuevo archivo de Excel
df_combined.to_excel('archivo_combinado.xlsx', index=False)
