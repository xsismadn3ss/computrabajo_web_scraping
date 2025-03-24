from bs4 import BeautifulSoup
from data_types.offer import Offer
from typing import List
from .scrap_boxes import scrap_boxes
import requests
from data_types.scrap_params import ScrapParams
import colorama


def get_file(scrap_params: ScrapParams, job: str, location: str):
    """Descargar archivo HTML y guardarlos en la carpeta ``downloads``

    Args:
        scrap_params (ScrapParams): instancia de clase con parametros de busqueda
        job (str): trabajo buscado
        location (str): ubicación para buscar trabajos por zona
    """
    print(
        f"downloading {colorama.Fore.GREEN}{scrap_params.url.format(job, location, scrap_params.actual_page)}{colorama.Fore.RESET} ..."
    )
    res = requests.get(
        url=scrap_params.url.format(job, location, scrap_params.actual_page),
        headers=scrap_params.headers,
    )
    if not res.ok:
        return

    soup = BeautifulSoup(res.text, "html.parser")
    total = soup.find("h1", class_="title_page").find("span")
    scrap_params.total_items = int(total.text.strip().replace(" ", ""))
    scrap_params.total_pages = scrap_params.total_items // 20 + 1

    with open(
        f"downloads/page_{scrap_params.actual_page}.html", "w", encoding="utf-8"
    ) as file:
        file.write(res.text)
    scrap_params.actual_page += 1


def look_total_jobs() -> str:
    with open("downloads/page_1.html", "r", encoding="utf-8") as file:
        doc = file.read()
        file.close()

    soup = BeautifulSoup(doc, "html.parser")
    total_div = soup.find("div", class_="box_title")
    total_h1 = total_div.find("h1", class_="title_page")
    total_span = total_h1.find("span")
    n: str = total_h1.text.strip()
    words = n.split(" ")
    text = ""
    for word in words:
        if word == "":
            continue
        if word.strip().isdigit():
            text += f"{colorama.Fore.GREEN}{word.strip()}{colorama.Fore.RESET}"
            continue
        text += f"{word.strip()} "
    return text


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
