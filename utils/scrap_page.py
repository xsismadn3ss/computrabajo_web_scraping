from bs4 import BeautifulSoup
from data_types.offer import Offer
from typing import List
from .scrap_boxes import scrap_boxes
import requests
from data_types.scrap_params import ScrapParams


def scrap_page(scrap_params: ScrapParams):
    print(f"Scraping: {scrap_params.url.format(scrap_params.actual_page)}....")
    res = requests.get(
        url=scrap_params.url.format(scrap_params.actual_page),
        headers=scrap_params.headers,
    )
    if not res.ok:
        return []
    soup = BeautifulSoup(res.text, "html.parser")
    total = soup.find("h1", class_="title_page").find("span")
    scrap_params.total_items = int(total.text.strip().replace(" ", ""))
    scrap_params.total_pages = scrap_params.total_items // 20 + 1
    box_offers: list = soup.find_all("article", class_="box_offer")
    scrap_boxes(soup, box_offers)
    scrap_params.actual_page += 1
