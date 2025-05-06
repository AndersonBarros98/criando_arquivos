import os 
from pathlib import Path

caminho = Path().home()
novo_caminho = caminho / "Exercicios"

os.makedirs(novo_caminho,exist_ok=True)


exercicio1 = '''  numero = int(input("Digite um numero: "))

    if numero == 0:
      print("Esse numero e 0")

    if numero > 0:
      print("Numero positivo")

    if numero < 0:
      print("numero negativo") '''

exercicio_2 = '''

primeiro_numero = int(input("Digite um numero: "))
segundo_numero = int(input("Digite outro numero: "))

if primeiro_numero > segundo_numero:
  print(f"{primeiro_numero} e maior que {segundo_numero}")

else:
  print(f"{segundo_numero} e maior que {primeiro_numero}")

Exercício_3 = 

numero = int(input("Digite um numero: "))

if numero % 2 == 0:
  print(f"{numero} e par")

else:
  print(f"{numero} e impar") '''
  
  

exercicio_4 = '''

  ano = int(input("Digite um ano: "))

  if (ano % 4 == 0 and ano % 100 != 100) or ano % 400 == 0:
    print("Ano bissesto")

  else:
    print("Nao e ano bissesto") '''

exercicio_5 = '''

primeiro_numero = int(input("Digite um numero: "))
segundo_numero = int(input("Digite outro numero: "))
terceiro_numero = int(input("Digite um numero: "))

if primeiro_numero > segundo_numero and primeiro_numero > terceiro_numero:
  print(f"{primeiro_numero} e maior")

elif segundo_numero > primeiro_numero and segundo_numero > terceiro_numero:
  print(f"{segundo_numero} e maior")

else:
  print(f"{terceiro_numero} e maior") '''

exercicio_6 = '''

idade = int(input("Digite sua idade"))

if idade >= 18
  print("usuario pode votar!")

else:
  print("usuario nao pode votar!") '''

exercicio_7 = '''

print("Horario de ir embora")

horario_permitido = "21:40"

hora_atual = input("Digite o horário que você está saindo: ")

if hora_atual >= horario_permitido:
  print("Você já pode ir embora")

else:
  print("Permaneça até o horario") '''

exercicio_8 = '''

senha = "1234"

sua_senha = input("Digite uma senha")

if sua_senha == senha:
  print("Sua senha corresponde a senha original")

else:
  print("Senha nao corresponde") '''

exercicio_9 = '''

numero = int(input("Digite um numero: "))

if numero > 10 and numero < 50:
  print("Numero esta entre a contagem de 10 e 50")

else:
  print("Numero nao esta na sequencia") '''

exercicio_10 = '''

numero = int(input("Digite um numero: "))

if numero > 100:
  print("Numero alto")

else:
  print("Numero baixo") '''

exercicio_11 = '''

primeiro_numero = int(input("Digite um numero: "))
segundo_numero = int(input("Digite um numero: "))
operador = input("escolha um operador").lower()

if operador == "soma":
  print(f"resultado {primeiro_numero + segundo_numero}")

elif operador == "multiplica":
  print(f"resultado {primeiro_numero * segundo_numero}")

elif operador == "subtrair":
  print(f"resultado {primeiro_numero - segundo_numero}")

else:
  print(f"resultado {primeiro_numero / segundo_numero}") '''


exercicio_12 = '''

print("escolha de 1 a 5 para ver o numero por exetenso")

numero = int(input("Digite um numero: "))

if numero == 1:
  print("Um")

elif numero == 2:
  print("Dois")

elif numero == 3:
  print("Tres")

elif numero == 4:
  print("Quatro")

elif numero == 5:
  print("Cinco")

else:
  print("Numero nao definido") '''

exercicio_13 = '''

data = "XX/XX/XXXX"
hora = "XX:XX"

while True:
  print("Escolha entre exibir data e hora ou se deseja sair")
  escolha = input("escolha uma opcao: ")

  if escolha == "data":
    print(f"Hoje e dia {data}")

  elif escolha == "hora":
    print(f"Sao {hora} horas.")

  elif escolha == "sair":
    break

  else:
    print("Opcao invalida") '''


exercicios = (exercicio1,exercicio_2,exercicio_4,exercicio_5,exercicio_6,exercicio_7,exercicio_8,exercicio_9,exercicio_10,exercicio_11,exercicio_12,exercicio_13)


for i in range(1,len(exercicios)):
    novo_arquivo = novo_caminho / f'arquivo{i}.py'
    novo_arquivo.touch()
    for exercicio in exercicios:
      with open(novo_arquivo, 'w', encoding='utf-8') as file:
        file.write(exercicios[i - 1])

