
# INSTRUÇÕES DO PROJETO
# Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:

# 1: Soma
# 2: Subtração
# 3: Multiplicação
# 4: Divisão
# 0: Sair

# Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

# Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar.

# É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado. 

# Trabalhe esse código em seu IDE, suba ele para sua conta no GitHub e compartilhe o link desse projeto no campo ao lado para que outros desenvolvedores possam analisá-lo.

def soma(a, b):
    return a+b

def sub(a, b):
    return a-b

def mult(a, b):
    return a*b

def div(a, b):
    return a/b

while True:
    print()
    print("Escolha as opções:")
    print("1 - SOMA")
    print("2 - SUBTRAÇÃO")
    print("3 - MULTIPLICAÇÃO")
    print("4 - DIVISÃO")
    print("0 - SAIR DO PROGRAMA")

    operador = int(input())

    if(operador == 0): break

    if operador == 1:
        a = int(input("Primeiro número: "))
        b = int(input("Segundo número: "))
        print(soma(a,b))
    elif operador == 2:
        a = int(input("Primeiro número: "))
        b = int(input("Segundo número: "))
        print(sub(a,b))
        a = int(input("Primeiro número: "))
        b = int(input("Segundo número: "))
    elif operador == 3:
        a = int(input("Primeiro número: "))
        b = int(input("Segundo número: "))
        print(mult(a,b))
    elif operador == 4:
        a = int(input("Primeiro número: "))
        b = int(input("Segundo número: "))
        print(div(a,b))
    else: 
        print("Essa opção não existe")

   
