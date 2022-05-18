# A empresa Cara de Pau Ltda resolveu fazer uma pesquisa de mercado, abrangendo o maior número de pessoas possíveis, para saber se as pessoas estão gostando ou não de um novo produto lançado no mercado.
# A informações coletadas são: o sexo (M,F), a idade e uma resposta (S=sim, N=não, I=indiferente) de cada entrevistado.

# Faça um algoritmo que calcule:
# quantas pessoas foram entrevistadas;
# quantas pessoas disseram sim e quantas disseram não;
# quantas mulheres disseram sim e quantos homens disseram não.

numPessoas = 0
contPessoas = 0
contF = 0
contM = 0
contSim = 0
contNao = 0 
pergunta = int(input("Você deseja participar da pesquisa? 1- sim 2- não -->"))
    
while pergunta == 1:
    
    sexo = input("(m) Masculino ou (f) Feminino: ")
    idade = int(input("Informe sua idade: "))
    resposta = input("Você gostou do novo produto lançado? (s) sim (n) não (i) indiferente: ")

    contPessoas = contPessoas + 1
        
    if sexo == "f" and resposta == "s" :    
        contF = contF + 1
    if sexo == "m" and resposta == "n":
        contM = contM + 1   
    if resposta == "s":
        contSim = contSim + 1
    if resposta == "n":
        contNao = contNao + 1

    pergunta = int(input("Você deseja participar da pesquisa? 1- sim 2- não -->"))   
         
else:
    print("Ok!")
    print("Número de participantes: %d" % contPessoas)
    print("Número de Participantes que disseram sim: %d" %contSim)
    print("Número de Participantes que disseram não: %d" %contNao)
    print("Número de mulheres que disseram sim: %d" %contF)
    print("Número de homens que disseram não: %d" %contM)






  


   

