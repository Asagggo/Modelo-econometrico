import pandas as pd

# Leer el DataFrame desde un archivo de Excel
input_file = r'C:\Users\adria\OneDrive\Escritorio\Modelo econometrico\Modelo-econometrico\AllCountriesDataframe.xlsx'  # ruta archivo de entrada
df = pd.read_excel(input_file)

# Asegúrate de que la columna 'time' sea de tipo entero
df['time'] = df['time'].astype(int)

# Filtrar el DataFrame para el rango de años 1995-2020
df_filtered = df[(df['time'] >= 1995) & (df['time'] <= 2020)]

# Lista para almacenar los países que tienen todos los valores disponibles en el rango de años
valid_countries = []

# Agrupar por país
grouped = df_filtered.groupby('country')

# Verificar cada grupo
for country, group in grouped:
    if group.dropna().shape[0] == len(range(1995, 2021)):  # Debe tener 26 filas sin valores faltantes (1995-2020 inclusivo)
        valid_countries.append(country)

# Filtrar el DataFrame original para incluir solo los países válidos
result_df = df[df['country'].isin(valid_countries)]

# Escribir el DataFrame resultante a un nuevo archivo de Excel
output_file = r'C:\Users\adria\OneDrive\Escritorio\Modelo econometrico\Modelo-econometrico\AllCountriesDataframeFiltered2.xlsx'  # Reemplaza con la ruta a tu archivo de salida
result_df.to_excel(output_file, index=False)

print(f"Datos filtrados guardados en {output_file}")

# Imprimir la lista de países que quedaron después de la filtración
print("Países con datos completos de 1995 a 2020:")
for country in valid_countries:
    print(country)

print(f"Datos filtrados guardados en {output_file}")