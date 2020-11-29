import requests
from bs4 import BeautifulSoup

MAIN_ADDRESS = "https://www.imdb.com"

response = requests.get(MAIN_ADDRESS + "/find?s=ep&q=thriller&ref_=nv_sr_sm")
html_data = BeautifulSoup(response.content, 'html.parser')
# print(html_data.prettify())

table_findList = html_data.find('table', {'class': 'findList'})
# print(table_findList.prettify())
table_tr = table_findList.findAll('tr')

movie_info_array = []

for row in table_tr:
    movie_info = {}
    row_data = row.findAll('td')
    # print(row_data[1].a.text)
    sub_url = row_data[1].a['href']
    movie_info['title'] = row_data[1].a.text
    movie_info['sub_page'] = row_data[1].a['href']

    movie_sub_page_info_response = requests.get(MAIN_ADDRESS + movie_info['sub_page'])
    movie_sub_page_info = BeautifulSoup(movie_sub_page_info_response.content, 'html.parser')

    try:
        genre = movie_sub_page_info.find('div', {'class': 'see-more inline canwrap'})
        # print(genre)
        movie_info['genre'] = genre.a.text
        print(movie_info['title'])
        print(movie_info['genre'])
    except AttributeError:

        print(movie_info['title'] + "is no genre")

    finally:
        movie_info_array.append(movie_info)

print(movie_info_array)
