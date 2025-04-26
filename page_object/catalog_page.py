class CatalogPage:
    def __init__(self, browser):
        self.browser = browser
        self.url = "http://192.168.100.49:8081/en-gb/catalog/desktops"

    def open(self):
        self.browser.get("http://192.168.100.49:8081/en-gb/catalog/desktops")