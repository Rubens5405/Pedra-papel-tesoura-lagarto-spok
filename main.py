from modo_história import introdução
from jogar import versus_cpu
from versus import versus_player

print("Escolha seu modo de jogo:")

while True:
    opcoes = input("\nModo História (Somente introdução) - 1 \nContra o Computador - 2\nVersus Local -"\
" 3 \nSair do jogo - 4\n")
    
    if opcoes == "1":
        introdução()

    elif opcoes == "2":
        versus_cpu()

    elif opcoes =="3":
        versus_player()

    elif opcoes == "4":
        break

    else: 
        print("Opção inválida!")
