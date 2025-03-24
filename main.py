from utils.scrap_page import scrap_page, look_total_jobs, get_file
from data_types.research import research
from data_types.scrap_params import ScrapParams
import click
import colorama
import os

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
    "--job", prompt="indica el trabajo que deseas buscar ", help="Trabajo a buscar"
)
@click.option(
    "--location",
    prompt="indica la ubicación que deseas buscar ",
    default="san salvador",
    help="ubicación a buscar",
)
def download_files(job: str, location: str):
    """
    - DOWNLOAD FILES \n
    Antes de analizar los datos es necesario descargar los documentos HTML
    para no sobrecargar la página.

    description - descargar archivos para analizar
    """
    location = location.replace(" ", "-")
    job = job.replace(" ", "-")

    if not os.path.exists("downloads"):
        os.makedirs("downloads")
    for file in os.listdir("downloads"):
        file_path = os.path.join("downloads", file)
        if os.path.isfile(file_path):
            os.remove(file_path)

    get_file(scrap_params, job, location)
    while True:
        if scrap_params.actual_page > scrap_params.total_pages:
            print("download complete")
            break
        get_file(scrap_params, job, location)


@cli.command()
def total_jobs():
    """
    - TOTAL JOBS

    decription - ver numero de ofertas encontradas
    """
    try:
        total = look_total_jobs()
        print(total)
    except FileNotFoundError as e:
        print(e)
        print(
            f"No hay archivos HTML descargados para descargar ejecuta {colorama.Back.CYAN}download-files{colorama.Back.RESET} para descargar los archivos"
        )


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
def scrap(job: str, location: str):
    location = location.replace(" ", "-")
    param = job.replace(" ", "-")
    scrap_page(scrap_params)


if __name__ == "__main__":
    cli()
