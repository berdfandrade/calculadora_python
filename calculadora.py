# Essa função adiciona
def adiciona(x, y):
    return x + y

# Essa função subtrai

def subtrai(x, y):
    return x - y

def multiplica(x, y):
    return x * y

def divide(x, y):
    return x/ y

print("Escolha a operação:")
print("1. Adicionar")
print("2. Subtrair")
print("3. Multiplicar")
print("4. Dividir")

while True:
    #Pega o valor escrito pelo usuario

    escolha = input("Escola a operação(1/2/3/4): ")

    if escolha in ('1', '2', '3', '4'):
        num1 = int(input("Escolha o primeiro número: "))
        num2 = int(input("Escolha o segundo número: "))

    if escolha == '1':
        print(num1, "+", num2, "=", adiciona(num1, num2))

    if escolha == '2':
        print(num1, "-", num2, "=", subtrai(num1, num2))

    elif escolha == '3':
        print(num1, "*", num2, "=", multiplica(num1, num2))

    elif escolha == '4':
        print(num1, "/", num2, "=", divide(num1, num2))

# Verificar se o usuario quer prosseguir com outra operacao

    proximo_calc = input("Deseja fazer outra operacao? (sim/não): ")
    if proximo_calc != "sim":
        print("Adeus!")
        break

else: print("Entrada Invalida")
