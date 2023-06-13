import pandas as pd

# Paso 2: Cargar el archivo CSV en un DataFrame
data = pd.read_csv('C:/Users/Fernando/Desktop/Mod1WinLose.csv')

# Especificar el rival concreto
rival_name = 'Jinx'

# Paso 3: Filtrar los datos solo para el rival específico
rival_data = data[data['rivalName'] == rival_name]

# Paso 4: Calcular el porcentaje de victorias para cada combinación de campeón y rival con count > 1
win_rate = rival_data.groupby('championName')['win_x'].agg(['mean', 'count'])
win_rate_filtered = win_rate[win_rate['count'] > 10].copy()
win_rate_filtered['win_percentage'] = win_rate_filtered['mean'] * 100

# Paso 5: Ordenar el DataFrame win_rate_filtered en orden descendente según el porcentaje de victorias
win_rate_sorted = win_rate_filtered.sort_values(by='win_percentage', ascending=False)

# Paso 6: Filtrar los campeones con el mayor porcentaje de victorias
top_campeones = win_rate_sorted.head(5)  # Cambiar el número de filas aquí según tus necesidades

# Paso 7: Imprimir los resultados
print(f"Los campeones con mayor porcentaje de victorias contra el rival {rival_name} son:")
for championName, porcentaje_victorias, count in top_campeones[['win_percentage', 'count']].itertuples(index=True):
    print(f"Campeón: {championName}, Porcentaje de victorias: {porcentaje_victorias}%, Número de enfrentamientos: {count}")


# LO DE ABAJO FUNCIONABA IGUAL PERO DABA UN WARNING
# import pandas as pd

# # Paso 2: Cargar el archivo CSV en un DataFrame
# data = pd.read_csv('C:/Users/Fernando/Desktop/Mod1WinLose.csv')

# # Especificar el rival concreto
# rival_name = 'Jinx'

# # Paso 3: Filtrar los datos solo para el rival específico
# rival_data = data[data['rivalName'] == rival_name]

# # Paso 4: Calcular el porcentaje de victorias para cada combinación de campeón y rival con count > 1
# win_rate = rival_data.groupby('championName')['win_x'].agg(['mean', 'count'])
# win_rate_filtered = win_rate[win_rate['count'] > 20]
# win_rate_filtered['win_percentage'] = win_rate_filtered['mean'] * 100

# # Paso 5: Ordenar el DataFrame win_rate_filtered en orden descendente según el porcentaje de victorias
# win_rate_sorted = win_rate_filtered.sort_values(by='win_percentage', ascending=False)

# # Paso 6: Filtrar los campeones con el mayor porcentaje de victorias
# top_campeones = win_rate_sorted.head(5)  # Cambiar el número de filas aquí según tus necesidades

# # Paso 7: Imprimir los resultados
# print(f"Los campeones con mayor porcentaje de victorias contra el rival {rival_name} son:")
# for championName, porcentaje_victorias, count in top_campeones[['win_percentage', 'count']].itertuples(index=True):
#     print(f"Campeón: {championName}, Porcentaje de victorias: {porcentaje_victorias}%, Número de enfrentamientos: {count}")

