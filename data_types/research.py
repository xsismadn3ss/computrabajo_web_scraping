from dataclasses import dataclass
from .offer import Offer


@dataclass(repr=True)
class Research:
    companies: set
    locations: set
    offers: list[Offer]


research = Research(set(), set(), [])
