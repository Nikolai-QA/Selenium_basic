


class MainPage:
    def __init__(self, browser):
        self.browser = browser
        self.url = "http://192.168.100.49:8081"

    def open(self):
        self.browser.get(self.url)