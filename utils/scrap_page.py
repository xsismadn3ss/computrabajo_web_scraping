from bs4 import BeautifulSoup
from data_types.offer import Offer
from typing import List
from .scrap_boxes import scrap_boxes
import requests
from data_types.scrap_params import ScrapParams


def look_total_jobs(scrap_params: ScrapParams, job: str, loaction: str) -> str:
    print(
        f"Scraping: {scrap_params.url.format(job, loaction, scrap_params.actual_page)}...."
    )
    res = requests.get(
        url=scrap_params.url.format(job, loaction, scrap_params.actual_page),
        headers=scrap_params.headers,
    )
    scrap_params.job = job
    scrap_params.location = loaction

    if not res.ok:
        return []
    # guardar todo el html
    soup = BeautifulSoup(res.text, "html.parser")
    total_div = soup.find("div", class_="box_title")
    total_h1 = total_div.find("h1", class_="title_page").find("span")
    total = total_h1.text.strip().replace(" ", "")
    return total


def scrap_page(scrap_params: ScrapParams, job: str, location: str) -> None:
    print(
        f"Scraping: {scrap_params.url.format(job, location, scrap_params.actual_page)}...."
    )
    res = requests.get(
        url=scrap_params.url.format(job, location, scrap_params.actual_page),
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
