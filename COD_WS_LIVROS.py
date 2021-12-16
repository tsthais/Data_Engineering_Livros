#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importando bibliotecas
import requests
from bs4 import BeautifulSoup 
import re
import pandas as pd


# In[2]:


# realizando a coleta das páginas em que estão os livros
paginas = []

nova_pagina = "http://books.toscrape.com/catalogue/page-1.html"
# enquanto o código da página for 200 (páginas válidas ou existentes)
while requests.get(nova_pagina).status_code == 200:
# coloca no vetor a url da nova pagina, inicialmente a primeira pagina    
    paginas.append(nova_pagina)
# para atualizar a nova é separado a primeira parte da url até "-", ou seja, 
# 'http://books.toscrape.com/catalogue/page', seguido de o número atual mais 1
# seguido do ".html"
    nova_pagina = paginas[-1].split("-")[0] + "-" + str(int(paginas[-1].split("-")[1].split(".")[0]) + 1) + ".html"
    


# In[3]:


# criando os vetores para compor o banco de dados
nome_livro = []
preco_livro = []
classificacao = []
estoque = []


# In[4]:


for j in paginas:
    url = requests.get(j)
    soup = BeautifulSoup(url.text, 'html.parser')
    # coletando todas caracteristicas dos produtos
    products = soup.findAll("li", {"class": "col-xs-6 col-sm-4 col-md-3 col-lg-3"})
    for i in products:
        # coletando nome dos livros
        nome=i.h3.a["title"]
        # colocando no vetor nome_livro
        nome_livro.append(nome)
        
        # coletando o preço dos livros
        preco = i.findAll("p", {"class": "price_color"})
        preco = preco[0].get_text().replace('Â', '').replace('£', '').strip()
        # colocando no vetor preco_livro
        preco_livro.append(preco)
        
        # coletando a classificação dos livros
        cls = i.find("p", class_ = re.compile("star-rating")).get("class")[1]
        
        # reescrevendo a classificação
        
        if cls == "One":
            cls = '1'
        else:
            if cls == "Two":
                cls = '2'
            else:
                if cls == "Three":
                    cls = '3'
                else:
                    if cls == "Four":
                        cls = '4'
                    else:
                        cls = '5'
         # colocando no vetor classificacao
        classificacao.append(cls)
        
        # coletando o estoque dos produtos 
        etqe = i.findAll("p", {"class": "instock availability"})
        etqe = etqe[0].get_text().strip()
        
        # reescrevendo o estoque dos produtos
        if etqe == "In stock":
            etqe = "Em estoque"
        else:
            etqe = "Em falta"
        
        # colocar no vetor estoque
        estoque.append(etqe)


# In[5]:


# criando o banco de dados 
dados_coletados = pd.DataFrame({'nome_livro': nome_livro, 
                                'preco_livro': preco_livro, 
                                'avaliacao_livro': classificacao, 
                                "estoque_livro": estoque})


# In[6]:


# primeiras linhas do banco de dados 
dados_coletados.head()


# In[7]:


# exportando banco de dados 
dados_coletados.to_excel(r'D:\Projetos\WS_Livros\Livros.xlsx', sheet_name='WS_Livros', index = False)

