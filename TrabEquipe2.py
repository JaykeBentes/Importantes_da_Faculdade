#Exercicio 1:
class Funcionario:
    
    def __init__(self, nome,salario):
        self.nome=nome
        self._salario=salario
    
    def addAumento(self,adicional):
        print(f"O funcionário(a) {self.nome} recebeu um aumento de: R${adicional} no seu salário de R${self._salario}.")
        self._novoSalario= self._salario+adicional
        return self._novoSalario
    
    def ganhoAnual(self):
        return f"Anualmente o funcionário(a) ganha: R${self._novoSalario*13}."
    
    def exibeDados(self):
        return f"O funcionário(a): {self.nome}, ganhou uma promoção de cargo e seu salário mensal foi de R${self._salario} para R${self._novoSalario} mensalmente."
        
class Assistente(Funcionario):
    
    def __init__(self,nome,salario,matricula):
        super().__init__(nome,salario)
        self._matricula=matricula
        
    def get_nome(self):
        return self.nome
    
    def set_nome(self, nome):
        self.nome=nome
        
    def get_matricula(self):
        return self._matricula
        
    def set_matricula(self, matricula):
        self._matricula=matricula 
    
    def exibeDados(self):
        return f"O funcionário(a) {self.nome} de matrícula n° {self._matricula}, possui um salário de R${self._salario}."
        
class Tecnico(Assistente):
    
    def __init__(self,nome,salario,matricula,bonus):
        super().__init__(nome,salario,matricula)
        self.bonus=bonus
        
    def ganhoAnual(self):
        print(f"O(A) assistente técnico {self.nome} de matrícula {self._matricula} ganha anualmente R${(self._salario+self.bonus)*13}.")
        
class Admnistrativo(Assistente):
    
    def __init__(self,nome,salario,matricula,turno=True):
        super().__init__(nome,salario,matricula)
        self.turno=turno
        
    def ganhoAnual(self):
        if self.turno:
            print(f"O(A) assistente administrativo {self.nome} de matrícula {self._matricula} recebe anualmente R${(self._salario+1000)*13}.")
        else:
            print(f"O(A) assistente administrativo {self.nome} de matrícula {self._matricula} recebe anualmente R${self._salario*13}.")
            
    def trocaTurno(self):
        self.turno=False
        return
        
meuFuncionario=Funcionario('Maria', 2500)
#meuFuncionario.addAumento(750)
#print(meuFuncionario.ganhoAnual())
#print(meuFuncionario.exibeDados())
meuAssistente=Assistente('João',4300,34343456)
#print(meuAssistente.exibeDados())
#meuAssistente.set_nome('Fulano')
#print(meuAssistente.get_nome())
meuAssistente.set_matricula(67576757)
#print(meuAssistente.get_matricula())
#print(meuAssistente.exibeDados())
tec1=Tecnico('Carlos',3800,92919394,500)
#tec1.ganhoAnual()
adm1=Admnistrativo('Zélia',5000,78797870)
#adm1.ganhoAnual()
#adm1.trocaTurno()
#adm1.ganhoAnual()

#Exercicio 2:
class Animal:
    
    def __init__(self,nome,raca):
        self.nome=nome
        self.raca=raca
        
    def listar(self):
        print(f"Este bichinho se chama {self.nome} e é da raça {self.raca}.")
        
    def caminhar (self):
        print(f"O(A) {self.nome} ama caminhar!")
        
class Cachorro(Animal):
    
    def __init__ (self, nome, raca):
        super().__init__(nome,raca)
        
    def latir(self):
        print("Au-Au")
        
class Gato(Animal):
    
    def __init__ (self, nome,raca):
        super().__init__(nome,raca)
        
    def miar(self):
        print("Miau!")
        
meuAnimal=Animal("Fiona","Ramster")
#meuAnimal.caminhar()
meuCachorro=Cachorro("Rex","Pintcher")
#meuCachorro.listar()
#meuCachorro.latir()
meuGato=Gato("Bart","Frajola")
#meuGato.listar()
#meuGato.miar()

class Pessoa:
    def __init__(self,nome,idade):
        self.nome=nome
        self.idade=idade
        
    def listar_Pessoa(self):
        return f"O(A) {self.nome} tem {self.idade} anos."
    
class Miseravel(Pessoa):
    def __init__(self,nome,idade):
        super().__init__(nome,idade)
        
    def mendigar(self):
        return f"'O(A) {self.nome} está mendigando para sobreviver."
    
class Pobre(Pessoa):
    def __init__(self,nome,idade):
        super().__init__(nome,idade)
        
    def trabalhar(self):
        return f'O(A) {self.nome} está trabalhando duro para sobreviver.'
    
class Rico(Pessoa):
    def __init__(self, nome, idade,dinheiro):
        super().__init__(nome, idade)
        self.dinheiro=dinheiro
        
    def fazCompras(self,valorCompra):
        self.dinheiroAtual = self.dinheiro-valorCompra
        return f'O(A) {self.nome} fez uma compra de R${valorCompra} e agora possui R${self.dinheiroAtual}'
    
pessoa1=Pessoa('Joao Carlos',29)
#print(pessoa1.listar_Pessoa())
miseravel2=Miseravel('Tiao',45)
#print(miseravel2.mendigar())
pobre3=Pobre('Sasa',22)
#print(pobre3.trabalhar())
rico4=Rico('Salvatore',37,2540300)
#print(rico4.fazCompras(50600))

