import pandas as pd
from getChampId import getChampionsId

df = pd.read_csv("Apuntes-Jupyter-ENAE-main\TFM\API-LOL-MATCHES\EUW1_6381286401.csv")
#print(df)
#dfGeneral["win"] = df["win"]
#dfGeneral["role"] = df["individualPosition"] 

def winLoseEngine(df:pd.DataFrame):
    
    dfGeneral = pd.DataFrame()
    columnasMod1                = ["info.gameMode", "teamPosition", "championId", "championName", "win"]
    dfGeneral                   =  df[columnasMod1]
    dfGeneral.columns.values[1] = "role"
         
    ####### SEPARO LOS DF EN 2 (UNO PARA CADA EQUIPO) ##########

    dfTeamX = dfGeneral.iloc[:5]
    dfTeamY = dfGeneral.iloc[5:]

    dfTeamX1= pd.merge(dfTeamX, dfTeamY, on = "role", how= "inner")
    dfTeamY1= pd.merge(dfTeamY, dfTeamX, on = "role", how= "inner")

    dfModelo1 = pd.concat([dfTeamX1,dfTeamY1], ignore_index = True)
    dfModelo1["win_x"] = dfModelo1["win_x"].astype(int)
    dfModelo1.drop(columns=["win_y"], inplace = True)
    dfModelo1 = dfModelo1.rename(columns = {"championId_y" : "rivalId", "championName_y" : "rivalName",
                                            "championId_x" : "championId", "championName_x" : "championName"})
    
    return dfModelo1 
    

def kdaWinLoseEngine(df:pd.DataFrame):
    
    df["kda"] = (df["kills"] + df["assists"]) / df["deaths"].replace(0, 1)

    dfGeneral = pd.DataFrame()
    columnasMod2                = ["info.gameMode", "teamPosition", "championId", "championName", "kda", "win"]
    dfGeneral                   =  df[columnasMod2]
    dfGeneral.columns.values[1] = "role"
            
    ####### SEPARO LOS DF EN 2 (UNO PARA CADA EQUIPO) ##########

    dfTeamX = dfGeneral.iloc[:5]
    dfTeamY = dfGeneral.iloc[5:]

    dfTeamX1= pd.merge(dfTeamX, dfTeamY, on = "role", how= "inner")
    dfTeamY1= pd.merge(dfTeamY, dfTeamX, on = "role", how= "inner")

    dfModelo2 = pd.concat([dfTeamX1,dfTeamY1], ignore_index = True)
    dfModelo2["win_x"] = dfModelo2["win_x"].astype(int)
    dfModelo2.drop(columns=["win_y"], inplace=True)
    dfModelo2 = dfModelo2.rename(columns = {"championId_y" : "rivalId", "championName_y" : "rivalName",
                                            "championId_x" : "championId", "championName_x" : "championName",
                                            "kda_x" : "kda", "kda_y" : "rival_kda", "win_x" : "win"})
    win_column = dfModelo2.pop("win")  # Extraer la columna "win"
    dfModelo2["win"] = win_column  # Agregar la columna "win" al final del DataFrame

    return dfModelo2

def killsMotor (df:pd.DataFrame):

    df["kills"]
    dfGeneral = pd.DataFrame()
    columnasMod3 = ["info.gameMode", "teamPosition", "championId", "championName", "kills", "win"]
    dfGeneral = df[columnasMod3]
    dfGeneral.columns.values[1] = "role"

    dfTeamX = dfGeneral.iloc[:5]
    dfTeamY = dfGeneral.iloc[5:]

    dfTeamX1= pd.merge(dfTeamX, dfTeamY, on = "role", how= "inner")
    dfTeamY1= pd.merge(dfTeamY, dfTeamX, on = "role", how= "inner")

    dfModelo3 = pd.concat([dfTeamX1,dfTeamY1], ignore_index = True)
    dfModelo3["win_x"] = dfModelo3["win_x"].astype(int)
    dfModelo3.drop(columns=["win_y"], inplace=True)
    dfModelo3 = dfModelo3.rename(columns = {"championId_y" : "rivalId", 
                                            "championName_y" : "rivalName",
                                            "championId_x" : "championId", 
                                            "championName_x" : "championName",
                                            "kills_x": "championKills",
                                            "kills_y": "rivalKills",
                                            "win_x":"win"})
    win_column = dfModelo3.pop("win") 
    dfModelo3["win"] = win_column 

    return dfModelo3

