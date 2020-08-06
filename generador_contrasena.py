import random
def generar_contrasena():
    mayus = ['A','B','C','D','E','F','G','H','I','J','K','M','N','L','LL','P','Q','O','V','W','X','Y','Z']
    minus = ['a','b','c','d','e','f','g','h','i','j','k','m','n','l','ll','p','q','o','v','w','x','y','z']
    simbolos = ['!','@','#','$','%','^','&','*','+','-','.']
    numeros = ['1','2','3','4','5','6','7','8','9','0']
    caracteres = mayus + minus + simbolos + numeros
    contrasena = []
    for i in range(15):
        caracter_random = random.choice(caracteres) #elegimos un caracter especial con el metodo choice()
        contrasena.append(caracter_random)
    contrasena = ''.join(contrasena) #lo convertimos en un string con el metodo join()
    return contrasena

def run():
    contrasena = generar_contrasena()
    print(f'Tu nueva contrasena es: {contrasena}')

if __name__ == '__main__':
    run()