class Tamagoshi:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0
        self.saude = 100
        self.idade = 0
        self.tedio = 0
        self.energia = 100  
        self.dormindo = False  

    def alimentar(self, quantidade):
        if (quantidade >= 0) and (quantidade <= 100):
            self.fome -= self.fome * (quantidade / 100)
            print("nhac nhac nhac... 😋😋😋😋")
            print(f"{self.nome} foi alimentada e agora tem fome {self.fome:.1f}")

    def brincar(self, quantidade):
        if (quantidade >= 0) and (quantidade <= 100):
            self.tedio -= self.tedio * (quantidade / 100)
            self.energia -= 5
            print("UIIIIIIIIIIIIIII 🤪")
            print(f"{self.nome} brincou e agora tem tédio {self.tedio:.1f}")

    def getHumor(self):
        return 100 - ((self.fome + self.tedio) / 2)

    def vida(self):
        if (self.fome > 50 and self.fome <= 60) or (self.tedio > 50 and self.tedio <= 60):
            self.saude -= 10
        elif (self.fome > 60 and self.fome <= 80) or (self.tedio > 60 and self.tedio <= 80):
            self.saude -= 30
        elif (self.fome > 80 and self.fome <= 90) or (self.tedio > 80 and self.tedio <= 90):
            self.saude -= 50
        elif (self.fome > 90) or (self.tedio > 90):
            self.saude -= 70
            print("Estou morrendo... AAAAAAAAH")
        elif (self.fome > 99) or (self.tedio > 99):
            self.saude = 0
            print("Sua bonequinha Tamagoshi morreu 😭")

    def tempoPassando(self):
        self.vida()
        self.idade += 0.2
        self.tedio += 2.5
        self.fome += 5
        self.energia -= 2

    def status(self):
        print(f"\n🌸 Status da {self.nome}:")
        print(f"Idade: {self.idade:.1f}")
        print(f"Fome: {self.fome:.1f}")
        print(f"Tédio: {self.tedio:.1f}")
        print(f"Saúde: {self.saude}")
        print(f"Energia: {self.energia}")
        print(f"Dormindo: {self.dormindo}")
        print("-"*30)

    
    def dormir(self):
        self.dormindo = True
        print(f"{self.nome} foi de berço... 😴")

    def acordar(self):
        self.dormindo = False
        print(f"Eita que a {self.nome} acordou cheia de energia! SLAYYYY🎇🎇🎇🎇")
        self.energia = 100

    def salvar_estado(self):
        tipo = type(self).__name__  # isso vai pegar o nome da classe (ex: "BarbieTamagoshi")
        with open("estado_tamagoshi.txt", "w") as f:
            f.write(f"{tipo};{self.nome};{self.fome};{self.saude};{self.idade};{self.tedio};{self.energia};{self.dormindo}\n")#pra salvar o estado em txt
    
            
            
    def carregar_tamagoshi_salvo():
        try:
            with open("estado_tamagoshi.txt", "r") as f:
                dados = f.readline().strip().split(";")
                tipo = dados[0]
                nome = dados[1]
                fome = float(dados[2])
                saude = int(dados[3])
                idade = float(dados[4])
                tedio = float(dados[5])
                energia = int(dados[6])
                dormindo = dados[7] == "True"

                # Cria o objeto correto
                if tipo == "BarbieTamagoshi":
                    bicho = BarbieTamagoshi(nome)
                elif tipo == "PollyTamagoshi":
                    bicho = PollyTamagoshi(nome)
                elif tipo == "MonsterHighTamagoshi":
                    bicho = MonsterHighTamagoshi(nome)
                else:
                    print("Tipo de Tamagoshi desconhecido.")
                    return None

                # Atribui os atributos salvos
                bicho.fome = fome
                bicho.saude = saude
                bicho.idade = idade
                bicho.tedio = tedio
                bicho.energia = energia
                bicho.dormindo = dormindo

                if dormindo:
                    bicho.acordar()

                return bicho

        except FileNotFoundError:
            return None



class BarbieTamagoshi(Tamagoshi):
    def __init__(self, nome):
        super().__init__(nome)
        self.elegancia = 50
        self.autoestima = 50

    def seArrumar(self):
        print(f"{self.nome} está se arrumando! 💄✨")
        self.elegancia += 10
        self.autoestima += 5

    def desfilar(self):
        print(f"{self.nome} está desfilando na passarela! 👠💃")
        print("UAUUUUU👏👏👏👏")
        self.autoestima += 15
        self.fome += 5
        self.tedio -= 5

    def cantar(self):
        print(f"{self.nome} está cantando! 🎤🎶")
        print("ARRASA DIVA! 🥳🥳🥳")
        self.autoestima += 10
        self.tedio -= 10
        self.saude -= 5


