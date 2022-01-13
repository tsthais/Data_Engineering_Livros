#

<div>
  <h1 align="center"> Automação de Web e de Processos (Data Engineering) 👩‍💻🦾🖥</h1>
</div>

#

<h3>➡Sobre o Desafio </h3>

Este é um desafio de Data Engineering proposto no site da [Medium](https://medium.com/@meigarom/o-projeto-de-data-engineering-para-o-seu-portf%C3%B3lio-c186c7191823).
Neste site é posto que o desafio da engenharia de dados é coletar e organizar dados, de forma que o engenheiro de dados deve ter a capacidade de acessar fontes distintas de dados,
coletar essas informações e armazenar em um local de fácil acesso e que seja escalável.

# 

<h3>➡ Contexto do Desafio </h3>

A Book Club é uma Startup de troca de livros. O modelo de negócio funciona com base na troca de livros pelos usuários,
cada livro cadastrado pelo usuário, dá o direito à uma troca, porém o usuário também pode comprar o livro, caso ele 
não queira oferecer outro livro em troca.

Umas das ferramentas mais importantes para que esse modelo de negócio rentabilize, é a recomendação. Uma excelente recomendação aumenta o volume de trocas e vendas no site.

Você é um Data Scientist contrato pela empresa para construir um Sistema de Recomendação que impulsione o volume de trocas e vendas entre os usuários. Porém, a Book Club não coleta e nem armazena os livros enviados pelos usuários.

Os livros para troca, são enviados pelos próprios usuários através de um botão “Fazer Upload”, eles ficam visíveis no site, junto com suas estrelas, que representam o quanto os usuários gostaram ou não do livro, porém a Startup não coleta e nem armazena esses dados em um banco de dados.

Logo, antes de construir um sistema de recomendação, você precisa coletar e armazenar os dados do site. Portanto seu primeiro trabalho como um Data Scientist será coletar e armazenar os seguintes dados:

- O nome do livro;
- A categoria do livro;
- O número de estrelas que o livro recebeu;
- O preço do livro;
- Se o livro está em Estoque ou não.

Os dados para serem coletados e armazenados, estão disponíveis neste site. http://books.toscrape.com/

# 

<h3>➡ Passos que foram utilizados para resolver o desafio: </h3>

1. Faça o web scraper utilizando a linguagem Python;
2. Utilizar a biblioteca Selenium do Python para navegar entre os links das categorias e as páginas;
3. Utilizar a biblioteca BeautifulSoup do Python para coletar os dados das páginas HTML;
4. Instale no seu computador e configure um banco de dados Postgres;
5. Crie uma tabela para armazenar os dados.
