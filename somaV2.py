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

        qtd_dados = int(input("Informe quantos dados são: "))

        soma_total = 0  # Inicializa a variável para acumular a soma

        for i in range(qtd_dados):
            numero_aleatorio = random.randint(1, faces_dados)
            soma_total += numero_aleatorio
            print("O valor do Dado", i  + 1,"é:",numero_aleatorio)
            
        
        print("O resultado da soma é:", soma_total)   

        jogar_novamente = input("Deseja jogar novamente? (s/n): ").strip().lower()
        if jogar_novamente == 's':
            continue
        os.system('cls')
        print("Obrigado por jogar! Até a próxima!")
        break  # Sai do loop após exibir o resultado



    except ValueError:
        print("Entrada inválida! Por favor, insira um número inteiro.")
        input("Pressione Enter para tentar novamente...")  # Pausa para o usuário ler



