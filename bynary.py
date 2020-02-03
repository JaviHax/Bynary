'''
Programa desarrollado por Javier "JaviHax" Rivas 2019.
'''

print("\033[1;32;40m ______                                ")
print("\033[1;32;40m | ___ \                               ")
print("\033[1;32;40m | |_/ /_   _ _ __   __ _ _ __ _   _   ")
print("\033[1;32;40m | ___ \ | | | '_ \ / _` | '__| | | |  ")
print("\033[1;32;40m | |_/ / |_| | | | | (_| | |  | |_| |  ")
print("\033[1;32;40m \____/ \__, |_| |_|\__,_|_|   \__, |  ")
print("\033[1;32;40m         __/ |                  __/ |  ")
print("\033[1;32;40m        |___/                  |___/   ")
print("\033[1;32;40m Generator By JaviHax                  ")
validador = True
opc = input("Seleccione una opcion\n1). Convertir de Decimal a Binario.\n2). Convertir de Binario a Decimal.\n3). Complemento A10.\n4). Complemento A9.\n5). Complemento A1.\n6). Complemento A2.\n7). Salir.\nSu desicion: ")

if opc == '1':# convertir de decimal a binario
    while validador == True:
        decimal= input("Ingrese su numero decimal: ")
        binary = "{0:b}".format(int(decimal))
        print(f"El valor de {decimal} en binario es: {binary}")
        opc = input("Desea convertir otro numero?\n1). Si.\n2). No.\nSu respuesta: ")
        if opc == '1':
            validador = True
        elif opc == '2':
            print("Gracias por usar el programa.")
            validador = False
        else:
            print("Valor desconocido, Terminando ejecucion.")
            exit()
            
elif opc == '2':#convertir de binario a decimal
    while validador == True:
        binary = input("Ingrese su numero binario: ")
        decimal = int(binary, 2)
        print(f"El valor binario {binary} en decimal es: {decimal}")
        opc = input("Desea convertir otro numero?\n1). Si.\n2). No.\nSu respuesta: ")
        if opc == '1':
            validador = True
        elif opc == '2':
            print("Gracias por usar el programa.")
            validador = False
        else:
            print("Valor desconocido, Terminando ejecucion.")
            exit()

elif opc == '3':#complemento A10
    print("Bienvenido/a al complemento A10")
    minuendo = input("Ingrese el valor del minuendo: ")
    substraendo = input("Ingrese el valor del substraendo: ")
    total = int(minuendo) - int(substraendo)
    total = abs(total)
    auxiliar = int(total)

    if total > 0 and total < 10:
        control = 0
        while control < 9:
            complemento = 10
            operacion = complemento - int(substraendo)
            final = int(minuendo) + operacion
            substraendo = final
            control += final
            
        if operacion == auxiliar:
            print(f"El valor buscado es: {operacion}")
        else:
            cadena = str(final)
            print(f"El valor buscado es: {cadena[1:]}")

    elif total > 10 and total < 99:
        control = 0
        while control < 99:
            complemento = 100
            operacion = complemento - int(substraendo)
            final = int(minuendo) + operacion
            substraendo = final
            control += final
            
        if operacion == auxiliar:
            print(f"El valor buscado es: {operacion}")
        else:
            cadena = str(final)
            print(f"El valor buscado es: {cadena[1:]}")

    elif total > 100 and total < 999:
        control = 0
        while control < 999:
            complemento = 1000
            operacion = complemento - int(substraendo)
            final = int(minuendo) + operacion
            substraendo = final
            control += final
            
        if operacion == auxiliar:
            print(f"El valor buscado es: {operacion}")
        else:
            cadena = str(final)
            print(f"El valor buscado es: {cadena[1:]}")
    
    elif total > 1000 and total < 9999:
        control = 0
        while control < 9999:
            complemento = 10_000
            operacion = complemento - int(substraendo)
            final = int(minuendo) + operacion
            substraendo = final
            control += final
        
        if operacion == auxiliar:
            print(f"El valor buscado es: {operacion}")
        else:
            cadena = str(final)
            print(f"El valor buscado es: {cadena[1:]}")

    else:
        control = 0
        while control < 99999:
            complemento = 100_000
            operacion = complemento - int(substraendo)
            final = int(minuendo) + operacion
            substraendo = final
            control += final
            
        if operacion == auxiliar:
            print(f"El valor buscado es: {operacion}")
        else:
            cadena = str(final)
            print(f"El valor buscado es: {cadena[1:]}")

