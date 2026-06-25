import pandas as pd
from sklearn.linear_model import LinearRegression

class Regresion_Lineal:
    def __init__(self):

        self.datos = {
            "habitantes": [2, 3, 4, 4, 5, 5, 6, 6, 7, 8],
            "dispositivos": [2, 3, 4, 5, 6, 7, 8, 8, 10, 12],
            "autos": [0, 0, 1, 1, 1, 2, 2, 2, 2, 3],
            "cargadores": [0, 0, 1, 1, 1, 2, 2, 2, 2, 3],
            "consumo": [140, 165, 210, 225, 260, 320, 360, 380, 430, 510]
        }
        self.df = pd.DataFrame(self.datos)
        
    def obtener_caracteristicas(self):
    
        return self.df[["habitantes", "dispositivos", "autos", "cargadores"]]
        
    def obtener_objetivo(self):
  
        return self.df["consumo"]


class ModeloConsumo:
    def __init__(self):
      
        self.modelo = LinearRegression()
        
    def entrenar(self, X, y):
   
        self.modelo.fit(X, y)
        print("")
        
    def predecir_consumo(self, datos_vivienda):
  
        columnas = ["habitantes", "dispositivos", "autos", "cargadores"]
        df_vivienda = pd.DataFrame([datos_vivienda], columns=columnas)
        
        prediccion = self.modelo.predict(df_vivienda)
        return round(prediccion[0], 2)



if __name__ == '__main__':
    print("\n")
    

    manejador_datos = Regresion_Lineal()
    ia_modelo = ModeloConsumo()

    X = manejador_datos.obtener_caracteristicas()
    y = manejador_datos.obtener_objetivo()
    

    ia_modelo.entrenar(X, y)
    
   
    nueva_vivienda = [5, 8, 2, 2]

    resultado = ia_modelo.predecir_consumo(nueva_vivienda)
    
    print(f"\nConsumo estimado para la vivienda: {resultado} KWh")
    