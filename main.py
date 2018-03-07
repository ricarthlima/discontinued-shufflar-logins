'''
Universidade Federal de Pernambuco - UFPE (www.ufpe.br)
Centro de Informática - CIn (www.cin.ufpe.br)

Autor: Ricarth Lima (rrsl@cin.ufpe.br)
Data: 06/03/2018 v1.0

Copyright @ Ricarth Lima 2018
'''

#1. Importações
import random

#2. Classes
class Monitor:
    ''' Classe que representa um monitor. É inicializado com o nome do monitor e
    e seu histórico de alunos. Além disso pode-se adicionar e consultar uma lista
    dos monitorandos escolhidos para lista atual.
    '''
    def __init__(self,nome,historico):
        self.__nome = nome
        self.__historico = historico
        self.__atuais = []

    def __repr__(self):
        ''' Representação para Shell.'''
        return str(self.__nome) + ": " + str(self.__historico)

    def __str__(self):
        ''' Representação para String.'''
        return str(self.__nome) + ": " + str(self.__historico)

    def getNome(self):
        return self.__nome

    def getHistorico(self):
        return self.__historico

    def getAtuais(self):
        return self.__atuais

    def add(self, login):
        '''Adiciona um login de um monitorando na lista de atuais.'''
        self.__atuais.append(login)

    def att(self):
        '''Atualiza o historico do monitor com os atuais.'''
        self.__historico = self.__historico + self.__atuais

#3. Funções
def tokenizar(string, sep):
    '''Porque eu não gosto do split. Também dei uma configurada
    para que meus arquivos aceitem comentários.'''
    lista = []
    palavra = ""

    chave = False
    for letra in string:
        if letra == "\n":
            chave = False
            
        if letra == "#" and chave == False:
            chave = True

        if chave == False:   
            if letra == sep:
                if palavra != "":
                    lista.append(palavra)
                    palavra = ""
            else:
                palavra += letra
    if palavra != "":
        lista.append(palavra)
    return lista

def leMonitores():
    '''Lê o arquivo dos monitores, aliemnta uma lista de objetos do tipo
    Monitor com os respectivos nomes e históricos.
    '''
    file = open('monitores.txt','r')
    lista = tokenizar(file.read(),"\n")
    file.close()

    listaMonitores = []
    for linha in lista:
        texto = tokenizar(linha," ")
        monitor = Monitor(texto[0],texto[1:])
        listaMonitores.append(monitor)
        
    return listaMonitores

def leLogins():
    ''' Lê o arquivo dos logins dos monitorandos que enviaram arquivos
    nessa lista.
    '''
    file = open('logins.txt','r')
    lista = tokenizar(file.read(),"\n")
    return lista

def mostraAtuais(monitores):
    ''' Dada uma lista de monitores, imprime seus nomes e seus monitorandos
    escolhidos.
    '''
    for monitor in monitores:
        print(monitor.getNome(),monitor.getAtuais())

def gravaAtuais(monitores):
    ''' Dada uma lista de monitores, gera um arquivo com seus monitorandos atuais.
    '''
    file = open("lista.txt","a")
    for monitor in monitores:
        if isinstance(monitor, Monitor):
            file.write(str(monitor.getNome())+": "+str(monitor.getAtuais())+"\n")
        else:
            file.write(monitor+" ")
    file.close()

def gravaMonitores(monitores):
    '''Dada uma lista de monitores, sobreescreve o arquivo monitores com as
    novas informações, seguindo o padrão para leitura.
    '''
    file = open("monitores.txt","w")
    
    for monitor in monitores:
        nome = monitor.getNome()
        historico = monitor.getHistorico()

        file.write(nome)
        for login in historico:
            file.write(" "+login)
        file.write("\n")

    file.write("\n")
    file.close()
    
#4. Função Principal        
def main():
    ''' Função principal do programa.
    '''
    monitores = leMonitores()
    logins = leLogins()
    random.shuffle(logins)  #Embaralha a lista de logins.

    const = (len(logins) // len(monitores)) - 1     #Define a quantidade máxima de monitorandos por monitor.
    
    while len(logins) != 0:
        login = logins[0]   #Define o login atual como sendo o primeiro da lista.

        #Dado o login escolhido, distribui entre os monitores.
        i = 0
        while i < len(monitores):
            if (login in monitores[i].getHistorico()) or (len(monitores[i].getAtuais()) > const):
                i = i + 1
            else:
                monitores[i].add(login)
                break #Ao achar um monitor onde o monitorando possa se encaixar, para.

        #Confere se chegou um momento em que os não há como inserir um monitorando em nenhum monitor.
        if i >= len(monitores):
            break
        else:
            del logins[0]

    #Imprimir na tela informações
    mostraAtuais(monitores)
    print("Resto: ", logins)

    #Gerar um arquivo auxiliar.
    if input("\nDeseja gerar um arquivo? s/n ").lower() == "s":
        gravaAtuais(monitores)
        gravaAtuais(logins)

    #Gravar no historico dos monitores
    if input("\nDeseja gravar os dados no historico dos monitores? s/n ").lower() == "n":
        if input("\nTem certeza? Os dados gerados serão perdidos. s/n ").lower() == "n":
            return

    for monitor in monitores:
        monitor.att()

    gravaMonitores(monitores)
    
          
main()
