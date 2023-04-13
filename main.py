print("Digite um número: ")
a = int(input(">>>")) + 1
b = list(range(2,a))
b.pop()
print(b)
if a % b == 0:
    print("Numero Não é primo")
else:
    print("é um número primo")