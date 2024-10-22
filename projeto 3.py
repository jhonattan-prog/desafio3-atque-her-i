class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo


    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}\nIdade: {self.idade}\nTipo: {self.tipo}")
    
    def atacar(self):
        if self.tipo == "mago":
            ataque = "magia"
        elif self.tipo == "guerreiro":
            ataque = "espada"
        elif self.tipo == "monge":
            ataque = "artes marciais"
        elif self.tipo == "ninja":
            ataque = "shuriken"
        else:
            ataque = "realizou um ataque desconhecido"

        
        print(f"{self.nome} o {self.tipo}, atacou usando {ataque}")

heroi1 = Heroi("Gandalf", 150, "mago")
heroi2 = Heroi("Conan", 35, "guerreiro")
heroi3 = Heroi("Bruce Lee", 32, "monge")
heroi4 = Heroi("Ryu Hayabusa", 28, "ninja")



heroi_escolhido = input("Escolha o nome do herói (Gandalf, Conan, Bruce Lee, Ryu Hayabusa): ").lower()

if heroi_escolhido == "gandalf":
    heroi_selecionado = heroi1
elif heroi_escolhido == "conan":
    heroi_selecionado = heroi2
elif heroi_escolhido == "bruce lee":
    heroi_selecionado = heroi3
elif heroi_escolhido == "ryu hayabusa":
    heroi_selecionado = heroi4
else:
    heroi_selecionado = None
    print("Herói não encontrado.")


if heroi_selecionado:
    escolha = input("Você quer ver as informações do herói antes do ataque? (sim/não): ").lower()

    if escolha == "sim":
        heroi_selecionado.mostrar_informacoes()

    
    atacar = input("Você deseja atacar? (sim/não): ").lower()

    if atacar == "sim":
        heroi_selecionado.atacar()
    else:
        print(f"{heroi_selecionado.nome} decidiu não atacar.") 
else:
    print("Não foi possível realizar a ação devido à escolha inválida.")