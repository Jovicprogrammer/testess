
lista_perguntas = ["Conhece a vítima?", "Esteve no local do crime?", "Trabalha com a vítima?", "Se encontrou com a vítima?"]
print (lista_perguntas)

contador = 0

for i in range (4):
    sim = 1
    nao = 2
    resposta = (input("Sim [1] ou Não [2]?  "))
    

if resposta == 2*sim:
        print ("Suspeito")
if resposta == 3*sim:
        print ("Cúmplice")
if resposta == 4*sim:
        print ("Você é o Assassino")
if resposta == 1*sim or 0*sim:
        print ("Inocente")

