from bonecamae import Tamagoshi
from bonequinhasfilhas import PollyTamagoshi, BarbieTamagoshi, MonsterHighTamagoshi
import time

def main():
    bicho = Tamagoshi.carregar_tamagoshi_salvo()

    if bicho:
        print(f"\n✨ Encontramos um bichinho salvo: {bicho.nome} ({type(bicho).__name__})")
        resposta = input("Você quer continuar com esse bichinho? (s/n): ").lower() #s voce po em maiusculo ja converte TECNOLOOGIA

        if resposta != "s":
            bicho = None

    if not bicho:
        print("\n 💗Olá! Seja bem vindo(a) a fábrica de Bonequinhas Tamagoshis da Helo!💗\n")
        print("✨ Escolha o tipo da sua bonequinha Tamagoshi ✨")
        print("1 - Barbie")
        print("2 - Polly")
        print("3 - Monster High")

        escolha = input("Digite o número: ")
        nome = input("Escolha o nome da sua bonequinha: ")

        print(f"\n{nome} está sendo criada", end="")
        for _ in range(3):
            time.sleep(0.6)
            print(".", end="", flush=True)
        time.sleep(1)

        if escolha == "1":
            bicho = BarbieTamagoshi(nome)
        elif escolha == "2":
            bicho = PollyTamagoshi(nome)
        elif escolha == "3":
            bicho = MonsterHighTamagoshi(nome)
        else:
            print("Opção inválida... 🫢")
            bicho = Tamagoshi(nome)

        time.sleep(0.8)
        print("\n🎉✨", end=" ")
        if isinstance(bicho, BarbieTamagoshi):
            print(f"{nome} nasceu toda fashionista direto da fábrica da Barbie! 💄👛")
        elif isinstance(bicho, PollyTamagoshi):
            print(f"{nome} nasceu cheia de energia e pronta pra se aventurar!🙈")
        elif isinstance(bicho, MonsterHighTamagoshi):
            print(f"{nome} saiu das sombras direto do colégio Monster High! 🦇🕸️")
        else:
            print(f"{nome} nasceu! Cuide bem dela! 🐣💗")
        time.sleep(1.2)    

        print("\n📜 Regrinhas para cuidar da sua bonequinha Tamagoshi 💖")
        print("-" * 50)
        print("1️⃣ Alimente, brinque e deixe sua bonequinha dormir.")
        print("2️⃣ Fique de olho nos status: fome, tédio, energia e saúde.")
        print("3️⃣ Se você deixar ela com muita fome ou tédio, a saúde dela vai cair!")
        print("4️⃣ Se a saúde chegar a 0... ela vai morrer 😭")
        print("5️⃣ Use o menu para interagir com sua bonequinha e mantê-la feliz!")
        print("-" * 50)
        time.sleep(2)

    while True:
        print("\nO que você quer fazer?")
        print("1 - Alimentar ")
        print("2 - Brincar ")
        print("3 - Ações especiais ")
        print("4 - Mostrar status ")
        print("5 - Passar o tempo")
        print("6 - Criar pet para sua bonequinha")
        print("7 - Ver pet da sua bonequinha")
        print("8 - Ver conquistas desbloqueadas ")
        print("9 - Dar banho na bonequinha ")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            try:
                quantidade = int(input("🍽️ Quanto você deseja alimentar sua bonequinha? (0-100): "))
                if quantidade >= 0 and quantidade <= 100 :
                    bicho.alimentar(quantidade)
                else:
                    print("Por favor, digite um valor entre 0 e 100.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

        elif opcao == "2":
            try:
                quantidade = int(input("🎲 Quanto tempo você quer brincar com sua bonequinha? (0-100): "))
                if quantidade >=0 and quantidade <=100 :
                    bicho.brincar(quantidade)
                else:
                    print("Por favor, digite um valor entre 0 e 100.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

        elif opcao == "3":
            # 🎀 Menu da Barbie
            if isinstance(bicho, BarbieTamagoshi): #o isinstance vai fazer uma verificação pra saber qual bichinho eu tenho"
                print("\n🎀 Menu da Barbie 🎀")
                print("1 - Se arrumar")
                print("2 - Desfilar")
                print("3 - Cantar")
                print("4 - Tirar fot0")
                escolha_barbie = input("Escolha: ")
                if escolha_barbie == "1":
                    bicho.seArrumar()
                elif escolha_barbie == "2":
                    bicho.desfilar()
                elif escolha_barbie == "3":
                    bicho.cantar()
                elif escolha_barbie == "4":
                    bicho.fazerFotos()    
                elif escolha_barbie == "5":
                    bicho.fazerSpa()   
                else:
                    print("Opção inválida!")

            # 🌟 Menu da Polly
            elif isinstance(bicho, PollyTamagoshi):
                print("\n🌟 Menu da Polly 🌟")
                print("1 - Explorar")
                print("2 - Inventar brincadeira")
                print("3 - Andar de patins")
                print("4 - Acampar com os bests")
                print("5 - Criar uma nova obra de arte")
                escolha_polly = input("Escolha: ")
                if escolha_polly == "1":
                    bicho.explorar()
                elif escolha_polly == "2":
                    bicho.inventarBrincadeira()
                elif escolha_polly == "3":
                    bicho.andarPatins()
                elif escolha_polly == "4":
                    bicho.acampar()    
                elif escolha_polly == "5":
                    bicho.criarObraArte()

                else:
                    print("Opção inválida!")

            # 🕸️ Menu da Monster High
            elif isinstance(bicho, MonsterHighTamagoshi):
                print("\n🕸️ Menu da Monster High 🕸️")
                print("1 - Transformar")
                print("2 - Assustar")
                print("3 - Ritual")
                print("4 - Chamar a familia")
                print("5 - Dançar")
                escolha_mh = input("Escolha: ")
                if escolha_mh == "1":
                    bicho.transformar()
                elif escolha_mh == "2":
                    bicho.assustar()
                elif escolha_mh == "3":
                    bicho.ritual()
                elif escolha_mh == "4":
                    bicho.invocarFamilia()
                elif escolha_mh == "5":
                    bicho.dançarMacabra()
                else:
                    print("Opção inválida!")

        elif opcao == "4":
            bicho.status()

        elif opcao == "5":
            bicho.tempoPassando()

        elif opcao == "6":
            bicho.criar_animalzinho()

        elif opcao == "7":
            bicho.mostrar_animalzinho()

        elif opcao == "8":
            bicho.verificar_conquistas()
    
            
        elif opcao == "0":
            bicho.dormir()
            bicho.salvar_estado()
            print("💾 Estado salvo! Até mais! 👋")
            break

        else:
            print("Opção inválida!")
            
main()            
                        

                        
