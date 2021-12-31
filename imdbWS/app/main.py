# WebScrapping Project - Top 250 Movies from IMDB
# Author: duvrdx (Eduardo Henrique)
# 
# Libs: requests - BeautifulSoup - pandas
 

# Importing libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

def main():
    # Variáveis
    url = "https://www.imdb.com/chart/top/"
    response = "" 
    site = ""
    moviesList = []

    # Fazendo uma requisição do tipo GET, para obter o conteúdo do site
    response = requests.get(url)

    # Testes de Conexãos
    print(f"Status Code: {response.status_code}")

    # Criando objeto do tipo BS4
    site = BeautifulSoup(response.content, "html.parser")

    # Isolando o <tbody class="lister-list">
    tbody = site.find("tbody", attrs={"class": "lister-list"})

    # Resgatando informações dos TD
    for tr in tbody.find_all("tr"):
        title = tr.find("td", attrs={"class":"titleColumn"}).find("a").text
        year = tr.find("td", attrs={"class":"titleColumn"}).find("span",attrs={"class":"secondaryInfo"}).text
        link = "https://www.imdb.com/" + tr.find("td", attrs={"class":"titleColumn"}).find("a")["href"]
        imbdRating = tr.find("td", attrs={"class":"ratingColumn imdbRating"}).find("strong").text
        cover = tr.find("td", attrs={"class":"posterColumn"}).find("img")["src"]

        # Removendo '(' ')' do ano
        if '(' in year:
            year = year.replace('(',"")
        if ')' in year:
            year = year.replace(')',"")
        
        # Adicionando informações em uma matriz
        moviesList.append([title,year,imbdRating,cover,link])
    
    # Criando um dataframe com Pandas
    moviesDF = pd.DataFrame(moviesList, columns=["title","year","imdbRating","cover","link"])
    print(moviesDF)

    # Exportando DF como CSV e XLSX
    moviesDF.to_csv("moviesDF.csv", encoding='utf-8', index=False)
    moviesDF.to_excel(r'moviesDF.xlsx', index = False)


if __name__ == "__main__":
    main()