class ParesImpares:
    def ExtraePares(self, lista):
     nuevalista = []
     for elemento in lista:
        if (elemento % 2 == 0):#cuadrado
         nuevalista.append(elemento)
         
         
     return nuevalista
    
            
    def ExtraeImpares(self, lista)->list:
        nuevalista = []
        for elemento in lista:
            if (elemento % 2 == 1):#cubo
                nuevalista.append(elemento)
               
        return nuevalista
    
    def Par(n:int)->bool:
        if n%2==0:
            return True
        else:
            return False
        
         
if __name__ == "__main__":
     lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
     
     obj= ParesImpares()
     print(obj.ExtraePares(lista))
     print(obj.ExtraeImpares(lista))
   

     verifica=lambda n: n%2==0
        
     positivo=lambda n: n>0
     negativo=lambda n: n<0

     MayorDedos=lambda a,b: a>b
     print(f"El valor de a es mayor que b? {MayorDedos(450, 256)}")

     print(f"El numeroes positivo? {positivo(120)}")
     

     
     Otralista=map(lambda n: n**2, list(filter(lambda n: n%2 == 0, lista)))
     print(list(Otralista))

     edades= [15, 22, 30, 17, 45, 60]
     Minuevalista=list(map(lambda edad: "eres mayor de edad" if (edad >= 18) else "no eres mayor de edad", edades))
     print(edades)
     print(Minuevalista)
     #numeros pares entre dos numeros
     OtrasLista=list(map(lambda n: n / 2, list(filter(lambda n: n%2==0,edades))))
     print(OtrasLista)
     

     