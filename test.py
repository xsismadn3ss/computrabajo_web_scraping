import requests
from bs4 import BeautifulSoup
from offer import Offer

total_offers = 0
total_pages = 0
offers: list[Offer] = []

# peticion inicial para obtener el total de ofertas para la busqueda
URL = "https://sv.computrabajo.com/trabajo-de-programador-en-san-salvador?p=1"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
}
res = requests.get(URL, headers=headers)
if res.ok:
    # obtener total de ofertas
    soup = BeautifulSoup(res.text, 'html.parser')
    total = soup.find('h1', class_="title_page").find('span')
    total_offers = int(total.text.strip().replace(' ',''))
    total_pages = total_offers // 20 +1
    print("Ofertas encontradas: ",total_offers)
    print("Paginas a consultar", total_pages)

    box_offers: list = soup.find_all('article', class_='box_offer')