class PollyTamagoshi(Tamagoshi):
    def __init__(self, nome):
        super().__init__(nome)
        self.aventura = 50
        self.criatividade = 50

    def explorar(self):
        print(f"{self.nome} saiu para explorar o mundo! 🌍")
        self.aventura += 15
        self.fome += 10
        self.energia -= 10

    def inventarBrincadeira(self):
        print(f"{self.nome} inventou uma nova brincadeira! Ela é muito criativa né? 🧸")
        self.criatividade += 20
        self.tedio -= 15

    def andarPatins(self):
        print(f"{self.nome} está andando de patins! 🛼")
        self.aventura += 10
        self.tedio -= 20
        self.saude -= 5
        self.energia -= 15


class MonsterHighTamagoshi(Tamagoshi):
    def __init__(self, nome):
        super().__init__(nome)
        self.estilo = 50
        self.poderSombrio = 50

    def transformar(self):
        print(f"{self.nome} se transformou em morcego! 🦇")
        self.poderSombrio += 20
        self.saude -= 10

    def assustar(self):
        print(f"{self.nome} assustou todo mundo! Ela é muito doidinha 👻")
        self.estilo += 10
        self.tedio -= 20

    def ritual(self):
        print(f"{self.nome} realizou um ritual misterioso... 🔮")
        self.saude += 20
        self.fome += 15


def main():
    bicho = Tamagoshi.carregar_tamagoshi_salvo()

    if bicho:
        print(f"\n✨ Encontramos um bichinho salvo: {bicho.nome} ({type(bicho).__name__})")
        resposta = input("Você quer continuar com esse bichinho? (s/n): ").lower() #s voce po em maiusculo ja converte TECNOLOOGIA

        if resposta != "s":
            bicho = None

    if not bicho:
        print("✨ Escolha sua bonequinha Tamagoshi ✨")
        print("1 - Barbie")
        print("2 - Polly")
        print("3 - Monster High")

        escolha = input("Digite o número: ")
        nome = input("Digite o nome da sua bonequinha: ")

        if escolha == "1":
            bicho = BarbieTamagoshi(nome)
        elif escolha == "2":
            bicho = PollyTamagoshi(nome)
        elif escolha == "3":
            bicho = MonsterHighTamagoshi(nome)
        else:
            print("Opção inválida... 🫢")
            bicho = Tamagoshi(nome)

    while True:
        print("\nO que você quer fazer?")
        print("1 - Alimentar")
        print("2 - Brincar")
        print("3 - Ações especiais")
        print("4 - Mostrar status")
        print("5 - Passar o tempo")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            bicho.alimentar(50)

        elif opcao == "2":
            bicho.brincar(50)

        elif opcao == "3":
            # 🎀 Menu da Barbie
            if isinstance(bicho, BarbieTamagoshi): #o isinstance vai fazer uma verificação pra saber qual bichinho eu tenho"
                print("\n🎀 Menu da Barbie 🎀")
                print("1 - Se arrumar")
                print("2 - Desfilar")
                print("3 - Cantar")
                escolha_barbie = input("Escolha: ")
                if escolha_barbie == "1":
                    bicho.seArrumar()
                elif escolha_barbie == "2":
                    bicho.desfilar()
                elif escolha_barbie == "3":
                    bicho.cantar()
                else:
                    print("Opção inválida!")

            # 🌟 Menu da Polly
            elif isinstance(bicho, PollyTamagoshi):
                print("\n🌟 Menu da Polly 🌟")
                print("1 - Explorar")
                print("2 - Inventar brincadeira")
                print("3 - Andar de patins")
                escolha_polly = input("Escolha: ")
                if escolha_polly == "1":
                    bicho.explorar()
                elif escolha_polly == "2":
                    bicho.inventarBrincadeira()
                elif escolha_polly == "3":
                    bicho.andarPatins()
                else:
                    print("Opção inválida!")

            # 🕸️ Menu da Monster High
            elif isinstance(bicho, MonsterHighTamagoshi):
                print("\n🕸️ Menu da Monster High 🕸️")
                print("1 - Transformar")
                print("2 - Assustar")
                print("3 - Ritual")
                escolha_mh = input("Escolha: ")
                if escolha_mh == "1":
                    bicho.transformar()
                elif escolha_mh == "2":
                    bicho.assustar()
                elif escolha_mh == "3":
                    bicho.ritual()
                else:
                    print("Opção inválida!")

        elif opcao == "4":
            bicho.status()

        elif opcao == "5":
            bicho.tempoPassando()

        elif opcao == "0":
            bicho.dormir()
            bicho.salvar_estado()
            print("💾 Estado salvo! Até mais! 👋")
            break

        else:
            print("Opção inválida!")
            
main()            
                        
