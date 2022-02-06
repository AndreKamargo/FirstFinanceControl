ArquivoMes = open("Mes.txt","r").read()

print("-------------------------------------------------")
print("-------CONTROLE FINANCEIRO DE",ArquivoMes, "--------")
print("-------------------------------------------------")

#Variavel loop menu inicial
Selecionar = ""
ContasFixas = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
ContasNome = ["Energia","Gas","Internet","Celular","Cartão de credito","Nota","Aluguel","Atacadão"]

#Funções Valores Gastos Diarios
def TotalMercado():
    arquivo = open("Mercado.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.rstrip()
        linha = float(linha)
        palavras.append(linha)

    global TotalMercadoV
    TotalMercadoV = sum([float(x) for x in palavras])
    arquivo.close()
def TotalSair():
    arquivo = open("Sair.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.rstrip()
        linha = float(linha)
        palavras.append(linha)

    global TotalSairV
    TotalSairV = sum([float(x) for x in palavras])
    arquivo.close()
def TotalCompras():
    arquivo = open("Compras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.rstrip()
        linha = float(linha)
        palavras.append(linha)

    global TotalComprasV
    TotalComprasV = sum([float(x) for x in palavras])
    arquivo.close()

#Função importa tabela de gastos fixos
def TabelaContas():
    arquivo = open("ContasFixas.txt", "r")
    global ContaTabela
    ContaTabela = []

    for linha in arquivo:
        linha = linha.rstrip()
        linha = float(linha)
        ContaTabela.append(linha)
    arquivo.close()
TabelaContas()

#Função importar tabela de ganhos
def TabelaCredito():
    arquivo = open("Credito.txt", "r")
    global CreditoTabela
    CreditoTabela = []

    for linha in arquivo:
        linha = linha.rstrip()
        linha = float(linha)
        CreditoTabela.append(linha)
    arquivo.close()
TabelaCredito()


#Função salvar gastos fixos
def SalvarContasFixa():
    var = "\n".join(map(str, ContaTabela))
    ArquivoContasFixa = open("ContasFixas.txt","w")
    ArquivoContasFixa.write(var)

#Formatar numeros na moeda brasileira
def real(valor):
  a = "{:,.2f}".format(float(valor))
  b = a.replace(',','v')
  c = b.replace('.',',')
  return c.replace('v','.')

#Função para mostrar valor mais alto de uma tabela
def MaisCaro():
    max_val = 0
    global idx_max
    idx_max = 0

    for i in range(len(ContaTabela)):
        if ContaTabela[i] > max_val:
            max_val = ContaTabela[i]
            idx_max = i

#Classe não utilizada
def Ganhos():
    class Ganhos:
        def __init__(self, valor, empresa, especificacao):
            self.valor = valor
            self.empresa = empresa
            self.especificacao = especificacao


#Loop de ações do Menu
while Selecionar != "0":
    Selecionar = input("\n(1)Adicionar gasto (2)Adicionar gasto fixo (3)Adicionar credito (4)Saldo (5)Relatorio\Terminar mês (0)Sair   ")

    # Na opção numero4 é possivel estabelecer uma meta para o mes e ver o saldo atual. é possivel modificar saldo e meta.
    if Selecionar == "4":
        ArquivoSaldo = open("Saldo.txt","r").read()
        ArquivoSaldo = float(ArquivoSaldo)
        ArquivoMeta = open("Meta.txt","r").read()
        ArquivoMeta = float(ArquivoMeta)
        Meta = ArquivoMeta - ArquivoSaldo

        if ArquivoSaldo < ArquivoMeta:
            print("\nSeu saldo no mês de {} é {}. É preciso ganhar {} para chegar na meta de {}.".format(ArquivoMes,real(ArquivoSaldo),real(Meta),real(ArquivoMeta)))
        else:
            Meta = abs(Meta)
            print("\nSeu saldo do mês de {} é {}. Parabens, voce ultrapassou a meta de {} e lucrou {}.".format(ArquivoMes,real(ArquivoSaldo),real(ArquivoMeta),real(Meta)))

        AdicionarSaldo = input("\n(1)Voltar (2)Sobrescrever Saldo (3)Sobrescrever Meta   ")

        if AdicionarSaldo == "1":
            continue
        elif AdicionarSaldo == "2":
            NovoSaldo = str(input("\nValor do novo saldo (xxxx.xx): R$ "))
            ArquivoSaldo = open("Saldo.txt", "w")
            ArquivoSaldo.write(NovoSaldo)
            ArquivoSaldo.close()
        elif AdicionarSaldo == "3":
            NovaMeta = str(input("\nValor da nova meta (xxxx,xx): R$ "))
            ArquivoSaldo = open("Meta.txt", "w")
            ArquivoSaldo.write(NovaMeta)
            ArquivoSaldo.close()

    #Opção 1 é para colocar gastos diarios sem ser contas fixas.
    if Selecionar == "1":
        TipoGasto = input("\n(1)Mercado (2)Sair (3)Compras ")
        if TipoGasto == "1":
            ValorGastoDia = input("\nQual o valor? ")
            Arquivo = open("Mercado.txt","a")
            Arquivo.write("\n")
            Arquivo.write(ValorGastoDia)
            Arquivo.close()
            TotalMercado()
            print("\nValor de gasto com mercado até o momento é ",TotalMercadoV)


        elif TipoGasto == "2":
            ValorGastoDia = input("\nQual o valor? ")
            Arquivo = open("Sair.txt", "a")
            Arquivo.write("\n")
            Arquivo.write(ValorGastoDia)
            Arquivo.close()
            TotalSair()
            print("\nValor de gasto com saidas até o momento é ", TotalSairV)

        elif TipoGasto == "3":
            ValorGastoDia = input("\nQual o valor? ")
            Arquivo = open("Compras.txt", "a")
            Arquivo.write("\n")
            Arquivo.write(ValorGastoDia)
            Arquivo.close()
            TotalCompras()
            print("\nValor de gasto com compras até o momento é ", TotalComprasV)
    #Opção 2 colocar gastos de contas fixas
    if Selecionar == "2":
        TipoFixo = input("\n(1)Energia (2)Gas (3)Internet (4)Celular (5)Cartão (6)DAS (7)Aluguel (8)Atacadão   ")
        if TipoFixo == "1":
            ValorFixo = input("\nQual valor da conta de luz? ")
            ContaTabela[0] = ValorFixo
            SalvarContasFixa()
        elif TipoFixo == "2":
            ValorFixo = input("\nQual valor da conta de gas? ")
            ContaTabela[1] = ValorFixo
            SalvarContasFixa()
        elif TipoFixo == "3":
            ValorFixo = input("\nQual valor da conta de internet? ")
            ContaTabela[2] = ValorFixo
            SalvarContasFixa()
        elif TipoFixo == "4":
            ValorFixo = input("\nQual valor da conta de celular? ")
            ContaTabela[3] = ValorFixo
            SalvarContasFixa()
        elif TipoFixo == "5":
            ValorFixo = input("\nQual valor da conta do cartão de credito? ")
            ContaTabela[4] = ValorFixo
            SalvarContasFixa()
        elif TipoFixo == "6":
            ValorFixo = input("\nQual valor da conta das notas? ")
            ContaTabela[5] = ValorFixo
            SalvarContasFixa()
        elif TipoFixo == "7":
            ValorFixo = input("\nQual valor do aluguel? ")
            ContaTabela[6] = ValorFixo
            SalvarContasFixa()
        elif TipoFixo == "8":
            ValorFixo = input("\nQual valor do atacadão? ")
            ContaTabela[7] = ValorFixo
            SalvarContasFixa()
    #Opçao 3 para adicionar credito no saldo
    if Selecionar == "3":
        ValorGanho = str(input("Qual o valor ganho? "))
        Empresa = input("Qual a empresa? ")
        Especificacao = input("Qual foi o trabalho")
        print('{:>25} {:>25} {:>25}'.format(real(ValorGanho),Empresa,Especificacao), file=open("Ganhos.txt", "a"))
        print(ValorGanho,file=open("Credito.txt","a"))
        ArquivoValorCredito = open("Saldo.txt", "r").read()
        Credito = float(ValorGanho) + float(ArquivoValorCredito)
        Credito = str(Credito)
        ArquivoCredito = open("Saldo.txt", "w")
        ArquivoCredito.write(Credito)
        ArquivoCredito.close()
        print("Saldo atual: ", Credito)
    #Opção 5 Mudar de mes, criar relatorio mensal
    if Selecionar == "5":
        print("Gerando relatorio do mês de ",ArquivoMes)
        ArquivoSaldo = open("Saldo.txt", "r").read()
        ArquivoSaldo = float(ArquivoSaldo)
        ArquivoMeta = open("Meta.txt", "r").read()
        ArquivoMeta = float(ArquivoMeta)
        TotalGastoFixo = sum([float(x)for x in ContaTabela])
        MaisCaro()
        TotalMercado()
        TotalSair()
        TotalCompras()
        TotalGastosVariavel = TotalMercadoV + TotalSairV + TotalComprasV
        GanhosTexto = open("Ganhos.txt","r").read()
        SomaCredito = sum([float(x)for x in CreditoTabela])
        Defit = ArquivoMeta - SomaCredito
        Porcentagem = 100 * float(ContaTabela[idx_max]) / float(TotalGastoFixo)
        TotalGastos = TotalGastoFixo + TotalGastosVariavel
        Lucro = SomaCredito - TotalGastos
        novo = open(ArquivoMes + ".txt","w+")

        print("---------------------------------------------",file=open(ArquivoMes + ".txt","a"))
        print("-------CONTROLE FINANCEIRO DE",ArquivoMes, "--------", file=open(ArquivoMes + ".txt", "a"))
        print("---------------------------------------------", file=open(ArquivoMes + ".txt", "a"))
        print("Meta: R$", real(ArquivoMeta), file=open(ArquivoMes + ".txt", "a"))
        print("Saldo: R$",real(ArquivoSaldo),file=open(ArquivoMes + ".txt", "a"))
        print("\nGastor fixos: ",file=open(ArquivoMes + ".txt", "a"))
        print("Energia: R$",ContaTabela[0],file=open(ArquivoMes + ".txt", "a"))
        print("Gas: R$", ContaTabela[1], file=open(ArquivoMes + ".txt", "a"))
        print("Internet: R$", ContaTabela[2], file=open(ArquivoMes + ".txt", "a"))
        print("Celular: R$", ContaTabela[3], file=open(ArquivoMes + ".txt", "a"))
        print("Cartão: R$", ContaTabela[4], file=open(ArquivoMes + ".txt", "a"))
        print("Nota: R$", ContaTabela[5], file=open(ArquivoMes + ".txt", "a"))
        print("Aluguel: R$", ContaTabela[6], file=open(ArquivoMes + ".txt", "a"))
        print("Atacadão: R$", ContaTabela[7], file=open(ArquivoMes + ".txt", "a"))
        print("O maior gasto fixo foi ",ContasNome[idx_max],"sendo ","%.0f" % Porcentagem,"% dos gastos fixos",file=open(ArquivoMes + ".txt", "a"))
        print("Total de gastos fixo: R$",real(TotalGastoFixo),file=open(ArquivoMes + ".txt", "a"))
        print("\nOutros gastos",file=open(ArquivoMes + ".txt", "a"))
        print("Mercado: R$",TotalMercadoV,file=open(ArquivoMes + ".txt", "a"))
        print("Saidas: R$", TotalSairV, file=open(ArquivoMes + ".txt", "a"))
        print("Compras: R$", TotalComprasV, file=open(ArquivoMes + ".txt", "a"))
        print("Total de gastos sem ser contas: R$", real(TotalGastosVariavel), file=open(ArquivoMes + ".txt", "a"))
        print("\nGanhos",file=open(ArquivoMes + ".txt", "a"))
        print('{:>25} {:>25} {:>25}'.format("Valor","Empresa","Trabalho"), file=open(ArquivoMes + ".txt", "a"))
        print(GanhosTexto,file=open(ArquivoMes + ".txt", "a"))
        print("Total de ganhos R$ ",real(SomaCredito),file=open(ArquivoMes + ".txt", "a"))
        print("Total de gastos R$ ",real(TotalGastos),file=open(ArquivoMes + ".txt", "a"))
        if SomaCredito > TotalGastos:
            print("\nSeus lucros foram maior que despesas",file=open(ArquivoMes + ".txt", "a"))
            print("Lucro total R$",real(Lucro),file=open(ArquivoMes + ".txt", "a"))
        else:
            print("Suas despesas foram acima dos ganhos", file=open(ArquivoMes + ".txt", "a"))
            print("Despesa total R$", real(Lucro), file=open(ArquivoMes + ".txt", "a"))

        if ArquivoMeta > SomaCredito:
            print("\nVoce não atingiu a meta de R$",real(ArquivoMeta),file=open(ArquivoMes + ".txt", "a"))
            print("Deficit de R$",Defit,file=open(ArquivoMes + ".txt", "a"))

        NovoMes = str(input("\nDeseja começar novo mes ?(1)Sim (2)Não"))
        if NovoMes == "1":
            QualMes = input("Qual o novo mês? ")
            print(QualMes,file=open("Mes.txt", "w"))
            print("",file=open("Compras.txt", "w"))
            print("", file=open("ContasFixas.txt", "w"))
            print("", file=open("Credito.txt", "w"))
            print("", file=open("Ganhos.txt", "w"))
            print("", file=open("GastosDiarios.txt", "w"))
            print("", file=open("Mercado.txt", "w"))
            print("", file=open("Sair.txt.txt", "w"))
        elif NovoMes == "2":
            continue
























