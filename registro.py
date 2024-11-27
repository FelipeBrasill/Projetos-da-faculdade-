print( '                                             MENU                                                         '            )
#teste do tratamento de erros
erros=1
#estrutura teste
infonovela=['Marimar',1984,'sbt']
dicionarionovela={'Marimar':0 ,'1984':1, 'sbt':2 }
#variaveis de controle
memoria=50
continuar=1
encontrado=0
vertodos=0
posicao=0
import os
while erros==1:
 try:
  selecao=int(input("digite 0 para INSERIR dados de uma novela; \ndigite 1 para EXIBIR as novelas salvas; \ndigite 2 para EXIBIR PARTE da informacao salva; \ndigite 3 para BUSCAR uma novela "))
  break
 except ValueError:
     print('por favor,entre com um digito do teclado')

#1.notei o excesso de informacao na tela e importei a biblioteca os para fazer a limpza com o comando cls
#estrutura condicional de selecão

if selecao==0 or selecao==1 or selecao==2 or selecao==3:
  if selecao==0:
   print("informe os dados a seguir:")
   nome=input('qual o nome da novela?  ')
   infonovela.append(nome)
   while erros==1:
    try:
      ano=int(input('qual o ano da novela?  '))
      infonovela.append(ano) 
      break
     #2.nao consegui fazer a limpeza desse comando     
    except ValueError:
       print('por favor,entre com um numero inteiro')
   emissora=input('qual o nome da emissora onde a novela foi veiculada?  ')
   infonovela.append(emissora)
   print(f'MEMORIA RESTANTE:{memoria-len(infonovela)}')
   print('dados adicionados,obrigado')
   for indice,elementos in enumerate(infonovela):
    dicionarionovela={}
    dicionarionovela[f'{elementos}']=indice
else:
  print("valor não definido.Por favor,escolha entre uma das opções")
#opçoes

if selecao==1:
  print(infonovela)

if selecao==2:
  inicio=int(input(f'{len(infonovela)}->Quantidade de dados salvos \ninforme onde começa o recorte da lista: '))
  fim=int(input("informe onde deseja que termine o recorte"))
  print(infonovela[inicio:fim])

if selecao==3:
    filtro=int(input("deseja procurar pelo nome?:digite 1 \ndeseja pocurar pelo ano:digite 2 \ndeseja procurar pela emissora?:digite 3"))
    if filtro==1:
      opcoes='o nome'
    if filtro==2:
      opcoes='o ano'
    if filtro==3:
      opcoes='a emissora'
    buscador=input(f'informe {opcoes} que deseja buscar: ')
    for i in range(len(infonovela)):
     if buscador==str(infonovela[i]):
      print('dado encontrado na posicao:',i)
      encontrado=1
      vertodos=1
      posicao=i
      break
    if encontrado==0:
      print('dado nao encontrado')
    if vertodos==1:
      a=int(input("deseja ver as informacoes relacionadas? \n1-SIM/2-NAO "))
      if a==1:
        if filtro==1:
          print(infonovela[posicao])
          print(infonovela[posicao+1])
          print(infonovela[posicao+2])
        if filtro==2:
          print(infonovela[posicao])
          print(infonovela[posicao+1])
          print(infonovela[posicao-1])
        if filtro==3:
          print(infonovela[posicao])
          print(infonovela[posicao-1])
          print(infonovela[posicao-2])
         
desejacontinuar=int(input('\ndeseja continuar? \n1-SIM 2-NÃO\n '))

#verificar se deseja continuar adicionando informação

if desejacontinuar!=1:
 print("cabou")
 continuar=0

#loop do deseja continuar
while (continuar==1):
  os.system("cls")
  
  selecao=int(input("digite 0 para INSERIR dados de uma novela; \ndigite 1 para EXIBIR as novelas salvas; \ndigite 2 para EXIBIR PARTE da informacao salva; \ndigite 3 para BUSCAR uma novela "))
  if (selecao==0) or (selecao==1) or (selecao==2) or (selecao==3):
   
   if selecao==0:
    print("informe os dados a seguir:")
    nome=input('qual o nome da novela?  ')
    infonovela.append(nome)
    ano=int(input('qual o ano da novela?  '))
    infonovela.append(ano)
    emissora=input('qual o nome da emissora onde a novela foi veiculada?  ')
    infonovela.append(emissora)
    print(f'memoria restante:{memoria-len(infonovela)}' )
    print('dados adicionados,obrigado')
   for indice,elementos in enumerate(infonovela):
    dicionarionovela={}
    dicionarionovela[f'{elementos}']=indice
   
   if selecao==1:
    print(infonovela)
   
   if selecao==2:
     inicio=int(input(f'{len(infonovela)}->Quantidade de dados salvos \ninforme onde começa o recorte da lista: '))
     fim=int(input("informe onde deseja que termine o recorte"))
     print(infonovela[inicio:fim])

   #3.preciso incrementar com os dados completos
   if selecao==3:
    filtro=int(input("deseja procurar pelo nome?:digite 1 \ndeseja pocurar pelo ano:digite 2 \ndeseja procurar pela emissora?:digite 3"))
    if filtro==1:
      opcoes='o nome'
    if filtro==2:
      opcoes='o ano'
    if filtro==3:
      opcoes='a emissora'
    buscador=input(f'informe {opcoes} que deseja buscar: ')
    for i in range(len(infonovela)):
     if buscador==str(infonovela[i]):
      print('dado encontrado na posicao:',i)
      encontrado=1
      vertodos=1
      posicao=i
      break
    if encontrado==0:
      print('dado nao encontrado')
    if vertodos==1:
      a=int(input("deseja ver as informacoes relacionadas? \n1-SIM/2-NAO "))
      if a==1:
        if filtro==1:
          print(infonovela[posicao])
          print(infonovela[posicao+1])
          print(infonovela[posicao+2])
        if filtro==2:
          print(infonovela[posicao])
          print(infonovela[posicao+1])
          print(infonovela[posicao-1])
        if filtro==3:
          print(infonovela[posicao])
          print(infonovela[posicao-1])
          print(infonovela[posicao-2])
         

  else:
   print("valor não definido.Por favor,escolha entre uma das opções")    
  #a condição da memoria
  
  if (memoria-len(infonovela)==0):
    print("memoria esgotada")
    break
  else:  
   desejacontinuar=int(input('deseja continuar: 1-SIM 2-NÃO    '))
   if desejacontinuar!=1:
    print("cabou")
    continuar=0
  
  