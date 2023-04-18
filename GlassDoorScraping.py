import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.glassdoor.com.br/Avalia%C3%A7%C3%B5es/Aliare-Avalia%C3%A7%C3%B5es-E6020855.htm'

# adiciona um User-Agent ao cabeçalho da solicitação
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

response = requests.get(url, headers=headers)

content = response.content

#CONVERTE PARA HTML DENTRO DO BEATIFULSOUP
site=BeautifulSoup(content,'html.parser')

#Criando uma lista de avaliações vazia
Lista_Avaliacoes=[]

avaliacoes = site.findAll('div',attrs={'class':'gdReview'})

for avaliacao in avaliacoes:
 #data da avaliacao e cargo e local
 DataCargoLocal=avaliacao.find('span',attrs={'class':'common__EiReviewDetailsStyle__newUiJobLine'})

 #trazer o titulo de cada avaliação

 Titulo=avaliacao.find('a',attrs={'class':'reviewLink'})

 #trazer o link de cada avaliacao

 Link="https://www.glassdoor.com.br" +"" +Titulo['href']
 #print(Link)

 #adicionar a lista as avariaveis que escolhi = append
 Lista_Avaliacoes.append([Titulo.text,DataCargoLocal.text,Link])


ratings=pd.DataFrame(Lista_Avaliacoes,columns=['Titulo','DataCargoLocal','LinkAvaliacao'])

ratings.to_excel('AvaliacoesGlassdoor.xlsx',index=False)

print(ratings)