from dataclasses import dataclass
@dataclass
class Offer:
    company: str
    location:str
    mode: str
    salary:str|None
    published:str|None