#Exercicio 3:
class Ingresso():
    def __init__(self, valor):
        self.valor=valor
        
    def imprimeValor(self):
        pass
        
class Vip(Ingresso):
    def __init__(self, valor,adicional):
        super().__init__(valor)
        self.adicional=adicional
        
    def valorVip(self):
        ingressoVip=self.valor + self.adicional
        print(f"O valor do ingresso Vip é R${ingressoVip}")
    
class Normal(Ingresso):
    def __init__(self,valor):
        super().__init__(valor)
        
    def imprimeValor(self):
        print(f"O valor do ingresso Normal é R${self.valor}")

class CamaroteInf(Vip):
    def __init__(self, valor,adicional,cadeira, fileira):
        super().__init__(valor,adicional)
        self.cadeira=cadeira
        self.fileira=fileira
        
    def locIngressoCamInf(self):
        localizacao= str(self.cadeira)+self.fileira
        print(f"Ingresso da Cadeira Inferior referente a {localizacao}, e custa R${self.valor+self.adicional}.")
        
class CamaroteSup(Vip):
    def __init__(self,valor, adicional):
        super().__init__(valor,adicional)
        
    def valorCamSup(self):
        ingressoCamSup= self.valor + self.adicional
        print(f"O valor do ingresso Camarote Superior é R${ingressoCamSup}.")
        
meuVip=Vip(75,40)
#meuVip.valorVip()
meuIngresso=Normal(80)
#meuIngresso.imprimeValor()
meuCamInf=CamaroteInf(95,30,"15","B")
#meuCamInf.locIngressoCamInf()
meuCamSup=CamaroteSup(95,50)
#meuCamSup.valorCamSup()

#Exercicio 4:
class Imovel():
    
    def __init__(self,preco,endereco):
        self.preco=preco
        self.endereco=endereco
        
class Novo(Imovel):
    
    def __init__(self, preco,endereco,adicional):
        super().__init__(preco,endereco)
        self.adicional=adicional
        
    def valorNovo(self):
        novoPreco=self.preco+self.adicional
        print(f"O valor do Imóvel novo é R${novoPreco}; E ele se localiza em: {self.endereco}.")
        
class Velho(Imovel):
    
    def __init__(self,preco,endereco,desconto):
        super().__init__(preco,endereco)
        self.desconto=desconto
        
    def valorBaixo(self):
        precoDesconto=self.preco-self.desconto
        print(f"O valor do Imóvel mais antigo é R${precoDesconto}; E ele se localiza em: {self.endereco}.")
        
meuNovoApe=Novo(320000,"rua vinte quatro, bairro 3 - numero 40",120000)
#meuNovoApe.valorNovo()
minhaVelhaCasa=Velho(450000, "rua via cinco, numero 332 - bairro alfa", 150000)
#minhaVelhaCasa.valorBaixo()

#Exercicio 5:
class Produto:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

class ItemPedido(Produto):
    def __init__(self, nome, preco, quantidade):
        super().__init__(nome, preco)
        self._quantidade = quantidade

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_preco(self):
        return self._preco

    def set_preco(self, preco):
        self._preco = preco

    def get_quantidade(self):
        return self._quantidade

    def set_quantidade(self, quantidade):
        self._quantidade = quantidade

class Pedido:
    def __init__(self):
        self._itens = []
        self._forma_pagamento = None

    def adicionar_item(self, item):
        self._itens.append(item)

    def get_itens(self):
        return self._itens

    def set_forma_pagamento(self, forma_pagamento):
        self._forma_pagamento = forma_pagamento

    def get_forma_pagamento(self):
        return self._forma_pagamento

    def calcular_total(self):
        total = 0
        for item in self._itens:
            total += item.get_preco() * item.get_quantidade() 
        return total

produto1 = Produto("Farinha", 7.0)
produto2 = Produto("Açúcar", 5.0)

item1 = ItemPedido(produto1._nome, produto1._preco, 1)
item2 = ItemPedido(produto2._nome, produto2._preco, 2)

pedido = Pedido()
pedido.adicionar_item(item1)
pedido.adicionar_item(item2)
pedido.set_forma_pagamento("PIX")

#print("Total do pedido:", pedido.calcular_total())
#print("Forma de pagamento:", pedido.get_forma_pagamento())

#Exercicio 6:
class Pessoa:
    def __init__(self, nome, idade, pai=None, mae=None):
        self.nome = nome
        self.idade = idade
        self.pai = pai
        self.mae = mae

    def _str_(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"

    def mostrar_pais(self):
        if self.pai is not None:
            print(f"Pai: {self.pai.nome}")
        else:
            print("Pai: Desconhecido")

        if self.mae is not None:
            print(f"Mãe: {self.mae.nome}")
        else:
            print("Mãe: Desconhecida")

    def mostrar_arvore_genealogica(self, nivel=0):
        print(f"{'  ' * nivel}{self.nome} ({self.idade} anos)")
        if self.pai is not None:
            self.pai.mostrar_arvore_genealogica(nivel + 1)
        if self.mae is not None:
            self.mae.mostrar_arvore_genealogica(nivel + 1)

avo_paterno = Pessoa("João", 78)
avo_materno = Pessoa("Maria", 76)
pai = Pessoa("Williams", 50, avo_paterno)
mae = Pessoa("Caroline", 48, None, avo_materno)
filho = Pessoa("Abraão", 20, pai, mae)

#filho.mostrar_pais()
#print("\nÁrvore Genealógica:")
#filho.mostrar_arvore_genealogica()