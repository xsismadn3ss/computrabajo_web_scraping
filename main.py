import requests
from bs4 import BeautifulSoup
from data_types.offer import Offer
from utils.scrap_page import scrap_page, look_total_jobs
from data_types.research import research
from data_types.scrap_params import ScrapParams
from icecream import ic
import click

scrap_params = ScrapParams(
    url="https://sv.computrabajo.com/trabajo-de-{}-en-{}?p={}",
    headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
    },
)


@click.group()
def cli():
    """
    --------------BIENVENIDO A COMPUTRABAJO SCRAPER CLI --------------
    description - Aplicación de consola para obtener información de los trabajos de computrabajo
    """
    pass


@cli.command()
@click.option(
    "--job", prompt="indica el trabajo que deseas buscar: ", help="Trabajo a buscar"
)
@click.option(
    "--location",
    prompt="indica la ubicación que deseas buscar: ",
    help="Ubicación a buscar",
    default="san salvador",
)
def total_jobs(job: str, location: str):
    location = location.replace(" ", "-")
    job = job.replace(" ", "-")
    total = look_total_jobs(scrap_params, job, location)
    print(f"{total} trabajos de {scrap_params.job.replace('-', ' ')}")


@cli.command()
@click.option(
    "--job", prompt="indica el trabajo que deseas buscar ", help="Trabajo a buscar"
)
@click.option(
    "--location",
    prompt="indica la ubicación que deseas buscar ",
    help="Ubicación a buscar",
    default="san salvador",
)
def companies(job: str, location: str):
    location = location.replace(" ", "-")
    job = job.replace(" ", "-")
    raise NotImplementedError(
        "Implementar función para buscar empresas que ofrecen el trabajo buscado"
    )


@cli.command()
@click.option(
    "--job", prompt="indica el trabajo que deseas buscar: ", help="Trabajo a buscar"
)
@click.option(
    "--location",
    prompt="indica la ubicación que deseas buscar: ",
    help="Ubicación a buscar",
    default="san salvador",
)
def scrap(param: str, location: str):
    location = location.replace(" ", "-")
    param = job.replace(" ", "-")
    scrap_page(scrap_params)


if __name__ == "__main__":
    cli()
