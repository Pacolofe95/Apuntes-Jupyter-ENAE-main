import pandas as pd


roles = ['Top', 'Jungle', 'Mid', 'AD Carry', 'Support']

ID = list(enumerate(roles, 1))

dimRoleID = pd.DataFrame(ID, columns= ['ID', 'Role'])
print(dimRoleID)

#dimRoleID.to_csv("C:/Users/Fernando/Documents/DANIEL/Daniel_UM/ENAE/TFM/Apuntes-Jupyter-ENAE/TFM/dimRole.csv", index=False)

