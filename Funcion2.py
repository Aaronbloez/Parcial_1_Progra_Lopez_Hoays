#2. Crear una función que se llame reemplazarCaracteres que reciba una cadena de caracteres como primer parámetro, un carácter como segundo y otro carácter  como tercero,  
#la misma deberá reemplazar cada ocurrencia del segundo parámetro por el tercero y devolver la cantidad de veces que se reemplazo ese carácter  en la cadena

#Esta funcion recibe una cadena de string la compara con dos strings mas y mediante replace los reemplaza, despues tiene un for que mediante un contador mide las diferencias de caracteres
def Reemplazar_caracteres(cadena:str,caracter:str,caracter2:str)->str:
    cadena_final= cadena.replace(caracter,caracter2)
    contador = 0
    for i in cadena:
        if(i == caracter):
            contador+=1

    return cadena_final,contador




cadena = "Hoy es un buen diaoo"


Cadena_Final = Reemplazar_caracteres(cadena,"o","s")

print(Cadena_Final)



