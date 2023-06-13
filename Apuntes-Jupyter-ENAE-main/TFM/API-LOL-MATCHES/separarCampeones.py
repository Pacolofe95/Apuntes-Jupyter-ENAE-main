import pandas as pd

# Leer el archivo CSV
df = pd.read_csv('C:/Users/Fernando/Desktop/Mod1WinLose.csv')

# Obtener una lista única de roles (role)
roles = df['role'].unique()

# Recorrer cada rol
for role in roles:
    # Filtrar los datos por rol
    role_df = df[df['role'] == role]
    
    # Obtener una lista de campeones únicos para el rol actual
    champions = role_df['championId'].unique()
    
    # Recorrer cada campeón
    for champion_id in champions:
        # Filtrar los datos por campeón y rol
        champion_df = role_df[role_df['championId'] == champion_id]
        
        # Obtener el nombre del campeón
        champion_name = champion_df['championName'].iloc[0]
        
        # Verificar si el campeón tiene más de 4 registros
        if len(champion_df) > 4:
            # Crear un nuevo DataFrame con los registros del campeón
            new_df = pd.DataFrame(champion_df)
            
            # Generar un nombre de archivo único para el campeón y el rol
            file_name = f'{role}_{champion_name}_records.csv'
            
            # Guardar el nuevo DataFrame en un archivo CSV
            new_df.to_csv(file_name, index=False)


# import pandas as pd

# # Leer el archivo CSV
# df = pd.read_csv('C:/Users/Fernando/Desktop/Mod1WinLose.csv')

# # Obtener una lista única de roles (role)
# roles = df['role'].unique()

# # Bandera para controlar si se han procesado los dos primeros campeones del primer rol
# processed_champions = 0

# # Recorrer cada rol
# for role in roles:
#     # Verificar si se ha procesado el primer rol
#     if processed_champions > 0:
#         break
    
#     # Filtrar los datos por rol
#     role_df = df[df['role'] == role]
    
#     # Obtener una lista de campeones únicos para el rol actual
#     champions = role_df['championId'].unique()
    
#     # Recorrer cada campeón
#     for champion_id in champions:
#         # Verificar si se han procesado los dos primeros campeones del primer rol
#         if processed_champions > 1:
#             break
        
#         # Filtrar los datos por campeón y rol
#         champion_df = role_df[role_df['championId'] == champion_id]
        
#         # Obtener el nombre del campeón
#         champion_name = champion_df['championName'].iloc[0]
        
#         # Verificar si el campeón tiene más de 4 registros
#         if len(champion_df) > 4:
#             # Crear un nuevo DataFrame con los registros del campeón
#             new_df = pd.DataFrame(champion_df)
            
#             # Generar un nombre de archivo único para el campeón y el rol
#             file_name = f'{role}_{champion_name}_records.csv'
            
#             # Guardar el nuevo DataFrame en un archivo CSV
#             new_df.to_csv(file_name, index=False)
        
#         # Incrementar la cuenta de campeones procesados
#         processed_champions += 1
