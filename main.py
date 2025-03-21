import requests
from bs4 import BeautifulSoup
from data_types.offer import Offer
from utils.scrap_page import scrap_page
from data_types.research import research
from data_types.scrap_params import ScrapParams

scrap_params = ScrapParams(
    url="https://sv.computrabajo.com/trabajo-de-programador-en-san-salvador?p={}",
    headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
    },
)
scrap_page(scrap_params)
while True:
    if scrap_params.actual_page > scrap_params.total_pages:
        break
    scrap_page(scrap_params)

# Save scraped data to a text file
print("Saving recolected data....")
with open("scraped_jobs.txt", "w", encoding="utf-8") as f:
    f.write(f"Total Job: {len(research.offers)}\n\n")

    f.write(f"Locations ({len(research.locations)})\n")
    for location in research.locations:
        f.write(f"- {location}\n")
    f.write("\n")

    f.write(f"Companies ({len(research.companies)})\n")
    for company in research.companies:
        f.write(f"- {company}\n")
    f.write("\n")

    for offer in research.offers:
        # Write each offer's details on a new line
        f.write("-" * 50 + "\n")  # Separator between offers
        f.write(f"{offer.title.upper()}\n")
        f.write(f"Company: {offer.company}\n")
        f.write(f"Location: {offer.location}\n")
        f.write(f"Mode: {offer.mode}\n")
        f.write(f"Salry: {offer.salary}\n")
        f.write(f"Publisehd: {offer.published}\n")
        f.write("-" * 50 + "\n")  # Separator between offers

print("Data saved")
