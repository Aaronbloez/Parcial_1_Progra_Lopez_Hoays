#1. Crear una función llamada aplicarAumento que reciba como parámetro el precio de un producto y devuelva el valor del producto con un aumento del 5%. Realizar la llamada desde el main.


#Esta funcion recibe un flotante el cual es multiplicado por 5 y dividido por 100 para sacar el 5%, despues eso se le suma al flootante original y lo retorna
def aplicar_aumento(precio:float)->float:
    aumento = (precio*5)/100
    precio_final = precio+aumento
    return precio_final




Final = aplicar_aumento(200)

print(Final)