elif opc == '4':#complemento A9
    print("Bienvenido/a al complemento A9")
    minuendo = input("Ingrese el valor del minuendo: ")
    substraendo = input("Ingrese el valor del substraendo: ")
    total = int(minuendo) - int(substraendo)
    total = abs(total)
    auxiliar = int(total)

    if total > 1 and total < 9:
        control = 0
        while control < 9:
            complemento = 9
            operacion = complemento - int(substraendo)
            final = int(minuendo) + operacion
            substraendo = final
            control += final
            
        if operacion == auxiliar:
            print(f"El valor buscado es: {operacion}")
        else:
            cadena = str(final)
            print(f"El valor buscado es: {int(cadena[1:])+1}")

    elif total > 10 and total < 99:
        control = 0
        while control < 99:
            complemento = 99
            operacion = complemento - int(substraendo)
            final = int(minuendo) + operacion
            substraendo = final
            control += final
            
        if operacion == auxiliar:
            print(f"El valor buscado es: {operacion}")
        else:
            cadena = str(final)
            print(f"El valor buscado es: {int(cadena[1:])+1}")

    elif total > 100 and total < 999:
        control = 0
        while control < 999:
            complemento = 999
            operacion = complemento - int(substraendo)
            final = int(minuendo) + operacion
            substraendo = final
            control += final
            
        if operacion == auxiliar:
            print(f"El valor buscado es: {operacion}")
        else:
            cadena = str(final)
            print(f"El valor buscado es: {int(cadena[1:])+1}")

    elif total > 1000 and total < 9999:
        control = 0
        while control < 9999:
            complemento = 9999
            operacion = complemento - int(substraendo)
            final = int(minuendo) + operacion
            substraendo = final
            control += final
            
        if operacion == auxiliar:
            print(f"El valor buscado es: {operacion}")
        else:
            cadena = str(final)
            print(f"El valor buscado es: {int(cadena[1:])+1}")

    elif total > 10000 and total < 99999:
        control = 0
        while control < 99999:
            complemento = 99999
            operacion = complemento - int(substraendo)
            final = int(minuendo) + operacion
            substraendo = final
            control += final
            
        if operacion == auxiliar:
            print(f"El valor buscado es: {operacion}")
        else:
            cadena = str(final)
            print(f"El valor buscado es: {int(cadena[1:])+1}")
    
    else:
        control = 0
        while control < 999_999:
            complemento = 999_999
            operacion = complemento - int(substraendo)
            final = int(minuendo) + operacion
            substraendo = final
            control += final
            
        if operacion == auxiliar:
            print(f"El valor buscado es: {operacion}")
        else:
            cadena = str(final)
            print(f"El valor buscado es: {int(cadena[1:])+1}")

elif opc == '5':#complemento A1
    minuendo = input("Ingrese su minuendo en binario: ")
    substraendo = input("Ingrese su substraendo en binario: ")

    v_buscado = int(minuendo, 2) - int(substraendo, 2)
    v_buscado = abs(v_buscado)
    v_buscado = "{0:b}".format(v_buscado)

    lmin = len(minuendo)
    longitud = len(substraendo)
    substract = []
    for i in range(0, longitud): #invertidor de substraendo
        if substraendo[i] == '1':
            substract.append(0)
        else:
            substract.append(1)

    substract.reverse()
    exp = 0
    val = 0
    for i in range(0, longitud):#convierte sustraendo a decimal
        rec = substract[i] * (2**exp)
        val += rec
        exp += 1

    #bucle de control de calculo
    total = int(minuendo,2) + val
    total = "{0:b}".format(total)
    longitud = len(total)
    if longitud > lmin:
        trans = total[1:]
        trans = int(trans, 2)
        res = trans + 1
        res = "{0:b}".format(res)
        print(f"El valor buscado fue: {res}")

    else:
        result = []
        longitud = len(total)
        for i in range(0, longitud):
            if total[i] == '1':
                result.append(0)
            else:
                result.append(1)

        print(f"El valor buscado fue: {result}")

elif opc == '6':#complemento A2
    
    minuendo = input("Ingrese su minuendo (en binario): ")
    substraendo = input("Ingrese su substraendo (en binario): ")

    v_buscado = int(minuendo, 2) - int(substraendo, 2)
    v_buscado = abs(v_buscado)
    v_buscado = "{0:b}".format(v_buscado)

    lmin = len(minuendo)
    longitud = len(substraendo)
    substract = []
    for i in range(0, longitud): #invertidor de substraendo
        if substraendo[i] == '1':
            substract.append(0)
        else:
            substract.append(1)

    substract.reverse()
    exp = 0
    val = 0
    for i in range(0, longitud):#convierte sustraendo a decimal
        rec = substract[i] * (2**exp)
        val += rec
        exp += 1

    #bucle de control de calculo
    total = int(minuendo,2) + val
    total = "{0:b}".format(total)
    longitud = len(total)
    if longitud > lmin:
        trans = total[1:]
        trans = int(trans, 2)
        res = trans + 1
        res = "{0:b}".format(res)
        print(f"El valor buscado fue: {res}")

    else:
        result = []
        longitud = len(total)
        for i in range(0, longitud):
            if total[i] == '1':
                result.append(0)
            else:
                result.append(1)

        print(f"El valor buscado fue: {result}")

elif opc == '7':#salida
    print("Gracias por preferirnos.")
    exit()

else:#default
    print("Valor desconocido, terminando ejecucion.")
    exit()