def Mirango(n:int):
    for i in range(n):
        if (i<5):
         yield i
        else:
            return

if __name__ == "__main__":
    res:int = 0
    Milista=[]

    for i in Mirango(10):
        Milista.append(i**2)
        res=res + i**2   
    print(res)
 #"mayor de edad" if n>=18: else "menor de edad"   
    cuadrados = [i**2 for i in range(10)]
    print(cuadrados)
    print(Milista)