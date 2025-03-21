from dataclasses import dataclass
from typing import Optional
import colorama


@dataclass
class Offer:
    title: Optional[str]
    company: Optional[str]
    location: Optional[str]
    mode: Optional[str]
    salary: Optional[str]
    published: Optional[str]

    def __post_init__(self):
        self.title = self.title.text.strip() if self.title else "sin titulo"
        self.company = (
            self.company.text.strip() if self.company else "empresa no mostrada"
        )
        self.location = self.location.text.strip() if self.location else "sin ubicación"
        self.mode = self.mode.strip() if self.mode else "no especeficado"
        self.salary = self.salary.strip() if self.salary else "no especificado"
        self.published = (
            self.published.text.strip() if self.published else "no especificado"
        )

    def __str__(self):
        return f"""
-----------------------------------------
{colorama.Fore.GREEN}{colorama.Style.BRIGHT}{self.title.upper()}{colorama.Fore.RESET}{colorama.Style.RESET_ALL}
Empresa: {colorama.Fore.GREEN}{self.company}{colorama.Fore.RESET}
Ubicación: {colorama.Fore.GREEN}{self.location}{colorama.Fore.RESET}
Modalidad: {colorama.Fore.GREEN}{self.mode}{colorama.Fore.RESET}
Salario: {colorama.Fore.GREEN}{self.salary}{colorama.Fore.RESET}
Publicado: {colorama.Fore.GREEN}{self.published}{colorama.Fore.RESET}
----------------------------------------
        """
