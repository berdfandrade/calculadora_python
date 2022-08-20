# Calculadora em Python

![GitHub top language](https://img.shields.io/github/languages/top/berdfandrade/calculadora_python?color=F&logo=Python&logoColor=FFFFFF&style=plastic)

### Como funciona o meu programa? Simples!

Primeiro criamos uma função para adicionar, que retorna a soma dos valores que foram colocados nos parâmetros. `def adiciona`.

```python
def adiciona(x, y);
    return x + y
```

Fazemos o mesmo para o resto das funções!

```python
def adiciona(x, y);
    return x + y

def subtrai(x, y):
    return x - y

def multiplica(x, y):
    return x * y

def divide(x, y):
    return x/ y
```

Criamos um `while loop`, que vai ficar rodando até escrevermos um `break` em um `if statement`, que vamos declarar posteriormente. Vamos pegar também um `input` escrito pelo usuário.

```python
while true:

    escolha = input("Escola a operação(1/2/3/4): ")
```

Escrevemos `"Escola a operação(1/2/3/4): "` no `input`, porque vamos definir qual vai ser a função que vamos utilizar. Para isso fazemos um `for loop` para iterar pelo valor que o usuário colocou:

```python
    if escolha in ('1', '2', '3', '4'):
        num1 = int(input("Escolha o primeiro número: "))
        num2 = int(input("Escolha o segundo número: "))
```

Agora criamos um `if statement` para poder criar diferentes condições para a opção que pode ser escolhida. Depois fazemos a operação desejada:

```python
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

```

No final, perguntamos se o usuário quer fazer outra operação. Se ele quiser ele digita `sim`, que não queira, ele pode digitar qualquer coisa, que o programa vai entender que não quer prosseguir. Poderíamos escrever o `não`, porém, é mais prático digitar `!=`, que quer dizer *diferente de sim*. Caso o usuário não digite `sim`, quebramos o `while loop`.

```python
    proximo_calc = input("Deseja fazer outra operacao? (sim/não): ")
    if proximo_calc != "sim":
        print("Adeus!")
        break
   
    else: print("Entrada Invalida")

```

O `else` serve como alternativa de erro para o `while loop`.

Então, nosso código pronto, fica assim:

```python
def adiciona(x, y):
    return x + y

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


    proximo_calc = input("Deseja fazer outra operacao? (sim/não): ")
    if proximo_calc != "sim":
        print("Adeus!")
        break

else: print("Entrada Invalida")


```
