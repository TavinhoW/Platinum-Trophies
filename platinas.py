import os # pega a biblioteca para limpar a consola
import platform # pega a biblioteca para ver em que sistema operativo estas (windows/linux)

# Localização do ficheiro (alterar no pc diferente)
file_path = '...'

# Função para limpar a consola (diferente se caso estiveres no windows ou no linux)
def clear_console():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

# Função para ler jogos do ficheiro e carregar na lista
def carregar_jogos():
    if os.path.exists(file_path):  # Verifica se o arquivo existe
        with open(file_path) as file: # se existir vai abrir o ficheiro na localização escrita 
            return sorted([linha.strip() for linha in file.readlines()])  # Vai remover as quebras de linha e meter os jogos na lista que estavam no ficheiro guardado e mete em ordem alfabetica
    return [] # se nao existir RIP

# Função para salvar a lista de jogos no ficheiro
def salvar_jogos(platina):
    with open(file_path, 'w') as file: # se existir vai abrir o ficheiro na localização escrita 
        for jogo in platina: # por cada jogo na lista
            file.write(jogo + '\n')  # Escreve cada jogo em uma nova linha no ficheiro

# Função para adicionar um jogo no ficheiro e na lista
def adicionar_jogo(jogo):
    platina.append(jogo)  # Adiciona a lista o jogo
    with open(file_path, 'a') as file: # se existir vai abrir o ficheiro na localização escrita 
        file.write(jogo + '\n')  # Adiciona o novo jogo no final do arquivo

# Função para remover um jogo da lista e do ficheiro
def remover_jogo(jogo):
    if jogo in platina:
        platina.remove(jogo)  # Remove da lista
        salvar_jogos(platina)  # muda o ficheiro de acordo com o que foi escrito de novo para estar sempre atualizado

# Lista de jogos para platinar
platina = carregar_jogos()  # Carregar jogos já presentes no ficheiro

# Menu Principal
while True:
    clear_console()
    print("\nPlaystation Platinums\nMade by: Tavinho\n\n\n1. Platinar (Jogos que tenho)\n2. Sair\n\n\nPSN: TavinhoKillerPT\n")
    
    try: # Verificação, ver se escreves um numero ou uma letra ou um numero nao desejado
        escolha_menu_0 = int(input())
    except ValueError:
        print("Por favor, insira um número válido.")
        input("Pressione Enter para continuar...")
        continue

    if escolha_menu_0 == 1: # se 1 vai para o menu principal
        while True:
            clear_console()

            print("\nPlaystation Platinums\nMade by: Tavinho\nPlatinar (Jogos que tenho)\n\n\n1. Ver Jogos para Platinar\n2. Adicionar Jogos para Platinar\n3. Remover Jogos para Platinar\n4. Voltar\n\n\nPSN: TavinhoKillerPT\n")

            try:
                escolha_menu_1 = int(input())
            except ValueError:
                print("Por favor, insira um número válido.")
                input("Pressione Enter para continuar...")
                continue

            if escolha_menu_1 == 1: # se 1 vai mostrar os jogos
                clear_console()
                print("\nPlaystation Platinums\nMade by: Tavinho\nPlatinar (Jogos que tenho)\n\n")
                
                if not platina: # se nao houver nenhum jogo na lista platina
                    print("Nenhum jogo adicionado ainda.")
                else: # se houver algum jogo
                    for jogo in platina: # por cada jogo que houver na lista platina vai digitar o jogo
                        print(jogo)

                print("\n\nDigite alguma coisa para avançar para a frente\n\nPSN: TavinhoKillerPT\n")
                input()

            elif escolha_menu_1 == 2: # se 2 vais adicionar um jogo a lista platina e depois ao ficheiro
                clear_console()
                print("\nPlaystation Platinums\nMade by: Tavinho\nAdicionar Platina (Jogos que tenho)\n\nDigite o nome do jogo para platinar\n\n")
                jogo = input()

                if jogo: # verificar se escreves alguma coisa ou se apenas deixaste em branco

                    exist_jogo = jogo.lower()
                    jogo_existe = False

                    for existente_jogo in platina: # Para verificar se o jogo ja existe no fichiero ou nao
                        if exist_jogo == existente_jogo.lower(): # cria uma variavel a dizer que é igual a variavel mas a meter em letras pequenas para nao haver casos de jgoos com letras mairoes q outras e isso
                            print("Jogo já existe\n\nDigite alguma coisa para voltar atras")
                            jogo_existe = True # mete true q significa q vais embora
                            break

                    if (jogo_existe == False): # se for false que signficia que nada é igual prosegue para este if e finalmente adiciona o jogo a lista e ao ficheiro
                        adicionar_jogo(jogo)  # Chama a função para adicionar o jogo ao ficheiro
                        print("Jogo" , jogo , "adicionado com sucesso!")

                else:
                    print("Nome do jogo inválido.")
                input("Pressione Enter para continuar...") # se escreves nada de jeito volta ao menu principal

            elif escolha_menu_1 == 3: # se 3 vais remover o jogo da lista platina e depois remover do ficheiro
                clear_console()
                print("\nPlaystation Platinums\nMade by: Tavinho\nRemover Platina\n(Digite o nome do jogo para remover da lista)\n\n")
                
                if not platina: # se nao escreveste nada nao vai remover nada e vai voltar para o menu principal
                    print("Nenhum jogo para remover.")
                else:
                    for jogo in platina:
                        print(jogo)

                    remover_jogo_input = input("\nDigite o nome do jogo que deseja remover:\n")

                    if remover_jogo_input in platina:
                        remover_jogo(remover_jogo_input)  # Chama a função para remover o jogo do ficheiro
                        print("Jogo" , remover_jogo_input , "removido com sucesso!")
                    else:
                        print("Jogo não encontrado na lista.")

                input("Pressione Enter para continuar...")

            elif escolha_menu_1 == 4: # se 4 vai voltar ao menu do inicio
                break

            else:
                print("Opção inválida, tente novamente.")
                input("Pressione Enter para continuar...")

    elif escolha_menu_0 == 2: # se 2 vai sair do programa
        print("\nSaindo do Programa\n")
        break

    else: # resposta errada tens lag
        print("Resposta inválida.")
        input("Pressione Enter para continuar...")
