print("Digite um número: ")
a = int(input(">>>"))
if a < 1:
    print("Número inválido")
else:

    if a == 2 or  a==3 or a==5 or a==7:
        print("Primo")
    elif a % 2 == 0 or a % 3 == 0 or a % 5 == 0 or a % 7 == 0 or a == 1:
        print("Não primo")
    else:
        print("Primo")