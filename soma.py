import random
import os

while True:
    os.system('cls')

    try:
        faces_dados = int(input("Informe quantas faces tem os dados que você gostaria de somar: "))

        if faces_dados <= 1:
            print("Valor inválido! O número de faces deve ser maior que 1.")
            input("Pressione Enter para tentar novamente...")  # Pausa para o usuário ler
            continue  # Volta ao início do loop

        # Gerar e exibir o número aleatório
        numero_aleatorio1 = random.randint(1, faces_dados)
        numero_aleatorio2 = random.randint(1, faces_dados)
        resultado_da_soma = numero_aleatorio1 + numero_aleatorio2
    
        print("O valor do Dado 1 é:",numero_aleatorio1)
        print("O valor do Dado 2 é:",numero_aleatorio2)    
        print("A soma dos dados é:",resultado_da_soma)

        jogar_novamente = input("Deseja jogar novamente? (s/n): ").strip().lower()
        if jogar_novamente == 's':
            continue
        os.system('cls')
        print("Obrigado por jogar! Até a próxima!")
        break  # Sai do loop após exibir o resultado



    except ValueError:
        print("Entrada inválida! Por favor, insira um número inteiro.")
        input("Pressione Enter para tentar novamente...")  # Pausa para o usuário ler



