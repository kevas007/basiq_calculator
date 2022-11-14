try:
    nombre1 = int( input("Entrer le premier nombre :  "))
    nombre2 = int(input("Entrer le second nombre :  "))

    op = input("Entrer l'opérateur: ")

    if op == "+" :
        result= nombre1 + nombre2
        print( result )
    elif op == "-":
        result=  nombre1 -  nombre2
        print( result )
    elif op == "*":
        result=  nombre1 *  nombre2
        print( result )
    elif op == "-":
        result=  nombre1 /  nombre2
        print( abs(result ))
    else:
        print('Invalid opérateur')
except:
    print('Somehting went rong')