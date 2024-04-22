# Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
# A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

# Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.

# Trabalhe esse código em seu IDE, suba ele para sua conta no GitHub e compartilhe o link desse projeto no campo ao lado para que outros desenvolvedores possam analisá-lo.

flag = True

while flag:
    print("Informe o nome completo:")
    name = input()
    print("Informe o ano de nascimento:")
    try:
        year = int(input())
        if(year<1992 or year>2022):
            print("O ano precisa estar entre 1992 e 2022.")
        else:
            print(f'{2022-year} anos para {name}')
        flag = False
    except:
        print("O ano só pode ser escrito em formato numérico.")
