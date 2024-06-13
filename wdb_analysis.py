import pandas as pd

# Cargar los datos en un DataFrame 
df = pd.read_excel(r'C:\Users\adria\OneDrive\Escritorio\Modelo econometrico\Modelo-econometrico\AllCountriesDataframe.xlsx')

# Mostrar una muestra de los datos
print(df.head())

# Paso 1: Calcular el número de datos no nulos por país
country_data_avail = df.groupby('country').count()

# Paso 2: Identificar los países con datos insuficientes
# Aquí asumimos que un país debe tener datos para al menos el 50% de los años disponibles
min_data_required = df['time'].nunique() / 2
countries_to_keep = country_data_avail[country_data_avail.min(axis=1) >= min_data_required].index

# Filtrar el DataFrame original para mantener solo los países con suficientes datos
filtered_df = df[df['country'].isin(countries_to_keep)]

# Paso 3: Determinar los años en los que la mayoría de los países tienen datos completos
years_data_avail = filtered_df.groupby('time').count()
min_countries_required = filtered_df['country'].nunique() * 0.75  # Asumimos que necesitamos al menos el 75% de los países con datos

years_to_keep = years_data_avail[years_data_avail.min(axis=1) >= min_countries_required].index

# Filtrar el DataFrame para mantener solo los años seleccionados
final_df = filtered_df[filtered_df['time'].isin(years_to_keep)]

# Identificar los países eliminados
eliminated_countries = set(df['country'].unique()) - set(final_df['country'].unique())

# Guardar el DataFrame final en un archivo de Excel
final_df.to_excel('filtered_data.xlsx', index=False)

# Mostrar los países eliminados
print("Países eliminados:", eliminated_countries)