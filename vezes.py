import random
import os

while True:
    os.system('cls')

    try:
        faces_dados = int(input("Informe quantas faces tem os dados que você gostaria de mutiplicar: "))

        if faces_dados <= 1:
            print("Valor inválido! O número de faces deve ser maior que 1.")
            input("Pressione Enter para tentar novamente...")  # Pausa para o usuário ler
            continue  # Volta ao início do loop

        qtd_vezes = int(input("Informe vezes você gostaria de multiplicar: "))

        numero_aleatorio = random.randint(1, faces_dados)

        print("")
        print("---------------------------------------------------------------------------")   
        print("")         

        print("O valor do Dado é:",numero_aleatorio,"ele sera multiplicado por",qtd_vezes)

        resultado = numero_aleatorio * qtd_vezes
        
        print("O resultado da mutiplicção é:", resultado)   

        jogar_novamente = input("Deseja jogar novamente? (s/n): ").strip().lower()
        if jogar_novamente == 's':
            continue
        os.system('cls')
        print("Obrigado por jogar! Até a próxima!")
        break  # Sai do loop após exibir o resultado



    except ValueError:
        print("Entrada inválida! Por favor, insira um número inteiro.")
        input("Pressione Enter para tentar novamente...")  # Pausa para o usuário ler



