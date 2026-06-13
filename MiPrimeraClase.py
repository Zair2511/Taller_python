class persona:
  
   def __init__(self):
    self.nombre = "Juan"
    self.apellido = "Flores Gasca"
#def es para definir un metodo
def MiMetodo(self):
    print(f"Hola, {self.nombre}")


if __name__ == "__main__":
    obj = persona()
    print(obj.nombre)
    print(obj.apellido)
    obj.MiMetodo()

   
