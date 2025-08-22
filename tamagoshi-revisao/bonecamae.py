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
        if quantidade >=0 and quantidade <=100 :
            self.fome -= quantidade
            if self.fome < 0:
                self.fome = 0
            print("nhac nhac nhac... 😋😋😋😋")
            print(f"{self.nome} foi alimentada e agora tem fome {self.fome:.1f}")
            
    def brincar(self, quantidade):
        if quantidade >=0 and quantidade <=100 :
            self.tedio -= quantidade
            self.fome += 10
            self.energia -= 5
            if self.tedio < 0:
                self.tedio = 0
            print("UIIIIIIIIIIIIIII 🤪")
            print(f"{self.nome} brincou e agora tem tédio {self.tedio:.1f}")


    
    def vida(self):
        if (50 < self.fome <= 60) or (50 < self.tedio <= 60):
            self.saude -= 10
        elif (60 < self.fome <= 80) or (60 < self.tedio <= 80):
            self.saude -= 30
        elif (80 < self.fome <= 90) or (80 < self.tedio <= 90):
            self.saude -= 50
        elif (self.fome > 90) or (self.tedio > 90):
            self.saude -= 70

        # aqui garante que saúde não fique negativa
        if self.saude < 0:
            self.saude = 0

        if 0 < self.saude <= 30:
            print("Estou morrendo... AAAAAAAAH")

        if self.saude == 0:
            print("Sua bonequinha Tamagoshi morreu 😭")



    def tempoPassando(self):
        self.idade += 5
        self.tedio += 2.5
        self.fome += 5
        self.energia -= 5
        self.saude -=10
        
        self.fome = min(max(self.fome, 0), 100)
        self.tedio = min(max(self.tedio, 0), 100)
        self.energia = min(max(self.energia, 0), 100)

      
        self.vida()


    def status(self):
        print(f"\n🌸 Status da {self.nome}:")
        print(f"Idade: {self.idade:.1f}")
        print(f"Fome: {min(max(self.fome, 0), 100):.1f}")
        print(f"Tédio: {min(max(self.tedio, 0), 100):.1f}")
        print(f"Saúde: {min(max(self.saude, 0), 100)}")
        print(f"Energia: {min(max(self.energia, 0), 100)}")
        print(f"Dormindo: {self.dormindo}")
        print("-" * 30)


    
    def dormir(self):
        self.dormindo = True
        print(f"{self.nome} foi de berço... 😴")

    def acordar(self):
        self.dormindo = False
        print(f"Eita que a {self.nome} acordou cheia de energia! SLAYYYY🎇🎇🎇🎇")
        self.energia = 100

    def criar_animalzinho(self):
        print(f"\nVamos criar um pet para {self.nome} 🐾")

        tipo = input("Tipo do pet (ex: cachorro, gato, coelho): ").strip()
        cor = input("Cor do pet: ").strip()
        acessorio = input("Acessório do pet (ex: laço, óculos, gravata): ").strip()
        nome = input("Nome do pet: ").strip()

        self.animalzinho = {
            "tipo": tipo,
            "cor": cor,
            "acessorio": acessorio,
            "nome": nome
        }

        print(f"\n🎉 {self.nome} agora tem um pet chamado {nome}! 🐶🐱🐰")
        print(f"É um {tipo} {cor} com {acessorio}. Que fofura! 🥰")
        
    def mostrar_animalzinho(self):
        if hasattr(self, 'animalzinho'):
            pet = self.animalzinho
            print(f"\n🐾 Pet da {self.nome}:")
            print(f"Nome: {pet['nome']}")
            print(f"Tipo: {pet['tipo']}")
            print(f"Cor: {pet['cor']}")
            print(f"Acessório: {pet['acessorio']}")
        else:
            print(f"{self.nome} ainda não tem um pet! 😢")

    def verificar_conquistas(self):
        from bonequinhasfilhas import BarbieTamagoshi, PollyTamagoshi, MonsterHighTamagoshi
        conquistas = []

        if self.idade >= 50:
            conquistas.append("👵 Idosa fashion: sua bonequinha viveu bastante!")

        if self.saude == 100:
            conquistas.append("💖 Bonequinha saudável: saúde perfeita!")

        if self.tedio == 0:
            conquistas.append("🎉 Nunca entediada: tédio zerado!")

        if self.fome == 0:
            conquistas.append("🍽️ Barriguinha cheia: fome zerada!")

        if hasattr(self, 'animalzinho'):
            conquistas.append("🐶 Mãe de pet: você criou um animalzinho!")

        if isinstance(self, BarbieTamagoshi):
            if getattr(self, 'elegancia', 0) >= 100:
                conquistas.append("💅 Rainha da Elegância: chegou a 100 de elegância!")
        elif isinstance(self, PollyTamagoshi):
            if getattr(self, 'aventura', 0) >= 100:
                conquistas.append("🛹 Exploradora Profissional: 100 de aventura!")
        elif isinstance(self, MonsterHighTamagoshi):
            if getattr(self, 'poderSombrio', 0) >= 100:
                conquistas.append("🧛 Rainha das Trevas: 100 de poder sombrio!")

        if conquistas:
            print("\n🏅 Conquistas desbloqueadas:")
            for c in conquistas:
                print(f"✅ {c}")
        else:
            print("\nNenhuma conquista desbloqueada ainda 😢 Continue cuidando dela!")
            
    def tomar_banho(self):
        print(f"\n🛁 Que tipo de banho você quer dar para {self.nome}?")
        print("1 - Banho de espuma (aumenta autoestima)")
        print("2 - Banho de pétalas (cura saúde)")
        print("3 - Banho rápido (reduz tédio)")

        escolha = input("Escolha o número do banho: ")

        if escolha == "1":
            print(f"{self.nome} está tomando um banho de espuma... 🛁✨")
            if hasattr(self, 'autoestima'):
                self.autoestima = min(self.autoestima + 15, 100)
                print(f"Autoestima de {self.nome} aumentou para {self.autoestima}!")
            else:
                print(f"{self.nome} adorou o banho, mas não tem autoestima para melhorar 😅")

            self.saude = min(self.saude + 5, 100)
            self.energia = max(self.energia - 5, 0)

        elif escolha == "2":
            print(f"{self.nome} está tomando um banho de pétalas... 🌸🌺")
            self.saude = min(self.saude + 20, 100)
            self.energia = max(self.energia - 10, 0)
            self.tedio = max(self.tedio - 5, 0)
            print(f"Saúde de {self.nome} melhorou para {self.saude}!")

        elif escolha == "3":
            print(f"{self.nome} está tomando um banho rápido... 🚿")
            self.tedio = max(self.tedio - 15, 0)
            self.energia = max(self.energia - 5, 0)
            print(f"Tédio de {self.nome} diminuiu para {self.tedio}!")

        else:
            print("Opção inválida. Nenhum banho foi tomado.")
            return

        print(f"{self.nome} está limpinha e renovada! Nada de banho só aos sabados hein✨")

        


    def salvar_estado(self):
        tipo = type(self).__name__  # isso vai pegar o nome da classe (ex: "BarbieTamagoshi")
        with open("estado_tamagoshi.txt", "w") as f:
            f.write(f"{tipo};{self.nome};{self.fome};{self.saude};{self.idade};{self.tedio};{self.energia};{self.dormindo}\n")#pra salvar o estado em txt
    
            
    @staticmethod       
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

                
                if tipo == "BarbieTamagoshi":
                    from bonequinhasfilhas import BarbieTamagoshi
                    bicho = BarbieTamagoshi(nome)
                elif tipo == "PollyTamagoshi":
                    from bonequinhasfilhas import PollyTamagoshi
                    bicho = PollyTamagoshi(nome)
                elif tipo == "MonsterHighTamagoshi":
                    from bonequinhasfilhas import MonsterHighTamagoshi
                    bicho = MonsterHighTamagoshi(nome)
                else:
                    print("Tipo de Tamagoshi desconhecido.")
                    return None

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
