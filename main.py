import requests
from bs4 import BeautifulSoup
import pandas as pd
import xlsxwriter

sirealNumber=[]
movieName=[]
movieYear=[]
movieGenre=[]
movieRating=[]

URL="https://www.imdb.com/list/ls041322734/"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
# print(soup.prettify())

table = soup.find('div', attrs = {'class':'lister list detail sub-list'})

for sno in table.findAll('span', attrs={'class':'lister-item-index unbold text-primary'}):
    sirealNumber.append(sno.text.strip("."))
    # print(sno.text.strip("."))

for mName in table.findAll('h3', attrs={'class':'lister-item-header'}):
    for movieNames in mName.findAll('a'):
        movieName.append(movieNames.text)

for years in table.findAll('span',attrs={'class':'lister-item-year text-muted unbold'}):
    movieYear.append(years.text.strip("()"))

for genres in table.findAll('span', attrs={'class':'genre'}):
    movieGenre.append(genres.text)

for ratingsTab in table.findAll('div',attrs={'class':'ipl-rating-star small'}):
    for ratings in ratingsTab.findAll('span', attrs={'class':'ipl-rating-star__rating'}):
        movieRating.append(ratings.text)



dat1 = pd.DataFrame(sirealNumber)
dat1.columns = ['Serial Number']
result1A = dat1

dat2 = pd.DataFrame(result1A)
dat3 = pd.DataFrame(movieName)
dat3.columns = ['Movie Name']
result2A = dat2.join(dat3)

dat4 = pd.DataFrame(result2A)
dat5 = pd.DataFrame(movieYear)
dat5.columns = ['Movie Year']
result3A = dat4.join(dat5)

dat6 = pd.DataFrame(result3A)
dat7 = pd.DataFrame(movieGenre)
dat7.columns = ['Movie Genre']
result4A = dat6.join(dat7)

dat8 = pd.DataFrame(result4A)
dat9 = pd.DataFrame(movieRating)
dat9.columns = ['Movie Rating']
result4A = dat8.join(dat9)


df1 = pd.DataFrame(result4A)
writer = pd.ExcelWriter('result.xlsx', engine='xlsxwriter')
df1.to_excel(writer, sheet_name='Sheet1')
worksheet = writer.sheets['Sheet1']
writer.save()