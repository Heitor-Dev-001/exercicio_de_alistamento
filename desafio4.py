#Faça um programa que leia o ano de nascimento de um jovem
#e informe, de acordo com sua idade:

#Se ele ainda vai se alistar ao serviço militar
#Se é a hora de se alistar
#Se já passou do tempo de alistamento


#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date


#Entrada do usuário
print('''Selecione seu sexo conforme as opções abaixo: 
[ 1 ] - Feminino 
[ 2 ] - Masculino''')
opcao =  int (input('Sua opção:'))

#Condições para masculino e feminino

if opcao == 1:
  sexo ='Feminino'
elif opcao == 2:
  sexo = 'Masculino'         
else:
  sexo = 'Opção inválida'
#Retorno
print('Você selecionou a opção {}'.format(sexo))


#Validando se é necessario se alistar ou não
if sexo == 'Masculino':
  print(' \033[44m Você precisa se alistar junto as forças armadas, favor digitar seu ano de nascimento na sequência \033[m')
else:
  print(' \033[31mVocê não precisa se alistar junto as forças armadas ! \033[m') #Alterar a resposta para a cor vermelha
  print('Fim do programa')
  
#Lógica do programa (Alistamento)
atual = date.today().year
print('-=-' *20)
nasc = int (input ('Ano de nascimento:'))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
  print('Você tem que alistar imediatamente!')
elif idade < 18:
  saldo = 18 - idade  #Calcula quanto tempo falta para o alistanmento
  print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento'.format(saldo))
  ano = atual + saldo
  print('Seu alistamento será em: {}'.format(ano))
elif idade > 18:
  saldo =  idade - 18  #Calcula quanto tempo passou para se alistar
  print('Você já deveria ter se alistado há {} anos'.format(saldo))
  ano = atual - saldo
  print('Seu alistamento foi em: {}'.format(ano))

print('-=-' * 20)




