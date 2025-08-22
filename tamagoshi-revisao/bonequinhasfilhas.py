from bonecamae import Tamagoshi

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
        print("\nSou a Barbie Girl,")
        print("Se você quer ser meu namorado, fica ligado")
        print("Presta atenção na minha condição")
        print("É diferente, sou muito exigente")
        print("-------------------------------------")
        print("ARRASA DIVA! 🥳🥳🥳")
        self.autoestima += 10
        self.tedio -= 10
        self.saude -= 5

    def fazerFotos(self):
        print(f"{self.nome} está fazendo um ensaio fotográfico super fashion! 📸✨")
        self.elegancia = min(self.elegancia + 15, 100)
        self.autoestima = min(self.autoestima + 10, 100)
        self.energia = max(self.energia - 10, 0)
        print(f"Elegância agora: {self.elegancia}, Autoestima agora: {self.autoestima}")

    def fazerSpa(self):
        print(f"{self.nome} está relaxando no spa! 💆‍♀️💖")
        self.saude = min(self.saude + 20, 100)
        self.tedio = max(self.tedio - 10, 0)
        self.energia = min(self.energia + 15, 100)
        print(f"Saúde: {self.saude}, Tédio: {self.tedio}, Energia: {self.energia}")
        


class PollyTamagoshi(Tamagoshi):
    def __init__(self, nome):
        super().__init__(nome)
        self.aventura = 50
        self.criatividade = 50

    def explorar(self):
        print(f"{self.nome} saiu para explorar o mundo! Bem vibe dora aventureira AMO!🌍")
        self.aventura += 15
        self.fome += 10
        self.energia -= 10

    def inventarBrincadeira(self):
        print(f"{self.nome} inventou uma nova brincadeira! Parabéns meu amor, você é muito criativa mesmo né! 🧸")
        self.criatividade += 20
        self.tedio -= 15

    def andarPatins(self):
        print(f"{self.nome} está andando de patins! Bem radical essa bonequinha 🤟👧🏼")
        self.aventura += 10
        self.tedio -= 20
        self.saude -= 5
        self.energia -= 15

    def acampar(self):
        print(f"{self.nome} foi acampar na floresta! 🏕️🔥")
        self.aventura = min(self.aventura + 20, 100)
        self.saude = max(self.saude - 5, 0)
        self.energia = max(self.energia - 15, 0)
        self.tedio = max(self.tedio - 10, 0)
        print(f"Aventura: {self.aventura}, Saúde: {self.saude}, Energia: {self.energia}")

    def criarObraArte(self):
        print(f"{self.nome} criou uma obra de arte incrível! 🎨🖌️")
        self.criatividade = min(self.criatividade + 25, 100)
        self.autoestima = getattr(self, 'autoestima', 50)
        self.tedio = max(self.tedio - 20, 0)
        print(f"Criatividade: {self.criatividade}, Tédio: {self.tedio}")
    


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

    def invocarFamilia(self):
        print(f"{self.nome} invocou sua família sombria para uma reunião! 🕸️🦇")
        self.poderSombrio = min(self.poderSombrio + 25, 100)
        self.saude = max(self.saude - 10, 0)
        self.tedio = max(self.tedio - 15, 0)
        print(f"Poder Sombrio: {self.poderSombrio}, Saúde: {self.saude}")

    def dançarMacabra(self):
        print(f"{self.nome} está dançando a dança macabra! 💃🖤")
        self.estilo = min(self.estilo + 15, 100)
        self.energia = max(self.energia - 20, 0)
        self.tedio = max(self.tedio - 10, 0)
        print(f"Estilo: {self.estilo}, Energia: {self.energia}")
    