def assistsMotor(df: pd.DataFrame):

    df["assists"]

    dfGeneral = pd.DataFrame()
    columnasMod4 = ["info.gameMode", "teamPosition", "championId", "championName", "assists", "win"]
    dfGeneral = df[columnasMod4]
    dfGeneral.columns.values[1] = "role"

    dfTeamX = dfGeneral.iloc[:5]
    dfTeamY = dfGeneral.iloc[5:]

    dfTeamX1 = pd.merge(dfTeamX, dfTeamY, on="role", how="inner")
    dfTeamY1 = pd.merge(dfTeamY, dfTeamX, on="role", how="inner")

    dfModelo4 = pd.concat([dfTeamX1, dfTeamY1], ignore_index=True)
    dfModelo4["win_x"] = dfModelo4["win_x"].astype(int)
    dfModelo4.drop(columns=["win_y"], inplace=True)
    dfModelo4 = dfModelo4.rename(columns={"championId_y": "rivalId",
                                          "championName_y": "rivalName",
                                          "championId_x": "championId",
                                          "championName_x": "championName",
                                          "assists_x": "championAssists",
                                          "assists_y": "rivalAssists",
                                          "win_x": "win"})
    win_column = dfModelo4.pop("win")
    dfModelo4["win"] = win_column

    return dfModelo4

def deathsMotor(df: pd.DataFrame):

    df["deaths"]

    dfGeneral = pd.DataFrame()
    columnasMod5 = ["info.gameMode", "teamPosition", "championId", "championName", "deaths", "win"]
    dfGeneral = df[columnasMod5]
    dfGeneral.columns.values[1] = "role"

    dfTeamX = dfGeneral.iloc[:5]
    dfTeamY = dfGeneral.iloc[5:]

    dfTeamX1 = pd.merge(dfTeamX, dfTeamY, on="role", how="inner")
    dfTeamY1 = pd.merge(dfTeamY, dfTeamX, on="role", how="inner")

    dfModelo5 = pd.concat([dfTeamX1, dfTeamY1], ignore_index=True)
    dfModelo5["win_x"] = dfModelo5["win_x"].astype(int)
    dfModelo5.drop(columns=["win_y"], inplace=True)
    dfModelo5 = dfModelo5.rename(columns={"championId_y": "rivalId",
                                          "championName_y": "rivalName",
                                          "championId_x": "championId",
                                          "championName_x": "championName",
                                          "deaths_x": "championDeaths",
                                          "deaths_y": "rivalDeaths",
                                          "win_x": "win"})
    win_column = dfModelo5.pop("win")
    dfModelo5["win"] = win_column

    return dfModelo5

def killsDeathsAssists(df: pd.DataFrame):
    dfGeneral = pd.DataFrame()
    columnasMod7 = ["info.gameMode", "teamPosition", "championId", "championName", "kills", "deaths", "assists", "win"]
    dfGeneral = df[columnasMod7]
    dfGeneral.columns.values[1] = "role"

    # Separar los DF en 2 (uno para cada equipo)
    dfTeamX = dfGeneral.iloc[:5]
    dfTeamY = dfGeneral.iloc[5:]

    dfTeamX1 = pd.merge(dfTeamX, dfTeamY, on="role", how="inner")
    dfTeamY1 = pd.merge(dfTeamY, dfTeamX, on="role", how="inner")

    dfModelo7 = pd.concat([dfTeamX1, dfTeamY1], ignore_index=True)
    dfModelo7["win_x"] = dfModelo7["win_x"].astype(int)
    dfModelo7.drop(columns=["win_y"], inplace=True)
    dfModelo7 = dfModelo7.rename(columns={"championId_y": "rivalId", "championName_y": "rivalName",
                                          "championId_x": "championId", "championName_x": "championName",
                                          "kills_x": "kills", "deaths_x": "deaths", "assists_x": "assists",
                                          "kills_y": "rival_kills", "deaths_y": "rival_deaths", "assists_y": "rival_assists",
                                          "win_x": "win"})
    win_column = dfModelo7.pop("win")  # Extraer la columna "win"
    dfModelo7["win"] = win_column  # Agregar la columna "win" al final del DataFrame

    return dfModelo7

def experienceChampion():
    
    dfGetChampionId = getChampionsId()


    return

a = experienceChampion()