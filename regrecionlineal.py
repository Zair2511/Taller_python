import pandas as pd
from sklearn.linear_model import LinearRegression

datos = {
    "habitantes": [2, 3, 4, 4, 5, 5, 6, 6, 7, 8],
    "dispositivos": [2, 3, 4, 5, 6, 7, 8, 8, 10, 12],
    "autos": [0, 0, 1, 1, 1, 2, 2, 2, 2, 3],
    "cargadores": [0, 0, 1, 1, 1, 2, 2, 2, 2, 3],
    "consumo": [140, 165, 210, 225, 260, 320, 360, 380, 430, 510]
}

df = pd.DataFrame(datos)

x = df[[
    "habitantes",
    "dispositivos",
    "autos",
    "cargadores"
]]

y=df["consumo"]

modelo=LinearRegression()

modelo.fit(x, y)

nueva_vivienda =[
    [5, 8, 2, 2]
]
prediccion = modelo.predict(nueva_vivienda)

print(
    "consumo estimado",
    round(prediccion[0], 2),
    "KWh"
)