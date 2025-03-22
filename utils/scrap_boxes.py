from bs4 import BeautifulSoup
from bs4.element import ResultSet
from data_types.offer import Offer
import re
from data_types.research import research


def scrap_boxes(soup: BeautifulSoup, boxes) -> list[Offer]:
    for box in boxes:
        title: str = box.find("h2")
        company = box.find("p", class_="dFlex vm_fx fs16 fc_base mt5").find("a")
        location = box.find("p", class_="fs16 fc_base mt5").find("span")
        published = box.find("p", class_="fs13")
        miscs = box.find("div", class_="fs13 mt15")
        salary: str = ""
        mode: str = ""

        if miscs is not None:
            miscs = miscs.find_all("span", class_="dIB mr10")
            for misc in miscs:
                if re.search(r"\d+", misc.text.strip()):
                    salary = misc.text.strip()
                else:
                    mode = misc.text.strip()
                    
        offer = Offer(title, company, location, mode, salary, published)
        
        research.add_offer(offer)
        research.add_by_company(offer)
        research.add_by_location(offer)
        research.add_by_mode(offer)
