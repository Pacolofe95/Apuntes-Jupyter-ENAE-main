import pyodbc
from functionsList import getTopPlayers

conn = pyodbc.connect('Driver={SQL Server};SERVER=enae-tfm.database.windows.net;Database=LOL2023Enae;UID=tfmlol;PWD=LOL2023Enae')

players = getTopPlayers()

cursor = conn.cursor()

for i in players:    
    cursor.execute(f"INSERT INTO topPlayers values('{i}')")
    conn.commit()
    print(i)

conn.close() 

