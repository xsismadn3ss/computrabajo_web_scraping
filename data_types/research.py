from dataclasses import dataclass
from .offer import Offer


@dataclass(repr=True)
class Research:
    companies: dict
    locations: dict
    mode: dict
    offers: list

    @property
    def total_jobs(self):
        return len(self.offers)

    @property
    def total_locations(self):
        count = 0
        for location in self.locations.keys():
            count += 1
        return count

    @property
    def total_companies(self):
        count = 0
        for company in self.companies.keys():
            count += 1
        return count

    @property
    def total_modes(self):
        count = 0
        for mode in self.mode.keys():
            count += 1
        return count

    def add_offer(self, offer: Offer):
        self.offers.append(offer)

    def add_by_company(self, offer: Offer):
        # añadir por compañia
        if offer.company:
            if offer.company not in self.companies.keys():
                self.companies[offer.company] = [offer]
            else:
                self.companies[offer.company].append(offer)

    def add_by_location(self, offer: Offer):
        # añadir por localizacion
        if offer.location not in self.locations.keys():
            self.locations[offer.location] = [offer]
        else:
            self.locations[offer.location].append(offer)

    def add_by_mode(self, offer: Offer):
        # añadir por modo de trabajo
        if offer.mode:
            if offer.mode not in self.mode.keys():
                self.mode[offer.mode] = [offer]
            else:
                self.mode[offer.mode].append(offer)


research = Research(dict(), dict(), dict(), list())
