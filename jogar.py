def versus_cpu(): 
    from oponentes import Sheldon, Monarca, Sósia, Spock, dialogo_especial
    from jogo import Jogo
    import random

    escolhas = ["pedra", "papel", "tesoura", "lagarto", "spock"]
    oponentes = ["Sheldon", "Monarca", "Spock", "Sósia"]

    rival = random.choice(oponentes)
    pontos_jogador = 0
    pontos_rival = 0
    jogada_rival = random.choice(escolhas)

    def verificação():
        escolha = input("Escolha entre Pedra, Papel, Tesoura, Lagarto ou Spock: ").lower()
        while escolha not in escolhas:
            print("Opção inválida.")
            escolha = input("Tente novamente: ").lower()
        return escolha

    for rodada in range(5):
        opcao = verificação()

        #Condição de Rival
        if rival == "Sheldon":
            jogada_rival = Sheldon(rodada+1)
    
        resultado = Jogo(opcao, jogada_rival)
        if resultado == "Você venceu!":
            pontos_jogador += 1
        elif resultado == "Você perdeu!":
            pontos_rival += 1

        print(f"{rodada + 1}ª rodada:")
        print(resultado)
        print(f"{pontos_jogador}  X  {pontos_rival}")
        print(f"Seu opononente jogou: {jogada_rival}")
        dialogo_especial(rodada + 1, rival, pontos_jogador, pontos_rival)
        print(" ")

        #Condição de Rival
        if rival == "Monarca":
            jogada_rival = Monarca(opcao)
        if rival == "Sósia":
            jogada_rival = Sósia(opcao)
        if rival == "Spock":
            jogada_rival = Spock(pontos_jogador, pontos_rival)

    print(f"Seu oponente era: {rival}")
    print(f"\nVocê  X  {rival} \n  {pontos_jogador}   X   {pontos_rival}")
