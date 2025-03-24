from typing import Optional


class ScrapParams:
    def __init__(self, url: Optional[str] = None, headers: Optional[dict] = None):
        self.total_items = None
        self.total_pages = None
        self.actual_page = 1
        self.url = url
        self.headers = headers
