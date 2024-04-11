# Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
# 1. Soma
# 2. Subtração
# 3. Multiplicação
# 4. Divisão

# Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

def soma(a, b):
    return a+b

def sub(a, b):
    return a-b

def mult(a, b):
    return a*b

def div(a, b):
    return a//b

def calculadora(a,b,operador):
    if operador == 1:
        print(soma(a,b))
    elif operador == 2:
        print(sub(a,b))
    elif operador == 3:
        print(mult(a,b))
    elif operador == 4:
        print(div(a,b))
    else: print(0)

while True:
    print()
    print("Escolha as opções:")
    print("1 - SOMA")
    print("2 - SUBTRAÇÃO")
    print("3 - MULTIPLICAÇÃO")
    print("4 - DIVISÃO")
    print("5 - SAIR DO PROGRAMA")

    operador = int(input())

    if(operador == 5): break

    a = int(input("Primeiro número: "))
    b = int(input("Segundo número: "))

    calculadora(a,b,operador)





    
